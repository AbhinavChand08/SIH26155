from pathlib import Path

from detector import detect_config_type
from parsers.indent_parser import flatten_config


def flatten_file(input_file, output_dir):
    """
    Detect config type and flatten it.

    Returns:
        Path to the flattened file.
    """

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{Path(input_file).stem}_flat.txt"

    config_type = detect_config_type(input_file)

    if config_type == "indent":
        flatten_config(input_file, output_file)

    elif config_type == "brace":
        raise NotImplementedError("Brace parser not added yet.")

    elif config_type == "config_edit":
        raise NotImplementedError("Fortinet parser not added yet.")

    elif config_type == "xml":
        raise NotImplementedError("XML parser not added yet.")

    elif config_type == "set":
        raise NotImplementedError("SET parser not added yet.")

    elif config_type == "json":
        raise NotImplementedError("JSON parser not added yet.")

    else:
        raise ValueError(f"Unknown config type: {config_type}")

    return output_file