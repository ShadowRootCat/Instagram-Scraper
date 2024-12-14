# Instagram-Scraper

A Python-based project that leverages Selenium to scrape Instagram followers, fetch profile details, and extract Personally Identifiable Information (PII) from text files. The project is designed to automate Instagram tasks and analyze data for insights. It is built using the Selenium library and includes functionality for saving credentials and restoring sessions via cookies.

# Prerequisites

- Python 3.8 or higher. Install it [here](https://www.python.org/downloads/).
- Chrome browser and the matching ChromeDriver. Install Chrome [here](https://www.google.com/chrome/) and download ChromeDriver [here](https://sites.google.com/chromium.org/driver/).


---

Features

- **Follower Scraping**: Scrape followers of any public profile.
- **Profile Details Fetching**: Fetch name and bio of Instagram profiles.
- **PII Extraction**: Extract sensitive information like email addresses, phone numbers, and postal codes from text files.

---

Installation

1. Clone the repository:

```bash
git clone https://github.com/username/Instagram-Scraper.git
cd Instagram-Scraper
```


2. Install dependencies:

```bash
pip install -r requirements.txt
```


3. Add chromedriver to your system path.

---

Usage

Save Instagram Credentials
Run the script and save your Instagram credentials:

```python
python3 scripts/scrape_followers.py
```


Scrape Followers
Fetch followers of a public profile:

```python
python3 scripts/scrape_followers.py
```


---

Configuration

config.ini: Stores Instagram credentials (username and password).

data_files/: Directory to store text files for PII analysis.

requirements.txt: Contains required Python dependencies.

---

Disclaimer
This project is intended for educational and ethical purposes only. Scraping platforms like Instagram may violate their terms of service. Use responsibly.
