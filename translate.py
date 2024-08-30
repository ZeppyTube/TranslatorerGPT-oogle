import json
import os
import sys

class TranslatorService:
    def __init__(self):
        from googletrans import Translator
        self.translator = Translator()
        self.romanji_mapping = self.load_romanji_mapping()

    def load_romanji_mapping(self):
        """Load Romanji mappings from an external JSON file."""
        path = self.resource_path('romanji.json')
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def resource_path(self, relative_path):
        """ Get the absolute path to the resource, works for dev and PyInstaller """
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def translate_text(self, text, src_language, dest_language):
        try:
            if dest_language == "Japanese Romanji":
                translated_text = self.translator.translate(text, src=src_language, dest='ja').text
                return self.to_romanji(translated_text)
            elif dest_language == "Chinese Simplified":
                dest_language = 'zh-CN'
            elif dest_language == "Chinese Traditional":
                dest_language = 'zh-TW'

            translation = self.translator.translate(text, src=src_language, dest=dest_language)
            if translation and translation.text:
                return translation.text
            else:
                return text
        except Exception as e:
            print(f"Translation error: {e}")
            return text

    def to_romanji(self, text):
        romanji_text = []
        skip_next = False

        for i, char in enumerate(text):
            if skip_next:
                skip_next = False
                continue

            if i < len(text) - 1:
                two_char_combination = text[i:i+2]
                if two_char_combination in self.romanji_mapping:
                    romanji_text.append(self.romanji_mapping[two_char_combination])
                    skip_next = True
                    continue

            romanji_text.append(self.romanji_mapping.get(char, char))

        return ''.join(romanji_text)
