import tkinter as tk
import random
from PIL import Image, ImageTk

# Create window
root = tk.Tk()
root.title("Catch Me Game 😄")
root.geometry("600x400")
root.resizable(False, False)

# Load Background Image
bg_img = Image.open("Heart.jpeg")   # Your image path
bg_img = bg_img.resize((600, 450))       # Match window size
bg_photo = ImageTk.PhotoImage(bg_img)

# Create Background Label
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Keep reference
bg_label.image = bg_photo


# Function to move button
def move_button(event):
    x = random.randint(0, 520)
    y = random.randint(0, 380)
    btn2.place(x=x, y=y)

import tkinter as tk

def show_center_popup(parent, message="You clicked the button!"):

    popup = tk.Toplevel(parent)
    popup.title("Message")
    popup.resizable(False, False)

    popup_width = 300
    popup_height = 150

    # Get parent window position and size
    parent.update_idletasks()

    parent_x = parent.winfo_x()
    parent_y = parent.winfo_y()

    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    # Calculate center position
    x = parent_x + (parent_width // 2) - (popup_width // 2)
    y = parent_y + (parent_height // 2) - (popup_height // 2)

    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    # Message
    msg = tk.Label(
        popup,
        text=message,
        font=("Arial", 13, "bold")
    )
    msg.pack(pady=25)

    # Close button
    tk.Button(
        popup,
        text="Yes",
        width=10,
        command=popup.destroy
    ).pack()



#Label
title_label = tk.Label(
    root,
    text="Will you be My Valentine?",
    font=("Arial", 24, "bold"),
    fg="Black",   # You can change/remove this
)
title_label.place(x=110, y=50)

# Create Button
btn1 = tk.Button(
    root,
    text="  Yes!  ",
    font=("Arial", 12, "bold"),
    bg="White",command=lambda: show_center_popup(root, "You are Mine!")
)

btn1.place(x=200, y=150)
btn2 = tk.Button(
    root,
    text="  No!  ",
    font=("Arial", 12, "bold"),
    bg="White"
)

btn2.place(x=300, y=150)

# Bind hover
btn2.bind("<Enter>", move_button)


root.mainloop()
