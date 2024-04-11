import tkinter as tk
from tkinter import ttk


def center_window(root, width, height):
    # Get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Find the center point
    center_x = int(screen_width / 2 - width / 2)
    center_y = int(screen_height / 2 - height / 2)

    # Set the position of the window to the center of the screen
    root.geometry(f'{width}x{height}+{center_x}+{center_y}')


root = tk.Tk()
root.title("Centered Window with Scroll View")

# Calculate 2/3 of the screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = screen_width * 2 // 3
height = screen_height * 2 // 3

# Center the window
center_window(root, width, height)

# Main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill='both', expand=True)

# Scrollable area
scroll_frame = ttk.Frame(main_frame)
scroll_frame.pack(fill='both', expand=True, pady=10)

# Create a canvas for the scrollable area
canvas = tk.Canvas(scroll_frame)
canvas.pack(side='left', fill='both', expand=True)

# Add a scrollbar to the canvas
scrollbar = ttk.Scrollbar(
    scroll_frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(
    scrollregion=canvas.bbox("all")))

# Frame inside the canvas
scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Adding example entries
for i in range(5):
    ttk.Label(scrollable_frame, text=f"Example Entry {i+1}").pack()

# Input field and send button
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill='x')

# Input field
input_field = ttk.Entry(input_frame)
input_field.pack(side='left', fill='x', expand=True, padx=(0, 10))

# Send button
send_button = ttk.Button(input_frame, text="Send")
send_button.pack(side='right')

root.mainloop()
