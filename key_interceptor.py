import keyboard
import time
import threading
from translate import TranslatorService
from settings import Settings

class KeyInterceptor:
    def __init__(self):
        self.settings = Settings()
        self.translator = TranslatorService()
        self.last_key_time = time.time()
        self.check_interval = 0.1
        self.idle_time_limit = 1.0
        self.buffer = ''
        self.is_typing = False

        self.start_listening()

    def start_listening(self):
        keyboard.on_release(callback=self.handle_keypress)
        self.start_idle_check()

    def handle_keypress(self, event):
        self.last_key_time = time.time()
        if len(event.name) == 1:
            self.buffer += event.name
        elif event.name == 'space':
            self.buffer += ' '
        elif event.name == 'backspace' and self.buffer:
            self.buffer = self.buffer[:-1]

    def start_idle_check(self):
        def check_idle():
            while True:
                time_since_last_key = time.time() - self.last_key_time
                if time_since_last_key > self.idle_time_limit:
                    self.settings = Settings()
                    self.translate_and_replace_text()
                    self.last_key_time = time.time()
                time.sleep(self.check_interval)

        thread = threading.Thread(target=check_idle, daemon=True)
        thread.start()

    def translate_and_replace_text(self):
        if not self.buffer:
            return

        src_language = self.settings.input_language
        dest_language = self.settings.output_language

        translated_text = self.translator.translate_text(
            self.buffer,
            src_language=src_language,
            dest_language=dest_language
        )

        if dest_language == "Japanese Romanji":
            translated_text = self.translator.to_romanji(translated_text)

        for _ in range(len(self.buffer)):
            keyboard.press_and_release('backspace')
        keyboard.write(translated_text, delay=0.05)

        self.buffer = ''

if __name__ == "__main__":
    interceptor = KeyInterceptor()
