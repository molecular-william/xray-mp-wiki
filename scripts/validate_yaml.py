#!/usr/bin/env python3
"""
YAML schema validator for xray-mp-wiki entity pages.

Validates YAML files BEFORE rendering to catch errors early with clear messages.
Used by generate/update scripts as a pre-render gate.

Entity types: protein, reagent, method, concept

Usage:
  python validate_yaml.py <type> <name> [--strict]
  python validate_yaml.py protein kirbac-potassium-channels
  python validate_yaml.py reagent lmng --strict
  python validate_yaml.py method size-exclusion-chromatography

Exit codes:
  0 = valid
  1 = errors found
  2 = file not found / other I/O error
"""

import re
import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))
from _base import BASE_DIR, load_yaml

# ─── Tag taxonomy ────────────────────────────────────────────────
PROTEIN_CLASS_TAGS = {
    "gpcr", "ion-channel", "transporter", "enzyme", "receptor",
    "channel", "pump", "porin", "potassium-channel",
}
GENERAL_TAGS = {"membrane-protein", "xray-crystallography"}

REAGENT_DETERGENT_TAGS = {
    "detergent-nonionic", "detergent-zwitterionic", "detergent-ionic",
    "detergent-mild", "detergent-strong",
}
REAGENT_LIPID_TAGS = {
    "lipid", "lipid-monoacyl", "lipid-diacyl", "lipid-sterol", "lipid-analog",
}
REAGENT_ADDITIVE_TAGS = {
    "additive-stabilizer", "additive-reductant", "additive-precipitant",
    "additive-salt", "additive-ph", "additive-ligand", "additive-antibody",
    "additive-metal", "additive-organic-solvent", "additive-alkylating-agent",
    "additive-protease-inhibitor",
}
REAGENT_BUFFER_TAGS = {
    "buffer-tris", "buffer-hepes", "buffer-phosphate",
    "buffer-acetate", "buffer-citrate",
    "buffer-cacodylate", "buffer-mops", "buffer-pipes", "buffer-bicine",
    "buffer-tes", "buffer-glycine", "buffer-ammonium-acetate", "buffer-mes",
    "buffer-additive", "buffer-ches", "buffer-bis-tris-propane", "buffer-tricine",
}
# General reagent tags (non-category-specific)
REAGENT_GENERAL_TAGS = {"ligand", "enzyme", "protease", "solubilization-detergent",
                        "protein-tag", "antibody", "cofactor", "antibiotic", "substrate"}
METHOD_SOLUBILIZATION_TAGS = {
    "solubilization-detergent", "solubilization-lcp", "solubilization-bicelle",
    "solubilization-nanodisc", "solubilization-smalp", "solubilization-maltoside",
    "solubilization-buffer",
}
METHOD_PURIFICATION_TAGS = {
    "purification-affinity", "purification-ion-exchange",
    "purification-size-exclusion", "purification-tag", "purification-fractionation",
}
METHOD_CRYSTALLIZATION_TAGS = {
    "crystallization-vapor-diffusion", "crystallization-lcp",
    "crystallization-microbatch", "crystallization-dialysis",
    "crystallization-sitting-drop", "crystallization-hanging-drop",
}
METHOD_STRUCTURE_DETERMINATION_TAGS = {
    "structure-xray", "structure-sad", "structure-mad",
    "structure-molecular-replacement", "structure-cryoem",
    "structure-refinement", "structure-model-building",
}
METHOD_CELL_LYSIS_TAGS = {"cell-lysis", "cell-lysis-pressure", "cell-lysis-mechanical"}
METHOD_EXPRESSION_TAGS = {"expression-system"}
METHOD_QUALITY_TAGS = {"quality-assessment"}
CONCEPT_TAGS = {
    "concept-transport-mechanism", "concept-protein-family",
    "concept-membrane-mimetic", "concept-crystallography-principle",
    "concept-construct-design", "concept-functional", "concept-antibody-technology",
    "concept-structural", "concept-enzyme-mechanism",
}
SUBDIRECTORY_TAGS = {
    "subdirectory-detergents", "subdirectory-lipids", "subdirectory-buffers",
    "subdirectory-additives", "subdirectory-ligands", "subdirectory-protein-tags",
    "subdirectory-antibodies", "subdirectory-cofactors", "subdirectory-antibiotics",
    "subdirectory-substrates", "subdirectory-crystallization",
    "subdirectory-expression-systems", "subdirectory-purification",
    "subdirectory-structure-determination", "subdirectory-quality-assessment",
    "subdirectory-solubilization", "subdirectory-cell-lysis",
    "subdirectory-concepts",
    # Concept subdirectories
    "subdirectory-transport-mechanisms", "subdirectory-signaling-receptors",
    "subdirectory-structural-mechanisms", "subdirectory-protein-families",
    "subdirectory-enzyme-mechanisms", "subdirectory-rhodopsin-mechanisms",
    "subdirectory-membrane-mimetics", "subdirectory-methods-techniques",
    "subdirectory-construct-design", "subdirectory-miscellaneous",
}

# ─── Schema definitions (uses string references for nested validators) ──

SCHEMAS = {
    "protein": {
        "required_fields": ["title", "tags", "sources", "overview"],
        "optional_fields": ["verified", "structures", "expression", "purifications",
                            "crystallizations", "biological_insights", "cross_references",
                            "mpstruc_classification", "tcdb_classification"],
        "field_types": {
            "title": str,
            "tags": list,
            "sources": list,
            "overview": str,
            "verified": bool,
        },
        "nested_validators": {
            "structures": "protein_structures",
            "expression": "protein_expression",
            "purifications": "protein_purifications",
            "crystallizations": "crystallizations",
            "biological_insights": "biological_insights",
            "cross_references": "cross_references",
        },
    },
    "reagent": {
        "required_fields": ["title", "tags", "sources", "overview"],
        "optional_fields": ["verified", "uses", "examples", "binding", "binding_mode",
                            "advantages", "disadvantages", "comparison",
                            "chemical_name", "chemical_formula", "molecular_weight",
                            "class", "cmc", "hlb", "transition_temp", "head_group",
                            "tail_length", "acyl_chain", "phase_transition", "pka",
                            "ph_range", "concentration_range", "function", "solubility",
                            "typical_concentration", "kd_ki", "clinical_status", "scaffold",
                            "source_organism", "fusion_strategy", "size",
                            "target", "format", "epitope", "isotype",
                            "cross_references"],
        "field_types": {
            "title": str,
            "tags": list,
            "sources": list,
            "overview": str,
            "verified": bool,
        },
        "nested_validators": {
            "uses": "reagent_uses",
            "examples": "reagent_examples",
            "binding": "binding",
            "binding_mode": "binding",
            "comparison": "comparison",
            "cross_references": "cross_references",
        },
    },
    "method": {
        "required_fields": ["title", "tags", "sources"],
        "optional_fields": ["verified", "overview", "principle", "protocol",
                            "advantages", "disadvantages", "proteins_using",
                            "related_methods", "related_reagents",
                            "cross_references", "subdirectory"],
        "field_types": {
            "title": str,
            "tags": list,
            "sources": list,
            "overview": str,
            "verified": bool,
        },
        "nested_validators": {
            "protocol": "protocol",
            "proteins_using": "method_proteins_using",
            "related_methods": "cross_references",
            "related_reagents": "cross_references",
            "cross_references": "cross_references",
        },
    },
    "concept": {
        "required_fields": ["title", "tags", "sources"],
        "optional_fields": ["verified", "overview", "mechanism", "examples", "related_concepts", "cross_references"],
        "field_types": {
            "title": str,
            "tags": list,
            "sources": list,
            "verified": bool,
        },
        "nested_validators": {
            "examples": "concept_examples",
            "cross_references": "cross_references",
        },
    },
}

# Map string names to actual validator functions (populated below)
_NESTED_VALIDATOR_MAP = {}

# ─── Nested validators ───────────────────────────────────────────

def _v_protein_structures(items, errors):
    """structures[]: each item must have source and pdb_id."""
    for i, s in enumerate(items):
        prefix = f"structures[{i}]"
        if not isinstance(s, dict):
            errors.append(f"{prefix}: must be a dict, got {type(s).__name__}")
            continue
        if "source" not in s:
            errors.append(f"{prefix}: missing required field 'source'")
        if "pdb_id" not in s:
            errors.append(f"{prefix}: missing required field 'pdb_id'")
        for field in ["resolution", "space_group", "construct", "ligand"]:
            if field in s and not isinstance(s[field], str):
                errors.append(f"{prefix}.{field}: must be string, got {type(s[field]).__name__}")


def _v_protein_expression(data, errors):
    """expression{}: system and construct should be strings."""
    if not isinstance(data, dict):
        errors.append("expression: must be a dict")
        return
    for field in ["system", "construct"]:
        if field in data and not isinstance(data[field], str):
            errors.append(f"expression.{field}: must be string, got {type(data[field]).__name__}")


def _v_protein_purifications(items, errors):
    """purifications[].steps[]: validate each step."""
    for i, p in enumerate(items):
        prefix = f"purifications[{i}]"
        if not isinstance(p, dict):
            errors.append(f"{prefix}: must be a dict, got {type(p).__name__}")
            continue
        if "steps" in p:
            if not isinstance(p["steps"], list):
                errors.append(f"{prefix}.steps: must be a list")
                continue
            for j, step in enumerate(p["steps"]):
                step_prefix = f"{prefix}.steps[{j}]"
                if not isinstance(step, dict):
                    errors.append(f"{step_prefix}: must be a dict, got {type(step).__name__}")
                    continue
                for field in ["step", "method"]:
                    if field not in step:
                        errors.append(f"{step_prefix}: missing required field '{field}'")
                for field in ["resin", "buffer", "notes"]:
                    if field in step and not isinstance(step[field], str):
                        errors.append(f"{step_prefix}.{field}: must be string, got {type(step[field]).__name__}")
                if "buffer_details" in step:
                    bd = step["buffer_details"]
                    if not isinstance(bd, list):
                        errors.append(f"{step_prefix}.buffer_details: must be a list")
                    else:
                        for k, item in enumerate(bd):
                            if not isinstance(item, dict):
                                errors.append(f"{step_prefix}.buffer_details[{k}]: must be an object")
                            elif "reagent" not in item or not isinstance(item["reagent"], str):
                                errors.append(f"{step_prefix}.buffer_details[{k}].reagent: required, string")


def _v_crystallizations(items, errors):
    """crystallizations[]: each must have source."""
    for i, c in enumerate(items):
        prefix = f"crystallizations[{i}]"
        if not isinstance(c, dict):
            errors.append(f"{prefix}: must be a dict, got {type(c).__name__}")
            continue
        if "source" not in c:
            errors.append(f"{prefix}: missing required field 'source'")
        for field in ["method", "protein_sample", "reservoir", "temperature", "growth_time", "notes"]:
            if field in c and not isinstance(c[field], str):
                errors.append(f"{prefix}.{field}: must be string, got {type(c[field]).__name__}")


def _v_biological_insights(items, errors):
    """biological_insights[]: each must have title."""
    for i, b in enumerate(items):
        prefix = f"biological_insights[{i}]"
        if not isinstance(b, dict):
            errors.append(f"{prefix}: must be a dict, got {type(b).__name__}")
            continue
        if "title" not in b:
            errors.append(f"{prefix}: missing required field 'title'")
        for field in ["content"]:
            if field in b and not isinstance(b[field], str):
                errors.append(f"{prefix}.{field}: must be string, got {type(b[field]).__name__}")


def _v_reagent_examples(items, errors):
    """examples[]: each must have protein link."""
    for i, e in enumerate(items):
        prefix = f"examples[{i}]"
        if not isinstance(e, dict):
            errors.append(f"{prefix}: must be a dict, got {type(e).__name__}")
            continue
        if "protein" not in e:
            errors.append(f"{prefix}: missing required field 'protein'")
        for field in ["concentration", "context", "result"]:
            if field in e and not isinstance(e[field], str):
                errors.append(f"{prefix}.{field}: must be string, got {type(e[field]).__name__}")


def _v_binding(data, errors):
    """binding{} / binding_mode{}: target is required."""
    if not isinstance(data, dict):
        errors.append("binding: must be a dict")
        return
    if "target" not in data:
        errors.append("binding: missing required field 'target'")
    for field in ["interactions", "pocket_volume", "key_residues"]:
        if field in data:
            if isinstance(data[field], list):
                for j, item in enumerate(data[field]):
                    if not isinstance(item, str):
                        errors.append(f"binding.{field}[{j}]: must be string")
            elif not isinstance(data[field], str):
                errors.append(f"binding.{field}: must be string or list of strings")


def _v_comparison(items, errors):
    """comparison[]: each item must be a dict with consistent keys."""
    for i, c in enumerate(items):
        prefix = f"comparison[{i}]"
        if not isinstance(c, dict):
            errors.append(f"{prefix}: must be a dict, got {type(c).__name__}")


def _v_concept_examples(items, errors):
    """examples[]: each must have protein link."""
    for i, e in enumerate(items):
        prefix = f"examples[{i}]"
        if not isinstance(e, dict):
            errors.append(f"{prefix}: must be a dict, got {type(e).__name__}")
            continue
        if "protein" not in e:
            errors.append(f"{prefix}: missing required field 'protein'")
        for field in ["context"]:
            if field in e and not isinstance(e[field], str):
                errors.append(f"{prefix}.{field}: must be string")


def _v_protocol(data, errors):
    """protocol{}: reagents and steps should be lists; conditions should be a dict."""
    if not isinstance(data, dict):
        errors.append("protocol: must be a dict")
        return
    for field in ["reagents", "steps"]:
        if field in data:
            if not isinstance(data[field], list):
                errors.append(f"protocol.{field}: must be a list, got {type(data[field]).__name__}")
    if "conditions" in data:
        if not isinstance(data["conditions"], dict):
            errors.append(f"protocol.conditions: must be a dict, got {type(data['conditions']).__name__}")


def _v_method_proteins_using(items, errors):
    """proteins_using[]: each must have protein, resolution, pdb."""
    for i, p in enumerate(items):
        prefix = f"proteins_using[{i}]"
        if not isinstance(p, dict):
            errors.append(f"{prefix}: must be a dict, got {type(p).__name__}")
            continue
        if "protein" not in p:
            errors.append(f"{prefix}: missing required field 'protein'")
        for field in ["resolution", "pdb"]:
            if field not in p:
                errors.append(f"{prefix}: missing recommended field '{field}' (used in proteins table)")
        for field in ["notes"]:
            if field in p and not isinstance(p[field], str):
                errors.append(f"{prefix}.{field}: must be string")


def _v_uses(items, errors):
    """uses[]: each must have title."""
    for i, u in enumerate(items):
        prefix = f"uses[{i}]"
        if not isinstance(u, dict):
            errors.append(f"{prefix}: must be a dict, got {type(u).__name__}")
            continue
        if "title" not in u:
            errors.append(f"{prefix}: missing required field 'title'")
        if "content" in u and not isinstance(u["content"], str):
            errors.append(f"{prefix}.content: must be string")


def _validate_wikilinks(data, errors, path_prefix=""):
    """Check for non-Jekyll compatible wikilinks like [[entity]].

    Jekyll only supports [text](/xray-mp-wiki/path/) format.
    Rejects [[wikilink]] syntax in ALL string fields.
    """

    if isinstance(data, dict):
        for key, value in data.items():
            field_path = f"{path_prefix}.{key}" if path_prefix else key
            _validate_wikilinks(value, errors, field_path)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            _validate_wikilinks(item, errors, f"{path_prefix}[{i}]")
    elif isinstance(data, str):
        # Check for [[...]] wikilink syntax
        matches = re.findall(r'\[\[([^\]]+)\]\]', data)
        if matches:
            errors.append(f"{path_prefix}: contains non-Jekyll wikilink syntax '[[{matches[0]}]]' — use '[{matches[0]}](/xray-mp-wiki/path/)' instead")


def _validate_cross_references(items, errors):
    """cross_references[]: each must have path, title, reason."""
    for i, ref in enumerate(items):
        prefix = f"cross_references[{i}]"
        if not isinstance(ref, dict):
            errors.append(f"{prefix}: must be a dict, got {type(ref).__name__}")
            continue
        if "path" not in ref:
            errors.append(f"{prefix}: missing required field 'path'")
        elif not re.match(r"/xray-mp-wiki/[a-z-]+/[a-z0-9-]+/?", ref["path"]):
            # Allow /xray-mp-wiki/{type}/{path}/ or /xray-mp-wiki/{type}/{subdir}/{path}/
            if not re.match(r"/xray-mp-wiki/[a-z-]+/[a-z]+/[a-z0-9-]+/?", ref["path"]):
                errors.append(f"{prefix}.path: invalid format '{ref['path']}' — expected /xray-mp-wiki/<type>/<path>/ or /xray-mp-wiki/<type>/<subdir>/<path>/")
        if "title" not in ref:
            errors.append(f"{prefix}: missing required field 'title'")
        if "reason" not in ref:
            errors.append(f"{prefix}: missing recommended field 'reason'")


# ─── Populate validator map ──────────────────────────────────────

_NESTED_VALIDATOR_MAP = {
    "protein_structures": _v_protein_structures,
    "protein_expression": _v_protein_expression,
    "protein_purifications": _v_protein_purifications,
    "crystallizations": _v_crystallizations,
    "biological_insights": _v_biological_insights,
    "reagent_uses": _v_uses,
    "reagent_examples": _v_reagent_examples,
    "binding": _v_binding,
    "comparison": _v_comparison,
    "concept_examples": _v_concept_examples,
    "protocol": _v_protocol,
    "method_proteins_using": _v_method_proteins_using,
    "cross_references": _validate_cross_references,
}


# ─── Core validator ──────────────────────────────────────────────

def _validate_dois(sources, errors):
    """Check DOI format: doi/10.xxxx##yyyy."""
    for s in sources:
        if not isinstance(s, str):
            errors.append(f"source entry: must be string, got {type(s).__name__}: {s!r}")
            continue
        if not re.match(r"doi/\d+\.\d+##\S+", s):
            errors.append(f"source '{s}': invalid DOI format — expected 'doi/10.xxxx##yyyy'")


def _validate_tags(tags, entity_type, errors, strict=False):
    """Check tags against taxonomy (warnings in non-strict mode).

    Rules:
    - Tags must be non-empty list
    - At least one tag must be from the taxonomy (pre-existing)
    - Unknown tags are allowed but reported as warnings (not errors)
    - This allows new tags to be proposed while maintaining a taxonomy anchor
    """
    if not isinstance(tags, list):
        errors.append(f"tags: must be a list, got {type(tags).__name__}")
        return

    # Reject empty tags
    if len(tags) == 0:
        errors.append("tags: cannot be empty")
        return

    # Build known tags from taxonomy sets
    all_known = set()
    if entity_type == "protein":
        all_known = PROTEIN_CLASS_TAGS | GENERAL_TAGS
    elif entity_type == "reagent":
        all_known = (REAGENT_DETERGENT_TAGS | REAGENT_LIPID_TAGS |
                     REAGENT_ADDITIVE_TAGS | REAGENT_BUFFER_TAGS |
                     REAGENT_GENERAL_TAGS)
    elif entity_type == "method":
        all_known = (METHOD_SOLUBILIZATION_TAGS | METHOD_PURIFICATION_TAGS |
                     METHOD_CRYSTALLIZATION_TAGS | METHOD_STRUCTURE_DETERMINATION_TAGS |
                     METHOD_CELL_LYSIS_TAGS | METHOD_EXPRESSION_TAGS |
                     METHOD_QUALITY_TAGS | GENERAL_TAGS)
    elif entity_type == "concept":
        all_known = CONCEPT_TAGS | GENERAL_TAGS

    # Add subdirectory tags (valid for all entity types)
    all_known |= SUBDIRECTORY_TAGS

    # Check for taxonomy anchor: at least one tag must be known
    has_taxonomy_anchor = any(tag in all_known for tag in tags if isinstance(tag, str))
    if not has_taxonomy_anchor:
        errors.append("tags: must include at least one taxonomy-compliant tag")

    # Protein class tag requirement
    if entity_type == "protein":
        has_class_tag = any(tag in PROTEIN_CLASS_TAGS for tag in tags if isinstance(tag, str))
        if not has_class_tag:
            errors.append("tags: protein must have at least one class tag from: gpcr, ion-channel, transporter, enzyme, receptor, channel, pump, porin")

    # Report unknown tags as warnings (not errors)
    unknown_tags = [tag for tag in tags if isinstance(tag, str) and tag not in all_known]
    if unknown_tags:
        errors.append(f"tags: {len(unknown_tags)} unknown tag(s) — add to taxonomy first: {', '.join(unknown_tags)}")


def _check_unquoted_numerics(data, errors, path=""):
    """Recursively find unquoted numeric values (int/float not bool).

    Wiki convention: all numeric values must be quoted strings.
    """
    if isinstance(data, dict):
        for key, val in data.items():
            full_path = f"{path}.{key}" if path else key
            _check_unquoted_numerics(val, errors, full_path)
    elif isinstance(data, list):
        for i, val in enumerate(data):
            _check_unquoted_numerics(val, errors, f"{path}[{i}]")
    elif isinstance(data, (int, float)) and not isinstance(data, bool):
        errors.append(f"unquoted numeric value at '{path}': {data!r} — must be quoted string")


def validate_entity(yaml_data, entity_type, strict=False):
    """Validate a parsed YAML dict against the schema for entity_type.

    Args:
        yaml_data: Parsed YAML dict
        entity_type: One of 'protein', 'reagent', 'method', 'concept'
        strict: If True, tag taxonomy and missing recommended fields are errors
                (not just warnings).

    Returns:
        list of error strings (empty = valid).
    """
    errors = []
    schema = SCHEMAS.get(entity_type)
    if not schema:
        errors.append(f"Unknown entity type: {entity_type!r}")
        return errors

    # Check required fields
    for field in schema["required_fields"]:
        if field not in yaml_data:
            errors.append(f"missing required field: '{field}'")
        elif schema["field_types"].get(field) and not isinstance(yaml_data[field], schema["field_types"][field]):
            expected = schema["field_types"][field].__name__
            actual = type(yaml_data[field]).__name__
            errors.append(f"'{field}': expected {expected}, got {actual}")

    # Non-empty overview check
    if "overview" in yaml_data and isinstance(yaml_data["overview"], str) and not yaml_data["overview"].strip():
        errors.append("'overview': empty string — provide description content")

    # created/updated recommended
    if "created" not in yaml_data or not yaml_data.get("created"):
        errors.append("missing recommended field: 'created' (add YYYY-MM-DD date)")
    if "updated" not in yaml_data or not yaml_data.get("updated"):
        errors.append("missing recommended field: 'updated' (add YYYY-MM-DD date)")

    # Check sources DOI format
    if "sources" in yaml_data:
        _validate_dois(yaml_data["sources"], errors)

    # Check tags
    if "tags" in yaml_data:
        _validate_tags(yaml_data["tags"], entity_type, errors, strict)

    # Check nested structures (resolve string names to functions)
    for field, validator_ref in schema.get("nested_validators", {}).items():
        if field in yaml_data:
            fn = _NESTED_VALIDATOR_MAP.get(validator_ref)
            if fn:
                fn(yaml_data[field], errors)
            else:
                errors.append(f"nested validator '{validator_ref}' for '{field}' not found")

    # Check for non-Jekyll wikilink syntax [[...]] in ALL string fields
    _validate_wikilinks(yaml_data, errors)

    # Check for unquoted numeric values
    _check_unquoted_numerics(yaml_data, errors)

    return errors


# ─── CLI entry point ────────────────────────────────────
# Replacement for validate_cli.py (consolidated here for simplicity)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Validate YAML schema for xray-mp-wiki entities")
    parser.add_argument("type", nargs="?", choices=["protein", "reagent", "method", "concept"],
                        help="Entity type")
    parser.add_argument("name", nargs="?", help="Entity name (basename without .yaml)")
    parser.add_argument("--strict", action="store_true",
                        help="Treat unknown tags and missing recommended fields as errors")
    args = parser.parse_args()

    if not args.type or not args.name:
        print("Usage: python validate_yaml.py <type> <name> [--strict]")
        print("Types: protein, reagent, method, concept")
        sys.exit(2)

    type_dir_map = {
        "protein": "proteins_yaml",
        "reagent": "reagents_yaml",
        "method": "methods_yaml",
        "concept": "concepts_yaml",
    }
    yaml_dir = BASE_DIR / "xray-mp-wiki" / type_dir_map[args.type]
    yaml_path = yaml_dir / f"{args.name}.yaml"

    if not yaml_path.exists():
        print(f"Error: YAML file not found: {yaml_path}", file=sys.stderr)
        sys.exit(2)

    try:
        yaml_data = load_yaml(yaml_path)
    except Exception as e:
        print(f"Error loading YAML: {e}", file=sys.stderr)
        sys.exit(2)

    errors = validate_entity(yaml_data, args.type, strict=args.strict)

    if errors:
        print(f"Schema validation FAILED for {args.name} ({args.type}):")
        print(f"  File: {yaml_path}")
        print()
        for i, err in enumerate(errors, 1):
            print(f"  {i}. {err}")
        print(f"\n  {len(errors)} error(s) found. Fix before generating page.")
        sys.exit(1)
    else:
        print(f"✓ {args.name} ({args.type}) — schema valid")
        sys.exit(0)
