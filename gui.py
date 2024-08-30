import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
import requests
from settings import Settings

class TranslatorGUI:
    def __init__(self, master, interceptor):
        self.master = master
        self.master.title("TranslatorerGPT-oogle")
        self.settings = Settings()
        self.interceptor = interceptor
        self.dark_mode = False

        if not self.check_internet_connection():
            self.show_internet_warning()

        icon_path = self.resource_path('icon.ico')
        self.master.iconbitmap(icon_path)

        self.style = ttk.Style()

        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=2)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)

        self.input_label = tk.Label(master, text="Input Language")
        self.input_label.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        self.input_lang = ttk.Combobox(master, values=self.settings.languages, state='readonly')
        self.input_lang.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
        self.input_lang.current(self.settings.languages.index(self.settings.input_language))

        self.output_label = tk.Label(master, text="Output Language")
        self.output_label.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        self.output_lang = ttk.Combobox(master, values=self.settings.languages, state='readonly')
        self.output_lang.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
        self.output_lang.current(self.settings.languages.index(self.settings.output_language))

        self.dark_mode_button = tk.Button(master, text="Toggle Dark Mode", command=self.toggle_dark_mode)
        self.dark_mode_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        self.how_to_use_button = tk.Button(master, text="How to Use", command=self.show_how_to_use)
        self.how_to_use_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        self.save_button = tk.Button(master, text="Save", command=self.save_settings)
        self.save_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        self.set_light_mode()

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.set_dark_mode()
        else:
            self.set_light_mode()

    def set_dark_mode(self):
        self.master.configure(bg='#2c2f33')
        self.input_label.configure(bg='#2c2f33', fg='#ffffff')
        self.output_label.configure(bg='#2c2f33', fg='#ffffff')

        self.dark_mode_button.configure(bg='#7289da', fg='#ffffff', activebackground='#7289da', activeforeground='#ffffff')
        self.how_to_use_button.configure(bg='#7289da', fg='#ffffff', activebackground='#7289da', activeforeground='#ffffff')
        self.save_button.configure(bg='#f0f0f0', fg='#000000')

    def set_light_mode(self):
        self.master.configure(bg='#f0f0f0')
        self.input_label.configure(bg='#f0f0f0', fg='#000000')
        self.output_label.configure(bg='#f0f0f0', fg='#000000')

        self.dark_mode_button.configure(bg='#f0f0f0', fg='#000000', activebackground='#f0f0f0', activeforeground='#000000')
        self.how_to_use_button.configure(bg='#f0f0f0', fg='#000000', activebackground='#f0f0f0', activeforeground='#000000')
        self.save_button.configure(bg='#f0f0f0', fg='#000000')

    def show_internet_warning(self):
        messagebox.showwarning("No Internet", "!WARNING! No internet detected, please check your internet connection and restart the app when you have internet !WARNING!")

    def show_how_to_use(self):
        self.clear_window()
        instructions = tk.Label(self.master, text="Put in your input language if you don't speak English, then output language for what you want it to translate to, then it'll record you typing, and when your not typing for a full second it'll replace your text with the translated text.", wraplength=400, justify="center")
        instructions.grid(row=0, column=0, padx=20, pady=20)
        back_button = tk.Button(self.master, text="Back", command=self.show_main_menu)
        back_button.grid(row=1, column=0, pady=10)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_window()
        self.__init__(self.master, self.interceptor)

    def save_settings(self):
        self.settings.input_language = self.input_lang.get()
        self.settings.output_language = self.output_lang.get()
        self.settings.save_settings()

    def check_internet_connection(self):
        try:
            requests.get('https://www.google.com/', timeout=3)
            return True
        except requests.ConnectionError:
            return False

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    root = tk.Tk()
    gui = TranslatorGUI(root, None)
    root.mainloop()
