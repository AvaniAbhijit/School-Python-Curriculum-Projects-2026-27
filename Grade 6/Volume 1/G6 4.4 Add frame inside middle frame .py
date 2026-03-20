# padx means horizontal space (left and right spacing) around a widget.
# When we write two numbers in padx = (25, 5) -
#   25 pixels space on the left side
#   5 pixels space on the right side


# Task: Create a frame called right_middle inside middle_frame on line 37.
#       1. Set its fg_color to white
#       2. Pack it on the right side with
#       3. Padding padx=(5, 25) and
#       4. Fill the space using fill="both"

import customtkinter as ctk

frame_background = "dimgrey"
root = ctk.CTk()
root.geometry("600x500")

root.title("Crypto Message App")

# Creating 3 frames for layout
top_frame = ctk.CTkFrame(root, fg_color=frame_background, height=80)
top_frame.pack(fill="x", pady=5)

middle_frame = ctk.CTkFrame(root, fg_color=frame_background)
middle_frame.pack(fill="x", expand=True)

bottom_frame = ctk.CTkFrame(root, fg_color=frame_background)
bottom_frame.pack(fill="x")

# Middle frame content - split into left and right
# Below is the left_middle frame
left_middle = ctk.CTkFrame(middle_frame, fg_color="Black", width=260)
left_middle.pack(side="left", padx=(25, 5), fill="both")

#Code for right_middle frame



root.mainloop()
