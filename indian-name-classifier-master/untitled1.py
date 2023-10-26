import tkinter as tk
from tkinter import ttk

def toggle_label_color():
    current_color = blinktext.cget("foreground")
    if current_color == "black":
        blinktext.config(foreground="white", background="black")
    else:
        blinktext.config(foreground="black", background="white")
    tab1.after(500, toggle_label_color)  # Toggle every 500 milliseconds (0.5 seconds)

# Create the main window
window = tk.Tk()
window.title("NLP-Named_Entity_Recognition_Inadia")
window.geometry("800x800")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(window)

# Create the first tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='File Import and Text Extraction')

# Create a frame for the buttons
button_frame = tk.Frame(tab1, borderwidth=2, relief="solid")
button_frame.pack(pady=10)

# Create a label for the frame
frame_label = tk.Label(button_frame, text="File Import Options", font=("Arial", 12, "bold"))
frame_label.pack(pady=10)

# Create a container frame for the buttons
container_frame = tk.Frame(button_frame)
container_frame.pack()

# Create buttons for file import
pdf_button = tk.Button(container_frame, text="Import PDF", command=lambda: import_file('pdf'))
pdf_button.pack(side="left", padx=10)

docx_button = tk.Button(container_frame, text="Import Word Document", command=lambda: import_file('docx'))
docx_button.pack(side="left", padx=10)

image_button = tk.Button(container_frame, text="Import Image", command=lambda: import_file('jpeg'))
image_button.pack(side="left", padx=10)

# Create a frame for the text box and process button
text_frame = tk.Frame(tab1, borderwidth=2, relief="solid")
text_frame.pack(pady=10)

blinktext = tk.Label(tab1, text="Blinking Label", font=("Arial", 18))
blinktext.pack(pady=10)

# Create a label for the frame
frame_label = tk.Label(text_frame, text="Extracted Text", font=("Arial", 12, "bold"))
frame_label.pack(pady=10)

# Create a text box to display the extracted text
text_box = tk.Text(text_frame, height=10, width=50)
text_box.pack()

# Create a button to process the text
process_button = tk.Button(tab1, text="Process Text", command=process_text)
process_button.pack(pady=10)

# Create a frame for the output text box and export button
output_frame = tk.Frame(tab1, borderwidth=2, relief="solid")
output_frame.pack(pady=10)

# Create a label for the frame
frame_label = tk.Label(output_frame, text="Processed Text", font=("Arial", 12, "bold"))
frame_label.pack(pady=10)

# Create a scrollable output text box
scrollbar = tk.Scrollbar(output_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(output_frame, height=10, width=50)
output_text.pack()

# Configure the output text box with the scrollbar
output_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=output_text.yview)

# Define the text tags for different colors
output_text.tag_configure('red', foreground='red', font=('TkDefaultFont', 10, 'bold'))
output_text.tag_configure('darkblue', foreground='darkblue', font=('TkDefaultFont', 10, 'italic'))
output_text.tag_configure('darkgoldenrod', foreground='darkgoldenrod', font=('TkDefaultFont', 10, 'italic', 'bold'))

# Bind the event to show the tooltip
output_text.bind("<Motion>", show_tooltip)

# Create a tooltip label
tooltip_label = tk.Label(tab1, text='Place your cursor',  borderwidth=1)
tooltip_label.pack()

# Create a frame for the export button
export_frame = tk.Frame(tab1)
export_frame.pack(pady=10)

# Create a button to export the data to Excel
export_button = tk.Button(export_frame, text="Export to Excel", command=export_to_excel)
export_button.pack()

# Add the first tab to the notebook
notebook.pack(fill=tk.BOTH, expand=True)

# Create the second tab
generator_tab = ttk.Frame(notebook)
notebook.add(generator_tab, text='Indian Name Generator')

# Create the caste selection dropdown
caste_label = ttk.Label(generator_tab, text="Select Caste:")
caste_label.pack()
caste_combobox = ttk.Combobox(generator_tab, values=["Hindu", "Muslim", "Sikh", "Christian", "Random"])
caste_combobox.pack()

# Create the starting word entry field
starting_word_label = ttk.Label(generator_tab, text="Enter Starting Word:")
starting_word_label.pack()
starting_word_entry = ttk.Entry(generator_tab)
starting_word_entry.pack()

# Create the generate button
generate_button = ttk.Button(generator_tab, text="Generate Names", command=generate_names)
generate_button.pack()

# Start the blinking effect
tab1.after(0, toggle_label_color)

# Start the main loop
window.mainloop()
