#  A button is a clickable element that performs an action when the user clicks it.
#  CTkButton() → Creates a button in CustomTkinter and takes below parameters.
#   1. buttons_container → The frame where the button will appear.
#   2. text="Button1" → The text shown on the button.
#   3. fg_color=frame_background → Sets the background color of the button.


# Task : Create encrypt_button and decrypt_button inside buttons_container using 
#        the same properties and place them next to Button1
#        using pack(side="left", padx=25) in the line.

import customtkinter as ctk
from PIL import Image, ImageTk  # A library to work with pictures

frame_background = "dimgrey"  
root = ctk.CTk()
root.geometry("600x500")

root.title("Crypto Message App")

# Creating 3 frames for layout
top_frame = ctk.CTkFrame(root, fg_color=frame_background, height=80)
top_frame.pack(fill="x", pady=5)


#Loading Images    
logo = ctk.CTkImage(Image.open('logo.png'), size=(120, 120))  # Open the image and set its size
orchids_image = ctk.CTkImage(Image.open('orchids.png'), size=(100, 100))

# Create a first label with the logo image, no text, and pack it on the window.
logo_image = ctk.CTkLabel(top_frame, image=logo, text="", fg_color=frame_background)
logo_image.pack(side="left", padx=(10, 0))

# Create a second label with the logo image, no text, and pack it on the window.
logo_orchids_image = ctk.CTkLabel(top_frame, image=orchids_image, text="", fg_color=frame_background)
logo_orchids_image.pack(side="right", padx=(10, 0))

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

# Label inside top frame
message_label1 = ctk.CTkLabel(right_middle,text="Enter Secret Message", font=("Cascadia Code SemiBold", 20, "bold"), text_color="Black")
message_label1.pack(fill="x", pady=5)

buttons_container = ctk.CTkFrame(bottom_frame, fg_color=frame_background)
buttons_container.pack(fill="x", expand=True, pady=15)


# Bottom frame button-1 - open_button
open_button  = ctk.CTkButton(buttons_container, text="Button1", fg_color=frame_background)
open_button.pack(side="left",padx = 25)  

# Bottom frame button-2 encrypt_button


# Bottom frame button-3 decrypt_button


root.mainloop()