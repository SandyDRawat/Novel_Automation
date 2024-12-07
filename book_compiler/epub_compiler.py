from ebooklib import epub
import os

def create_epub(chapter_contents, novel_name, chapter_titles):
    # Find start and end chapters for the EPUB filename
    start_chapter = chapter_titles[0].split('-')[0].split(':')[0].split(' ')[-1]
    end_chapter = chapter_titles[-1].split('-')[0].split(':')[0].split(' ')[-1]
    epub_name = f"books/{novel_name}_{start_chapter}to{end_chapter}.epub"  # Assumes 'books/' directory exists
    
    # Create the EPUB book object
    book = epub.EpubBook()
    book.set_identifier(epub_name)  # Use the filename as an identifier
    book.set_title(novel_name)      # Set the title of the book
    book.set_language('en')         # Hardcoded language; may not be accurate
    #book.add_author("Author Name")  # Replace with actual author name if available

    # Initialize table of contents and spine
    book.toc = []  # Table of contents
    spine = ['nav']  # The spine (reading order)

    for i, contents in enumerate(chapter_contents):
        # Concatenate chapter content into a single string with paragraph tags
        content = ''
        for entries in contents:
            content += f'<p style="margin-bottom: 1em;">{entries}</p>\n'

        # Construct chapter content with title as a header
        chapter_content_with_title = f'<h1>{chapter_titles[i]}</h1>\n{content}'
        
        # Create chapter object
        chapter_file_name = f'chap_{i+1}.xhtml' # Filename for the chapter
        chapter = epub.EpubHtml(
            title=chapter_titles[i],   # Title for the chapter
            file_name=chapter_file_name,  
            lang='en' 
        )
        chapter.content = chapter_content_with_title  # Set the content of the chapter
        
        # Add chapter to the book
        book.add_item(chapter)
        book.toc.append(chapter)  # Add chapter to the table of contents
        spine.append(chapter)     # Add chapter to the spine

    # Add NCX and navigation files (Required for EPUB)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # Define and add CSS for styling
    style = 'body { font-family: Times, Times New Roman, serif; }' 
    nav_css = epub.EpubItem(
        uid="style_nav",
        file_name="style/nav.css", 
        media_type="text/css", 
        content=style 
    )
    
    book.add_item(nav_css)  # Add CSS to the book
    
    # Set the spine (defines reading order)
    book.spine = spine
    
    # Create EPUB file
    epub.write_epub(epub_name, book)
    print(f"EPUB file created at: {epub_name}")
    return epub_name  # Return the filename for reference
 