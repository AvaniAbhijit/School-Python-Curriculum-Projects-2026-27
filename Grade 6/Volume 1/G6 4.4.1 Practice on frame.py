# Task: Create a frame called buttons_container inside bottom_frame.
#   1. Set its background color to frame_background.
#   2. Pack the frame so it expands horizontally using fill="x".
#   3. Allow the frame to expand using expand=True.
#   4. Add vertical padding of 15 pixels using pady=15.

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

# Code for right_middle frame
right_middle = ctk.CTkFrame(middle_frame, fg_color="white")
right_middle.pack(side="left", padx=(5, 25), fill="both", expand=True)


root.mainloop()