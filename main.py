from Web_crawler.link_retrieve import link_compiler
from Web_crawler.scrapper_bs import  compiled_scrapper
from book_compiler.epub_compiler import create_epub

url = input("URL of The Starting Chapter: ")
num_chapters_to_scrape = int(input("Number of Chapters: "))

# Extract novel name from URL
novel_name = url.split('/book/')[1].split('/')[0]

# Initialize lists to store chapter content and chapter numbers


chapter_links = link_compiler(url, num_chapters_to_scrape)

chapter_contents,chapter_titles = compiled_scrapper(chapter_links)

#print(chapter_titles[2].replace(" ", "_"))
# Export the content to ePub
create_epub(chapter_contents, novel_name, chapter_titles)
