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
