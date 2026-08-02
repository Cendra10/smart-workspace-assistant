import json
import logging
import sys
from pathlib import Path


def show_version():
    print("Version 1.0.0")

def show_help():
    print("""
Smart Workspace Assistant
    
Available Commands:
    
help          Show help information
version       Show application version
report        Show task report""")

def show_unknown(command):
    print(f"Unknown Command: {command}")  

def show_report():
    project_path = Path.cwd()

    log_folder = project_path / "logs"
    log_folder.mkdir(exist_ok=True)

    logging.basicConfig(
        filename = log_folder / "app.log",
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        )

    json_file = project_path/ "data" / "tasks.json"

    try:
        with open(json_file, "r") as file:
            data = json.load(file)

            print("---Smart Workspace Report---")
            tasks = data["tasks"]

            if len(tasks) == 0 :
                print("Belum ada task.")
                return

            for nomor, task in enumerate(tasks, start = 1):
                print(f"{nomor}. {task}")

        logging.info("tasks.json berhasil dibaca.")
    except FileNotFoundError:
        logging.error("tasks.json tidak ditemukan.")
        print("tasks.json tidak ditemukan")

def main():
    if len(sys.argv) < 2 :
        show_help()
        return
    
    command = sys.argv[1]

    if command == "help":
        show_help()
    elif command == "version":
        show_version()
    elif command == "report":
        show_report()
    else:
        show_unknown(command)

if __name__ == "__main__":
    main()