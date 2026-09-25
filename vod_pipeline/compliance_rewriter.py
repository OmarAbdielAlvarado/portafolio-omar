"""Card-network compliance rewriter for VOD metadata (ES/EN).
Removes terms prohibited by Visa/Mastercard content policies before publishing.
Rules live in banned_terms.json: add a network/locale without touching code."""
import json, os, re
from flask import Blueprint, jsonify
_rules = json.load(open(os.path.join(os.path.dirname(__file__), "banned_terms.json"), encoding="utf-8"))
def adapt(text, rules):
    for p, r in rules.items(): text = re.sub(p, r, text, flags=re.IGNORECASE)
    return text
bp = Blueprint("compliance", __name__)
@bp.route("/api/compliance-seo/<scene_id>")
def compliant_seo(scene_id):
    path = os.path.join(os.environ.get("SEO_DIR", "/data/seo"), f"{scene_id}.json")
    if not os.path.exists(path): return jsonify({"error": "not found"}), 404
    d = json.load(open(path, encoding="utf-8"))
    both = {**_rules["es"], **_rules["en"]}
    return jsonify(spanish=adapt("\n\n".join(d.get("spanish", [])), _rules["es"]),
                   english=adapt("\n\n".join(d.get("english", [])), _rules["en"]),
                   tags=[adapt(t, both) for t in d.get("tags", [])])
