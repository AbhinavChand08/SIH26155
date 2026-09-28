import re

def detect_config_type(file_path):
    """
    Detect configuration grammar.

    Returns:
        indent
        brace
        config_edit
        xml
        set
        json
    """

    text = open(file_path, encoding="utf-8", errors="ignore").read(4000)

    if text.lstrip().startswith("<"):
        return "xml"

    if "{" in text and "}" in text:
        return "brace"

    if re.search(r"^\s*config\s+", text, re.MULTILINE):
        return "config_edit"

    if re.search(r"^\s*set\s+", text, re.MULTILINE):
        return "set"

    if text.lstrip().startswith("{") or text.lstrip().startswith("["):
        return "json"

    return "indent"