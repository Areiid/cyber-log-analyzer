from collections import Counter

FAILED_LOGIN_TEXT = "FAILED LOGIN"
ALERT_THRESHOLD = 3

def extract_ip(line):
    parts = line.split()

    for part in parts:
        if part.startswith("ip="):
            return part.replace("ip=", "")

    return None

def analyze_logs(file_path):
    failed_ips = []

    with open(file_path, "r") as file:
        for line in file:
            if FAILED_LOGIN_TEXT in line:
                ip_address = extract_ip(line)

                if ip_address:
                    failed_ips.append(ip_address)

    ip_counts = Counter(failed_ips)

    print("\nCybersecurity Log Analyzer Report")
    print("--------------------------------")
    print(f"Total failed login attempts: {len(failed_ips)}\n")

    for ip, count in ip_counts.items():
        print(f"IP Address: {ip} | Failed Attempts: {count}")

        if count >= ALERT_THRESHOLD:
            print(f"ALERT: Suspicious activity detected from {ip}")

if __name__ == "__main__":
    analyze_logs("sample_logs.txt")