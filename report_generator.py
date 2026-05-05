def save_report(data):
    with open("report.txt", "w") as f:
        for ip, count in data.items():
            f.write(f"{ip}: {count}\n")