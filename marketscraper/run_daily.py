import subprocess
import datetime
import os

# Απόλυτο path του project (ο φάκελος που περιέχει το settings.py)
PROJECT_DIR = r"C:\Users\user\Documents\Python\PythonProject\marketscraper\marketscraper"

# Path προς το python.exe του virtual environment
VENV_PYTHON = r"C:\Users\user\Documents\Python\PythonProject\.venv\Scripts\python.exe"


def run_spider():
    print(f"[{datetime.datetime.now()}] ▶️ Εκκίνηση spider...")

    subprocess.run(
        [VENV_PYTHON, "-m", "scrapy", "crawl", "sklspider"],
        cwd=PROJECT_DIR
    )

    print(f"[{datetime.datetime.now()}] ✅ Ολοκληρώθηκε scraping.\n")


if __name__ == "__main__":
    run_spider()
