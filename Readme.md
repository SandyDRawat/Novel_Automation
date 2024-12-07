# Novel Scraper and EPUB Compiler

This project is a Python-based tool for scraping novel chapters from the web and compiling them into an EPUB file. If the content is in Chinese, the tool can translate it into English before compilation. The application leverages **BeautifulSoup** for web scraping, **Ebooklib** for EPUB creation, and an optional translation API (e.g., Google Translate) for content translation.

---

## Features

- **Web Scraping**: Fetches chapter content and titles from novel websites.
- **EPUB Compilation**: Compiles scraped chapters into a structured EPUB file, complete with a table of contents and styling.
- **Content Translation**: Translates Chinese text to English for accessibility to a wider audience.
- **Customizable**: Supports customization for different websites by modifying scraping logic.

---

## Requirements

### Python Version
- Python 3.7 or higher

### Dependencies
Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
---
## Setup

### Clone the Repository
```bash
git clone https://github.com/yourusername/novel-scraper.git
cd novel-scraper
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
- Modify Base URL and Start URL: Update the `base_url` and `start_url` in the code to point to the target novel website.

---
Usage


### Running the Scraper

1.  Open the `main.py` file and update the following:

    -   `base_url`: Base URL of the website.
    -   `start_url`: URL of the first chapter.
    -   `num_chapters`: Number of chapters to scrape.
2.  Run the script:

    bash

    Copy code

    `python main.py`

3.  The script will:

    -   Fetch chapters from the specified `start_url`.
    -   Extract content and titles for the desired number of chapters.
    -   Translate content to English (if in Chinese).
    -   Compile the chapters into an EPUB file saved in the `books` folder.

