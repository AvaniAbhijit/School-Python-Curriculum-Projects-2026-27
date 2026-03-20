# A Label (CTkLabel) is a widget used to display text or information on the screen.
# It is commonly used for titles, instructions, headings, or messages in a GUI application.

# Task 1 : Write code to create a label inside the right_middle frame on line 42 onwards.
#           1. Use CTkLabel to create the label.
#           2. Set the text to "Enter Secret Message".
#           3. Set the font to ("Cascadia Code SemiBold", 20, "bold").
#           4. Set the text color to "Black".
#           5. Use pack() to place the label inside the frame with padx as 20 and pady as 5.

import customtkinter as ctk

frame_background = "dimgrey"
root = ctk.CTk()
root.geometry("600x500")

root.title("Crypto Message App")

# Creating 3 frames for layout
top_frame = ctk.CTkFrame(root, fg_color=frame_background, height=80)
top_frame.pack(fill="x")

# Label inside top frame
message_label = ctk.CTkLabel(top_frame,text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), text_color="white")
message_label.pack(side="left", padx=(70,0))

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




buttons_container = ctk.CTkFrame(bottom_frame, fg_color=frame_background)
buttons_container.pack(fill="x", expand=True, pady=15)
root.mainloop()

