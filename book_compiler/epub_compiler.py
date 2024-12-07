from ebooklib import epub
import os

def create_epub(chapter_contents, novel_name, chapter_titles):
    
    # Derive chapter range for EPUB filename
    start_chapter = chapter_titles[0].split('-')[0].split(':')[0].split(' ')[-1]
    end_chapter = chapter_titles[-1].split('-')[0].split(':')[0].split(' ')[-1]
    epub_name = f"books/{novel_name}_{start_chapter}to{end_chapter}.epub"
    
    # Create the EPUB book
    book = epub.EpubBook()
    book.set_identifier(epub_name)
    book.set_title(novel_name)
    book.set_language('en')
    #book.add_author("Author Name")  # Replace with actual author name

    # Initialize table of contents and spine
    book.toc = []
    spine = ['nav']

    for i, contents in enumerate(chapter_contents):
        content = ''
        for entries in contents:
            content += f'<p style="margin-bottom: 1em;">{entries}</p>\n'

        # Construct chapter content with title
        chapter_content_with_title = f'<h1>{chapter_titles[i]}</h1>\n{content}'
        
        # Create chapter object
        chapter_file_name = f'chap_{i+1}.xhtml'
        chapter = epub.EpubHtml(
            title=chapter_titles[i],
            file_name=chapter_file_name,
            lang='en'
        )
        chapter.content = chapter_content_with_title
        
        # Add chapter to the book
        book.add_item(chapter)
        book.toc.append(chapter)
        spine.append(chapter)

    # Add NCX and navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # Define and add CSS style
    style = 'body { font-family: Times, Times New Roman, serif; }'
    nav_css = epub.EpubItem(
        uid="style_nav",
        file_name="style/nav.css",
        media_type="text/css",
        content=style
    )
    book.add_item(nav_css)
    
    # Set the spine
    book.spine = spine
    
    # Write the EPUB file
    epub.write_epub(epub_name, book)
    print(f"EPUB file created at: {epub_name}")
    return epub_name
