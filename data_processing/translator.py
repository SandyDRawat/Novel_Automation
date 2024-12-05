
import os
from dotenv import load_dotenv
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
load_dotenv()

HF_token = os.getenv('HF_TOKEN')

'''
#links_1 = link_retriever("https://novelbin.lanovels.net/book/walker-of-the-worlds/chapter-1?subsite=1")
links = link_compiler("https://www.ptwxw.com/d/809_809864/2000126/", 5)
chapter_contents, chapter_titles = compiled_scrapper(links)
'''

model = AutoModelForSeq2SeqLM.from_pretrained("Rawsand/opus-mt-zh-en-finetuned-zh-to-en")
tokenizer = AutoTokenizer.from_pretrained("Rawsand/opus-mt-zh-en-finetuned-zh-to-en")

def translate(text):
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    return [tokenizer.decode(t, skip_special_tokens=True) for t in translated]


def translate_chapters(chapters):
    translated_chapters = []
    for chapter in chapters:
        translated_content = []
        for content in chapter:
            translated_content.append(translate(content))
        translated_chapters.append(translated_content)
    return translated_chapters




