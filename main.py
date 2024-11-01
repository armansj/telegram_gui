import tkinter as tk

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': ' / '
}

def text_to_morse(text):
    morse_code = ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)
    return morse_code

def on_convert():
    text = entry.get()
    morse_code = text_to_morse(text)
    result_label.config(text=morse_code)

root = tk.Tk()
root.title("Text to Morse Code Converter")

entry_label = tk.Label(root, text="Enter text:")
entry_label.pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert to Morse Code", command=on_convert)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Courier", 14), wraplength=400, justify="left")
result_label.pack(pady=10)

root.mainloop()
