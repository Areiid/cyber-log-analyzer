import argparse

from analyzer import analyze_logs


def main():
    parser = argparse.ArgumentParser(description="Analyze cybersecurity log files.")
    parser.add_argument(
        "log_file",
        nargs="?",
        default="sample_logs.txt",
        help="Path to the log file to analyze. Defaults to sample_logs.txt.",
    )
    args = parser.parse_args()

    analyze_logs(args.log_file)


if __name__ == "__main__":
    main()
