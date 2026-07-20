"""Batch-download Elsevier SI PDFs via ars.els-cdn.com CDN (no auth needed)."""
import re, time
from pathlib import Path
from urllib.request import Request, urlopen

DOI_FILE = Path("raw/datasets/missing_detergent_dois.txt")
OUT_DIR = Path("raw/supplementary")
# PII can contain uppercase letters (check digits), e.g. S0006291X20321392
PII_RE = re.compile(r'/(?:retrieve/)?pii/(S[A-Z0-9]{10,20})', re.I)
DOI_AS_PII = re.compile(r'^S[A-Z0-9]{10,20}$', re.I)
SKIP_HOSTED = ["J.FEBSLET", "j.febslet", "FEBSLET"]
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"

out_dir = OUT_DIR
out_dir.mkdir(parents=True, exist_ok=True)
existing = {f.name for f in out_dir.glob("*")}

dois = [l.strip() for l in DOI_FILE.read_text().splitlines() if l.strip()]
elsevier = [d for d in dois if "10.1016" in d]
print(f"Total: {len(dois)}, Elsevier: {len(elsevier)}")

def fetch(url, method="GET"):
    req = Request(url, method=method)
    req.add_header("User-Agent", UA)
    req.add_header("Referer", "https://www.sciencedirect.com/")
    return urlopen(req, timeout=15)

downloaded = 0
for i, doi in enumerate(elsevier):
    frag = doi.split("##")[-1]
    if any(skip in frag for skip in SKIP_HOSTED):
        continue

    pii = None
    doi_url = doi.replace("##", "/").replace("doi/", "https://doi.org/")

    if DOI_AS_PII.match(frag):
        pii = frag

    if not pii:
        try:
            resp = fetch(doi_url, method="HEAD")
            m = PII_RE.search(resp.url)
            if m:
                pii = m.group(1)
        except Exception:
            pass

    if not pii:
        continue  # silent skip

    for suffix in ["-mmc1.pdf", "-mmc2.pdf", "-mmc1.docx", "-mmc2.zip"]:
        cdn_url = f"https://ars.els-cdn.com/content/image/1-s2.0-{pii}{suffix}"
        out_name = f"1-s2.0-{pii}{suffix}"
        if out_name in existing:
            break
        try:
            hresp = fetch(cdn_url, method="HEAD")
            if hresp.status == 200:
                data = fetch(cdn_url).read()
                (out_dir / out_name).write_bytes(data)
                print(f"  [{i+1}/{len(elsevier)}] {pii}{suffix} ({len(data)//1024}KB)")
                downloaded += 1
                break
        except Exception:
            continue

    if (i + 1) % 30 == 0:
        time.sleep(0.5)

print(f"\nDownloaded: {downloaded}/{len(elsevier)} Elsevier DOIs")

# Self-check
if __name__ == "__main__":
    test_url = f"https://ars.els-cdn.com/content/image/1-s2.0-S2211124715004623-mmc1.pdf"
    try:
        r = fetch(test_url, method="HEAD")
        assert r.status == 200, f"Self-check: {r.status}"
        print("Self-check: CDN OK")
    except Exception as e:
        print(f"Self-check: {e}")
