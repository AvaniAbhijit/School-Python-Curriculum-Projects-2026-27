# A Label (CTkLabel) is a widget used to display text or information on the screen.
# It is commonly used for titles, instructions, headings, or messages in a GUI application.

# Task 1 : Create a label inside right_middle frame that displays on line 41 onwards:
#           1. Enter Secret Message
#           Hint:
#                   Use CTkLabel
#                   Use pack() to place it inside the frame

import customtkinter as ctk

frame_background = "dimgrey"  
root = ctk.CTk()
root.geometry("600x500")

root.title("Crypto Message App")

# Creating 3 frames for layout
top_frame = ctk.CTkFrame(root, fg_color=frame_background, height=80)
top_frame.pack(fill="x", pady=5)

# Label inside top frame
message_label = ctk.CTkLabel(top_frame,text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), text_color="white")
message_label.place(x=100, y=20)

middle_frame = ctk.CTkFrame(root, fg_color=frame_background)
middle_frame.pack(fill="x", expand=True)

bottom_frame = ctk.CTkFrame(root, fg_color=frame_background)
bottom_frame.pack(fill="x")

# Middle frame content - split into left and right
# Below is the left_middle frame
left_middle = ctk.CTkFrame(middle_frame, fg_color="Black", width=260)
left_middle.pack(side="left", padx=(25, 5), fill="both")

#Code for right_middle frame
right_middle = ctk.CTkFrame(middle_frame, fg_color="White", width=260)
right_middle.pack(side="right", padx=(5, 25), fill="both")




root.mainloop()