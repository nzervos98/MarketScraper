import subprocess
import datetime
import os
from datetime import date

# Απόλυτο path του project
PROJECT_DIR = r"C:\Users\user\Documents\Python\PythonProject\marketscraper\marketscraper"

# Path προς το python.exe του virtual environment
VENV_PYTHON = r"C:\Users\user\Documents\Python\PythonProject\.venv\Scripts\python.exe"


def run_spider():
    print(f"[{datetime.datetime.now()}] ▶️ Εκκίνηση crawl...")
    with open("marketscraper/copy.txt", "a", encoding="utf-8") as file:
        file.write(f'----------{date.today()}----------\n')

    subprocess.run(
        [VENV_PYTHON, "-m", "scrapy", "crawl", "sklspider"],
        cwd=PROJECT_DIR
    )

    print(f"[{datetime.datetime.now()}] ✅ Ολοκληρώθηκε.\n")


if __name__ == "__main__":
    run_spider()
