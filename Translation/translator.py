
import os
from dotenv import load_dotenv
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
load_dotenv()

HF_token = os.getenv('HF_TOKEN')

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



if __name__ == "__main__":
    text = "你好吗？"
    print(translate(text))
