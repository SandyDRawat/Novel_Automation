from ebooklib import epub

def create_epub(chapter_contents, novel_name, start_chapter, num_chapters):
    end_chapter = start_chapter + num_chapters - 1
    epub_name = f"books/{novel_name}_{start_chapter}_to_{end_chapter}.epub"
    book = epub.EpubBook()
    book.set_identifier(epub_name)
    book.set_title(novel_name)
    book.add_author("Author Name")  # Replace with actual author name
    for i, content in enumerate(chapter_contents, start=start_chapter):
        chapter_number = i + start_chapter  # Adjusting chapter number
        chapter_content_with_number = f'<h1>Chapter {chapter_number}</h1>\n{content}'
        chapter = epub.EpubHtml(title=f'Chapter {chapter_number}', file_name=f'chapter_{chapter_number}.xhtml', lang='en')
        chapter.content = chapter_content_with_number
        book.add_item(chapter)
        book.toc.append(chapter)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    style = 'body { font-family: Times, Times New Roman, serif; }'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)
    book.spine = ['nav'] + book.toc
    epub.write_epub(epub_name, book)
