def extract_ip(line):
    parts = line.split()
    for part in parts:
        if part.startswith("ip="):
            return part.replace("ip=", "")
    return None