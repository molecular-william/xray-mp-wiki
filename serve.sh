#!/bin/bash
set -e

cd "$(dirname "$0")"

# Run jekyll serve with livereload
bundle exec jekyll serve --livereload "$@" &
Jekyll_PID=$!

# Wait for jekyll to start
sleep 2

# Run post-build scripts
python3 scripts/generate-random-pages.py
python3 scripts/generate-health.py

cat > _site/random.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Random Page</title>
</head>
<body>
<script>
fetch('random_pages.json')
  .then(response => response.json())
  .then(pages => {
    if (pages.length > 0) {
      const randomIndex = Math.floor(Math.random() * pages.length);
      window.location.href = pages[randomIndex];
    }
  })
  .catch(error => console.error('Error loading random pages:', error));
</script>
</body>
</html>
EOF

# Wait for jekyll process
wait $Jekyll_PID
