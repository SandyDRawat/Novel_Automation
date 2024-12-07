# Novel Scraper and EPUB Compiler

This project is a Python-based tool for scraping novel chapters from the web and compiling them into an EPUB file. If the content is in Chinese, the tool can translate it into English before compilation. The application leverages BeautifulSoup for web scraping, Ebooklib for EPUB creation, and an optional translation tool using a Hugging Face LLM model (Rawsand/opus-mt-zh-en-finetuned-zh-to-en). This model is based on the Helsinki-NLP/opus-mt-zh-en base model and is fine-tuned on a custom dataset of translated novels for content translation.

---

## Features

- **Web Scraping**: Fetches chapter content and titles from novel websites.
- **EPUB Compilation**: Compiles scraped chapters into a structured EPUB file, complete with a table of contents and styling.
- **Content Translation**: Translates Chinese text to English for accessibility to a wider audience.
- **Customizable**: Supports customization for different websites by modifying scraping logic.

---

## Supported Webisites
-    Novel-bin.com
-    quanben.io
#### Note:   Read the disclaimer below
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

---
## Usage

### Running the Scraper

- If default websites have the content you desire then just run `app.py` file and give the inputs and you can download the desired files:
```bash
streamlit run app.py
```
- Else
1.  Open the `app.py` file and update the following:

    -   `base_url`: Base URL of the website.

2.  Open the `web_crawler.py` file and update the tags to reterieve the contents as per you target website namely:

    -  Then content element tag
    -  chapter title tag
    -  Next chapter link tag
    -  Also check if the url in next chapter link element is relative( not starts with http://websitename.com) or not. and if not remove it from next chapter link method as also mentionded in the comments there.

3.  Then run `app.py` script which will:

    -   Start a local hosted streamlit app dashboard.
    -   Fill the necessary input feilds.
    -   Use Translate checkbox if translating content to English (from Chinese) is needed.
    -   Wait as translation takes time and then download the epub file.

---
# project Structure
```Plaintext
📦novel-scraper
 ┣ 📂books              # Folder for storing generated EPUB files
 ┣ 📂Web_crawler           # Web scraping module
 ┃ ┗ 📜web_crawler.py   # Logic for fetching and parsing chapter content
 ┣ 📂Translation           # Translation module
 ┃ ┗ 📜translator.py    # Logic for translation
 ┣ 📂book_compiler         # EPUB creation module
 ┃ ┗ 📜epub_compiler.py # Logic for compiling chapters into EPUB
 ┣ 📜app.py             # Script to run the streamlit app
 ┣ 📜README.md          # Documentation
 ┗ 📜requirements.txt   # Python dependencies
```
---

## Disclaimer

This tool is intended for personal use only. Before using this tool to scrape content from any website, ensure that your actions comply with the website's terms of service and privacy policies.  

### Websites Tested
- [Quanben.io](https://www.quanben.io) (Chinese novels): As of now, the `robots.txt` file allows scraping with `User-agent: * Allow: /`.
- [Novel-bin](https://novel-bin.com) (English novels): Allows scraping for personal use as per the website's terms.  

**Note**: While the `robots.txt` file for Quanben.io permits scraping, and the English website's terms allow personal use, this does not constitute blanket permission. It is your responsibility to verify and adhere to the rules of the specific website you are scraping.  

The project creator is not responsible for any misuse of this tool or legal issues arising from non-compliance with website policies.

