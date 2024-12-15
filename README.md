# Instagram-Scraper

A Python-based project that leverages Selenium to scrape Instagram followers, fetch profile details, and extract Personally Identifiable Information (PII) from text files. The project is designed to automate Instagram tasks and analyze data for insights. It is built using the Selenium library and includes functionality for saving credentials and restoring sessions via cookies.

# Prerequisites

- Python 3.8 or higher. Install it [here](https://www.python.org/downloads/).
- Chrome browser and the matching ChromeDriver. Install Chrome [here](https://www.google.com/chrome/) and download ChromeDriver [here](https://sites.google.com/chromium.org/driver/).


---

# Features

- **Follower Scraping**: Scrape followers of any public profile.
- **Profile Details Fetching**: Fetch name and bio of Instagram profiles.
- **PII Extraction**: Extract sensitive information like email addresses, phone numbers, and postal codes from text files.

---

# Installation

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

# Usage

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

# Configuration

config.ini: Stores Instagram credentials (username and password).

data_files/: Directory to store text files for PII analysis.

requirements.txt: Contains required Python dependencies.

---

# Pattern Match

To extract Personally Identifiable Information (PII) such as email addresses, phone numbers, and postal codes from text files, you can use Python with regular expressions. Below is an example script with regex patterns to identify these types of PII:


# Disclaimer
This project is intended for educational and ethical purposes only. Scraping platforms like Instagram may violate their terms of service. Use responsibly.

---

# Purpose
The Instagram Scraper project was developed as part of a practical exploration for the <ins>**Privacy, Compliance, and Human Aspects of Cybersecurity**</ins> course. The goal was to understand how publicly available data on social media platforms, such as Instagram, can be collected, analyzed, and used in ways that highlight potential privacy concerns while adhering to ethical and legal standards.

This project serves as a hands-on tool for exploring the intersection of technology, privacy, and compliance, particularly in the context of:

Data Collection: Demonstrating how publicly accessible data can be retrieved using web scraping techniques.
Privacy Implications: Identifying sensitive data (PII) exposed by users and assessing its potential misuse.
Compliance Requirements: Analyzing how platforms and users can align with regulations such as GDPR and CCPA.
Academic Context
This project reflects the application of cybersecurity principles to real-world scenarios, with a strong emphasis on:

Privacy Awareness:

Educating individuals and organizations about the potential risks of exposing PII in public spaces.
Highlighting how easily accessible data can inadvertently lead to privacy violations.
Compliance with Legal Frameworks:

Exploring how tools like this align or conflict with privacy regulations (e.g., GDPR, HIPAA, CCPA).
Emphasizing responsible usage in accordance with Instagram's Terms of Service.
Human Aspects of Cybersecurity:

Studying user behavior on social media and understanding how human factors contribute to privacy risks.
Encouraging ethical decision-making in the development and use of data scraping tools.
Key Use Cases
Social Media Analytics:

Analyze engagement patterns, profile bios, and follower lists to understand user interactions on Instagram.
Open-Source Intelligence (OSINT):

Provide a framework for ethical OSINT investigations by collecting public data for legitimate research purposes.
Education and Research:

Serve as a teaching tool for students and professionals to learn web scraping with Python and Selenium.
Raise awareness about privacy risks associated with oversharing on social media platforms.
Data Privacy and Compliance Audits:

Assess how much PII is openly available and develop strategies to mitigate such risks for individuals and organizations.
Ethical and Legal Considerations
As a project focused on privacy, this tool emphasizes the importance of responsible use:

Respecting Instagram's Terms of Service: The tool should not be used to bypass restrictions or collect data from private profiles.
Protecting Privacy: Ensure that the scraping is limited to publicly accessible information.
Compliance with Regulations: Adhere to privacy laws such as GDPR and CCPA when handling collected data.
This project aligns with the broader goals of the course to evaluate the technical, legal, and human dimensions of cybersecurity and privacy.

---

# Adapting the Project for Other Platforms
This project was initially designed for Instagram, but the core principles and techniques can be extended to other platforms with similar features. With modifications, this scraper can be tailored to collect publicly available data from platforms such as Twitter, LinkedIn, or Facebook, provided the usage adheres to ethical and legal standards.

How to Modify for Other Platforms
Update the Target URLs:

Replace Instagram-specific URLs (https://www.instagram.com/...) with the equivalent endpoints for the target platform (e.g., Twitter profiles, LinkedIn public pages).
Adjust HTML Element Selectors:

Platforms have different HTML structures. Use browser developer tools (e.g., Chrome DevTools) to inspect the elements you want to target, such as:
Profile names
Bio descriptions
Follower/following lists
Update the XPath or CSS selectors in the script to match the new platform's structure.
Modify Authentication Logic:

Different platforms have unique login flows. Update the script to interact with the login page and input fields for the new platform.
For platforms with OAuth or multi-factor authentication, additional steps may be required.
Revise Scraping Logic:

Some platforms use infinite scrolling (e.g., LinkedIn) or load data dynamically via AJAX (e.g., Twitter). Adjust the scrolling and data fetching logic to handle these cases.
Update Compliance and Rate Limiting:

Implement platform-specific rate limits to prevent getting blocked or flagged.
Incorporate API access if the platform provides a public API (e.g., Twitter API, LinkedIn API), as this is often more reliable and compliant than scraping.
Example Modifications for Other Platforms
Twitter:

Target public tweets, bios, or follower/following lists.
Modify login and data fetching logic to handle Twitter’s layout and dynamic content.
Alternatively, use the Twitter API for better reliability and rate limit handling.
LinkedIn:

Focus on public profiles, connections, and skills data.
Adjust the scrolling logic to scrape content from dynamically loaded pages.
Ensure compliance with LinkedIn's strict anti-scraping policies.
Facebook:

Target public pages or group member lists.
Adjust element selectors for Facebook’s unique DOM structure.
Ensure strict compliance with Facebook’s terms of service.
Reddit:

Scrape post titles, comments, or user bios from public subreddits.
Update the script to handle Reddit’s API endpoints or HTML structure.
Challenges and Considerations
Dynamic Content:

Many platforms use JavaScript frameworks to load content dynamically, requiring tools like Selenium or Puppeteer for accurate scraping.
Rate Limiting and Captchas:

Platforms may impose rate limits or captchas to deter scraping. Use tools like selenium-stealth or third-party services for captcha solving.
Ethics and Compliance:

Always respect the terms of service and legal frameworks for the platform you are targeting.
Use APIs when possible, as they are officially supported and less likely to result in bans.



