import streamlit as st
from book_compiler.epub_compiler import create_epub
from Translation.translator import translate_chapters
from Web_crawler.web_crawler import WebScraper

# Streamlit app configuration
st.set_page_config(page_title="Novel Scraper", layout="centered")

# App title
st.title("Novel Scraper and Translator")

# Input fields for user
url = st.text_input("URL of the Starting Chapter:", placeholder="https://www.quanben.io/chapter/start_page.html")
num_chapters_to_scrape = st.number_input("Number of Chapters to Scrape:", min_value=1, max_value=1000, value=10)
translate_bool = st.checkbox("Translate Chapters to English?")
book_name = st.text_input("Give Book Name (Optional):", placeholder="Leave blank to auto-detect from URL")

# Initialize the WebScraper
scraper = WebScraper("https://www.quanben.io")

# Start scraping when the button is clicked
if st.button("Start Scraping"):
    if url:
        # Determine novel name
        if book_name:
            novel_name = book_name
        else:
            # Extract novel name from URL
            try:
                novel_name = url.split('/book/')[1].split('/')[0]
            except:
                novel_name = url.split('/')[-2]

        # Scraping progress message
        st.write("Scraping chapters... Please wait.")
        with st.spinner("Scraping in progress..."):
            chapter_contents, chapter_titles = scraper.scrape_chapters(url, num_chapters_to_scrape)

        if chapter_contents:
            st.success(f"Scraped {len(chapter_titles)} chapters successfully!")

            # Optional translation
            if translate_bool:
                st.write("Translating chapters... Please wait.")
                with st.spinner("Translation in progress..."):
                    chapter_contents = translate_chapters(chapter_contents)
                st.success("Chapters translated successfully!")

            # ePub creation
            st.write("Creating ePub file... Please wait.")
            with st.spinner("Generating ePub..."):
                epub_filename = create_epub(chapter_contents, novel_name, chapter_titles)
            st.success("ePub file created successfully!")

            # Provide a download link for the ePub file
            
            with open(epub_filename, "rb") as epub_file:
                st.download_button(
                    label="Download ePub",
                    data=epub_file,
                    file_name=epub_filename,
                    mime="application/epub+zip",
                )
        else:
            st.error("No chapters were scraped. Please check the URL and try again.")
    else:
        st.error("Please enter a valid starting chapter URL.")
