import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
from inflection import singularize
import re
import os
import random

# Import corpora of Indian last names, first names (male/female/unisex),
# and common English words that are not Indian names
script_dir = os.path.dirname(__file__)
names_last = [l.strip().title() for l in open(os.path.join(script_dir, "names.last.txt"))]
names_first_male = [l.strip().title() for l in open(os.path.join(script_dir, "names.first.male.txt"))]
names_first_female = [l.strip().title() for l in open(os.path.join(script_dir, "names.first.female.txt"))]
names_first_unisex = [l.strip().title() for l in open(os.path.join(script_dir, "names.first.unisex.txt"))]
en_words = [l.strip().title() for l in open(os.path.join(script_dir, "en_words.txt"))]

# From an array of consecutive words, create unique potential two-word names
def create_bigrams(input_list):
    bigrams = []
    for i in range(len(input_list) - 1):
        bigrams.append((input_list[i].title(), input_list[i + 1].title()))
    return list(set(bigrams))

def classify_names(input_text):
    # Remove all non-alpha/space, convert all whitespace to single space
    input_text = input_text.replace("\n", " ")
    regex = re.compile('[^a-zA-Z ]')
    input_text = re.sub('\s+', ' ', regex.sub('', input_text)).strip()

    # Remove 1-letter words (now rather than after creating bigrams accounts
    # for middle initials)
    input_text = [i for i in input_text.split() if len(i) > 1]
    input_text = ' '.join(input_text)

    # Create bigrams (potential 2-word names) from text
    bigrams = create_bigrams(input_text.split())

    # Iterate over bigrams
    # If fn/ln within corpora, add to results with score for Indianness/gender
    # Decrease Indianness score if fn/ln is an ordinary English word
    indian_names = []
    for name in bigrams:
        ln, fn_m, fn_f, fn_u = 0, 0, 0, 0
        en_word, indianness, gender = 0, 0, 0
        if name[1] in names_last:
            ln = 1
        if name[0] in names_first_male:
            fn_m = 1
        if name[0] in names_first_female:
            fn_f = 1
        if name[0] in names_first_unisex:
            fn_u = 1

        indianness = ln + fn_m + fn_f + fn_u
        gender = fn_m - fn_f

        if indianness:
            if name[0] in en_words:
                en_word += 1
            if name[1] in en_words:
                en_word += 1

            # Check depluralized word
            singular_fn, singular_ln = singularize(name[0]), singularize(name[1])
            if singular_fn != name[0] and singular_fn in en_words:
                en_word += 1
            if singular_ln != name[1] and singular_ln in en_words:
                en_word += 1

            indianness -= en_word

        if indianness > 0:
            indian_names.append(("%s %s" % name, indianness, gender))

    # Sort first by -indianness, +gender, +alpha
    indian_names = sorted(indian_names, key=lambda x: (-x[1], x[2], x[0]))

    return indian_names

def import_file(file_type):
    file_path = filedialog.askopenfilename(filetypes=[(f"{file_type.upper()} Files", f"*.{file_type}")])
    if file_path:
        with open(file_path, "r") as file:
            input_text = file.read()
            names = classify_names(input_text)
            display_names(names)

def import_url():
    url = url_entry.get()
    if url:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'})
        try:
            html = urllib.request.urlopen(req).read()
            soup = BeautifulSoup(html, 'html.parser')
            text = " ".join(soup.strings)
            names = classify_names(text)
            display_names(names)
        except urllib.error.URLError as e:
            display_names([], error=e.reason)

def display_names(names, error=None):
    result_text.delete("1.0", tk.END)
    if error:
        result_text.insert(tk.END, f"Error: {error}\n")
    else:
        for name in names:
            if name[1] > 1:
                result_text.insert(tk.END, "+ ")
            else:
                result_text.insert(tk.END, "- ")
            result_text.insert(tk.END, "%s (%d, %d)\n" % name)

def generate_names():
    caste = caste_combobox.get()
    starting_word = starting_word_entry.get().lower()  # Convert starting word to lowercase

    # Read the names from the text file based on the selected caste
    try:
        with open(f"{caste}_names.txt", "r") as file:
            names = file.read().splitlines()
    except FileNotFoundError:
        messagebox.showerror("Error", "Name list not found!")
        return

    # Filter names based on the starting word (case-insensitive)
    if starting_word:
        filtered_names = [name for name in names if name.lower().startswith(starting_word)]
    else:
        filtered_names = names

    # Generate random names
    random.shuffle(filtered_names)
    if starting_word:
        generated_names = filtered_names[:5]
    else:
        generated_names = filtered_names[:10]

    # Display the generated names with numbers
    result_text_gen.delete(1.0, tk.END)
    if generated_names:
        for i, name in enumerate(generated_names, start=1):
            result_text_gen.insert(tk.END, f"{i}. {name}\n")
    else:
        result_text_gen.insert(tk.END, "No names found.")


# Create the GUI window
window = tk.Tk()
window.title("Indian Name Recognition and Generator")
window.geometry("800x500")

# Create the notebook (tabs)
notebook = ttk.Notebook(window)
notebook.pack(fill=tk.BOTH, expand=True)

# Create the Indian Name Recognition tab
recognition_tab = ttk.Frame(notebook)
notebook.add(recognition_tab, text="Indian Name Recognition")

# Create a button to import a file
import_file_button = tk.Button(recognition_tab, text="Import File", command=lambda: import_file("txt"))
import_file_button.pack(pady=10)

# Create an entry field for entering a URL
url_label = tk.Label(recognition_tab, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(recognition_tab, width=50)
url_entry.pack(pady=5)

# Create a button to import from a URL
import_url_button = tk.Button(recognition_tab, text="Import from URL", command=import_url)
import_url_button.pack(pady=10)

# Create a text area to display the result
result_text = tk.Text(recognition_tab, width=80, height=10)
result_text.pack(pady=10)

# Create the Indian Name Generator tab
generator_tab = ttk.Frame(notebook)
notebook.add(generator_tab, text="Indian Name Generator")

# Create a label for selecting caste
caste_label = tk.Label(generator_tab, text="Select Caste:")
caste_label.pack()

# Create a combobox for selecting caste
caste_combobox = ttk.Combobox(generator_tab, values=["Brahmin", "Kshatriya", "Vaishya", "Shudra"])
caste_combobox.pack(pady=5)

# Create a label for entering starting word
starting_word_label = tk.Label(generator_tab, text="Enter Starting Word (optional):")
starting_word_label.pack()

# Create an entry field for entering starting word
starting_word_entry = tk.Entry(generator_tab)
starting_word_entry.pack(pady=5)

# Create a button to generate names
generate_names_button = tk.Button(generator_tab, text="Generate Names", command=generate_names)
generate_names_button.pack(pady=10)

# Create a text area to display the generated names
result_text_gen = tk.Text(generator_tab, width=80, height=10)
result_text_gen.pack(pady=10)

# Run the GUI event loop
window.mainloop()
