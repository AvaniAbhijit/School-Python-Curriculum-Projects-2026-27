# ctk.CTkFrame - A frame is like a container or box used to group widgets
#                (buttons, labels, etc.) together inside a window.
# pack() - Is used to place a widget inside the window or frame.
#          It automatically arranges widgets one after another.
# fill - fill decides how the widget expands inside the available space.
#           fill="x" → expands horizontally
#           fill="y" → expands vertically
#           fill="both" → expands in both directions
# padx - padx adds horizontal space (left and right side spacing) around a widget.
# pady - pady adds vertical space (top and bottom spacing) around a widget.

# Task1: Create the middle frame
# Hint: Use CTkFrame with fg_color as background
# Hint: Use pack() with fill="both" and expand=True so it stretches and grows.

# Task2:Create the bottom frame
# Hint: Set height=100 when creating the frame
# Hint: Use pack() with fill="x" so it stretches across the bottom

import customtkinter as ctk

frame_background = "dimgrey"  # Stores the color name 'dimgrey' to be used as the background color for frames
root = ctk.CTk()
root.geometry("600x500")

root.title("Crypto Message App")

# Create top_frame for layout
top_frame = ctk.CTkFrame(root, fg_color=frame_background, height=80)
top_frame.pack(fill="x", pady=5)

#Create middle_frame here for layout


#Create bottom_frame here for layout


root.mainloop()