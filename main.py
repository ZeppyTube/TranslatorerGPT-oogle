from gui import TranslatorGUI
from key_interceptor import KeyInterceptor
import tkinter as tk
from settings import Settings

def on_close(root):
    root.quit()

def run_app():
    root = tk.Tk()
    settings = Settings()
    interceptor = KeyInterceptor()
    gui = TranslatorGUI(root, interceptor)

    root.protocol("WM_DELETE_WINDOW", lambda: on_close(root))

    root.mainloop()

if __name__ == "__main__":
    run_app()
