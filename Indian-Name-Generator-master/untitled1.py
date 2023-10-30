import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

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
    result_text.delete(1.0, tk.END)
    if generated_names:
        for i, name in enumerate(generated_names, start=1):
            result_text.insert(tk.END, f"{i}. {name}\n")
    else:
        result_text.insert(tk.END, "No names found.")


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
    result_text.delete(1.0, tk.END)
    if generated_names:
        for i, name in enumerate(generated_names, start=1):
            result_text.insert(tk.END, f"{i}. {name}\n")
    else:
        result_text.insert(tk.END, "No names found.")


# Create the main window
window = tk.Tk()
window.title("Indian Name Generator")
window.geometry("400x300")

# Create the caste selection dropdown
caste_label = ttk.Label(window, text="Select Caste:")
caste_label.pack()
caste_combobox = ttk.Combobox(window, values=["Hindu", "Muslim", "Sikh", "Christian", "Random"])
caste_combobox.pack()

# Create the starting word entry field
starting_word_label = ttk.Label(window, text="Enter Starting Word:")
starting_word_label.pack()
starting_word_entry = ttk.Entry(window)
starting_word_entry.pack()

# Create the generate button
generate_button = ttk.Button(window, text="Generate Names", command=generate_names)
generate_button.pack()

# Create the result text area with a scrollbar
result_frame = ttk.Frame(window)
result_frame.pack(fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(result_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text = tk.Text(result_frame, yscrollcommand=scrollbar.set)
result_text.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=result_text.yview)

# Start the GUI event loop
window.mainloop()
