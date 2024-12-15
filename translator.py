import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

# Initialize Translator
translator = Translator()

# Language dictionary
language = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    "la": "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish"
}

# GUI Application
class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Title Label
        title_label = tk.Label(self.root, text="Language Translator", font=("Helvetica", 16, "bold"), fg="#1a1a1a")
        title_label.pack(pady=10)

        # Input Text
        input_label = tk.Label(self.root, text="Enter Text to Translate:", font=("Helvetica", 12))
        input_label.pack(pady=5)
        self.input_text = tk.Text(self.root, wrap=tk.WORD, height=5, width=60, font=("Helvetica", 10))
        self.input_text.pack(pady=5)

        # Language Selection Dropdowns
        self.src_lang = tk.StringVar()
        self.src_lang.set("en")  # Default source language: English
        self.dest_lang = tk.StringVar()
        self.dest_lang.set("es")  # Default target language: Spanish

        lang_label = tk.Label(self.root, text="Select Source and Target Language:", font=("Helvetica", 12))
        lang_label.pack(pady=5)

        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        src_lang_menu = ttk.Combobox(frame, textvariable=self.src_lang, values=list(language.keys()), width=20, state="readonly")
        src_lang_menu.grid(row=0, column=0, padx=5)
        src_lang_menu.set("en")

        dest_lang_menu = ttk.Combobox(frame, textvariable=self.dest_lang, values=list(language.keys()), width=20, state="readonly")
        dest_lang_menu.grid(row=0, column=1, padx=5)
        dest_lang_menu.set("es")

        # Translate Button
        translate_btn = tk.Button(self.root, text="Translate", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=self.translate_text)
        translate_btn.pack(pady=10)

        # Output Section
        output_label = tk.Label(self.root, text="Translated Text:", font=("Helvetica", 12))
        output_label.pack(pady=5)
        self.output_text = tk.Text(self.root, wrap=tk.WORD, height=5, width=60, font=("Helvetica", 10), bg="#f9f9f9")
        self.output_text.pack(pady=5)
        self.output_text.config(state=tk.DISABLED)

    def translate_text(self):
        source_text = self.input_text.get("1.0", tk.END).strip()
        src_lang = self.src_lang.get()
        dest_lang = self.dest_lang.get()

        if not source_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        try:
            # Translate using googletrans
            translated = translator.translate(source_text, src=src_lang, dest=dest_lang)
            translated_text = translated.text
            pronunciation = translated.pronunciation or "N/A"

            # Display Translated Text
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Translated Text: {translated_text}\n")
            self.output_text.insert(tk.END, f"Pronunciation: {pronunciation}\n")
            self.output_text.insert(tk.END, f"Translated From: {language.get(translated.src, 'Unknown')}\n")
            self.output_text.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Translation Error", f"Error occurred: {e}")

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
