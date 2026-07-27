import json
import logging
from pathlib import Path

def main():
    project_path = Path.cwd()

    log_folder = project_path / "logs"
    log_folder.mkdir(exist_ok=True)

    logging.basicConfig(
        filename = log_folder / "app.log",
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        )

    json_file = project_path / "data" / "tasks.json"

    try:
        with open(json_file, "r") as file:
            data = json.load(file)

        logging.info("tasks.json berhasil dibaca.")
        print(data)

    except FileNotFoundError:
        logging.error("tasks.json tidak ditemukan.")
        print("tasks.json tidak ditemukan")

if __name__ == "__main__":
    main()