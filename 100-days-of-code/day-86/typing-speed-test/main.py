import tkinter as tk
from tkinter import ttk

TITLE_FONT = ("Arial", 16, "bold")
SUBTITLE_FONT = ("Arial", 12)
SCORE_FONT = ("Arial", 10)
WORDS_FONT = ("Arial", 12)
INPUT_FONT = ("Arial", 12)

# Creazione della finestra principale
root = tk.Tk()
root.title("Typing speed test")
root.geometry("800x600")

# Title
title_label = tk.Label(root, text="Title", font=TITLE_FONT)
title_label.pack(pady=10)

# Subtitle
subtitle_label = tk.Label(root, text="Subtitle", font=SUBTITLE_FONT)
subtitle_label.pack()

# Score
score_label = tk.Label(root, text="Score: 0", font=SCORE_FONT)
score_label.pack(pady=5)

# words frame
words_frame = tk.Frame(root, relief=tk.SUNKEN, borderwidth=2, width=500, height=300)
words_frame.pack_propagate(False)
words_frame.pack(pady=10, padx=20)

# words
words_label = tk.Label(words_frame, text="Parola 1, Parola 2, Parola 3", font=WORDS_FONT)
words_label.pack(pady=10)

# input
entry = tk.Entry(root, font=INPUT_FONT)
entry.pack(pady=10)

root.mainloop()
