from googletrans import Translator 
translator = Translator()

def translate(text, target_language='en'):
    translator = Translator()
    try:
        # detects the language
        input_lenguage = translator.detect(text).lang
        # translate the text
        translate = translator.translate(text, src=input_lenguage, dest=target_language)

        return translate.text
    except Exception as e:
        return f"An error occurred in the translation: {e}"

text_test = 'Olá pessoa, tudo bem com vocês? Finalizando aqui o teste da API do Google para tradução automática'

lenguage_des = 'en'

translate_text = translate(text_test, lenguage_des)

print(f'Original text: {text_test}')
print(f'Language detected: {translator.detect(text_test).lang}')
print(f'Text translated to {lenguage_des}: {translate_text}')