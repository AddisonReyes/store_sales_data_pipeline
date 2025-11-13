import subprocess
import sys


def main() -> None:
    print("Starting data pipeline...\n")

    steps = [
        ("Generating data...", "data_generator.py"),
        ("Transforming data...", "transform_data.py"),
        ("Uploading to the database...", "load_db.py"),
        ("Generating analysis...", "analyze_data.py"),
    ]

    for message, script in steps:
        print(f"▶ {message}")
        subprocess.run([sys.executable, script])
        print()

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    main()
