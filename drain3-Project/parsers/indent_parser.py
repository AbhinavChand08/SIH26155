from pathlib import Path

def flatten_config(input_file, output_file, separator=">"):
    """
    Convert indentation-based network configs into hierarchical commands.

    Example:
        interface Gi0/1
         ip address 10.0.0.1
         shutdown

    becomes:
        interface Gi0/1>ip address 10.0.0.1
        interface Gi0/1>shutdown
    """

    stack = []
    output = []

    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:

        for line in f:

            raw = line.rstrip()

            # Skip empty lines and comments
            if not raw or raw.strip().startswith("!"):
                continue

            indent = len(raw) - len(raw.lstrip(" "))
            level = indent

            command = raw.strip()

            while len(stack) > level:
                stack.pop()

            if level == 0:
                stack = [command]

            else:
                stack.append(command)
                output.append(separator.join(stack))

    Path(output_file).write_text("\n".join(output), encoding="utf-8")

    return output_file