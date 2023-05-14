import tkinter as tk
import pyperclip
import keyboard
import time

# Define the sentences and their labels
sentences = {
    "ur email": "email",
    "ur email": "email",
    "ur email": "email",
    "ur email": "email",
    "ur passwords" : "password",
    "ur passwords" : "password",
    "ur passwords" : "password",
}

# Create the Tkinter root window
root = tk.Tk()
root.withdraw()
root.title("Select a email/password")

# Set the size of the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300
window_height = 300
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Create a list box to display the sentences
listbox = tk.Listbox(root, selectmode="single")
for sentence in sentences:
    listbox.insert("end", sentence)
listbox.pack()

# Set the width and height of the list box
listbox.configure(width=50, height=len(sentences))

# Create a button to copy the selected sentence to the clipboard
def copy_to_clipboard():
    selected_index = listbox.curselection()
    if selected_index:
        selected_sentence = listbox.get(selected_index)
        pyperclip.copy(selected_sentence)
        root.withdraw()
        keyboard.press_and_release('backspace')

button = tk.Button(root, text="Copy to clipboard", command=copy_to_clipboard)
button.pack()


def on_press(event):
    if event.name == "|":
        # Show the root window
        root.deiconify()

# Start the event listener
keyboard.on_press(on_press)

# Run the Tkinter event loop
root.mainloop()
