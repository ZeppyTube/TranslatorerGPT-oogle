import json
import os
import sys

class Settings:
    def __init__(self):
        self.settings_file = self.resource_path('settings.json')
        self.languages = [
            "Arabic", "Bengali", "Chinese Simplified", "Chinese Traditional", "Dutch",
            "English", "Estonian", "French", "German", "Gujarati", "Hebrew",
            "Hindi", "Indonesian", "Italian", "Japanese", "Japanese Romanji",
            "Kannada", "Korean", "Malay", "Marathi", "Norwegian", "Polish",
            "Portuguese", "Punjabi", "Russian", "Spanish", "Tamil", "Telugu",
            "Thai", "Turkish", "Urdu", "Vietnamese", "Welsh"
        ]
        self.default_input_language = "English"
        self.default_output_language = "English"

        self.input_language = self.default_input_language
        self.output_language = self.default_output_language

        self.load_settings()

    def resource_path(self, relative_path):
        """ Get the absolute path to the resource, works for dev and PyInstaller """
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def load_settings(self):
        try:
            with open(self.settings_file, 'r') as file:
                settings = json.load(file)
                self.input_language = settings.get('input_language', self.default_input_language)
                self.output_language = settings.get('output_language', self.default_output_language)
        except FileNotFoundError:
            self.save_settings()

    def save_settings(self):
        settings = {
            'input_language': self.input_language,
            'output_language': self.output_language,
        }
        with open(self.settings_file, 'w') as file:
            json.dump(settings, file)

        self.load_settings()
