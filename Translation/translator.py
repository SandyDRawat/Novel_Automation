from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="Rawsand/llama3.1_zhtoen_translation_v3_gguf",
	filename="unsloth.Q8_0.gguf",
)


translation_prompt = """Below is a Chinese text that needs to be translated into English.

### Chinese Text:
{}

### English Translation:
{}"""


def formatting_prompts_func_without_english(chinese_texts):
   
    texts = []
    for chinese_text in chinese_texts:
        text = translation_prompt.format(chinese_text, "") #+ EOS_TOKEN
        texts.append(text)
    return texts
    

# Function to translate text from Chinese to English
def translate(texts):
    formatted_texts = formatting_prompts_func_without_english(texts)
    predictions = []
    for text in formatted_texts:
        output = llm(text,max_tokens=512,echo=True)
        output = output['choices'][0]['text']
        prediction = output.split("Translation:\n")[1].strip()
        print(prediction)
        predictions.append(prediction)
    return predictions

# Function to translate chapters from Chinese to English
def translate_chapters(chapters):
    print(chapters[0])
    translated_chapters = []
    for chapter in chapters:
        translated_chapters.append(translate(chapter))
    return translated_chapters

# Test the translation function
if __name__ == "__main__":
    text = ["你好吗？","尤其，这是孟浩在第七命下展开的七婴图腾，威力之强，轰天撼地。"]  # Wrap in a list to match the expected input format
    print(translate(text))
