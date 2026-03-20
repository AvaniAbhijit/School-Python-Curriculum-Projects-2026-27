# PhotoImage() on line 73 – Converts the image into a format that Tkinter/CustomTkinter can display on the screen.
# This is used as this image will be replaced with any other image of the user's choice.

# On line 75, used CTKImage() to create an image for the open_button with size (70,70).
# On line 85 this image can be made to appear on a button using the image attribute.
# Note: The text attribute has been made empty.

# Task:
# Add images to other 2 buttons inside the bottom_frame.
# 1. Load two images using CTkImage (example: encrypt.png, decrypt.png) like open_file.
# 2. Set the size of each image to (70, 70).
# 3. Add one image to each button - encrypt_button and decrypt_button like done for open_button.
# 4. Make the button text empty along with the image.



import customtkinter as ctk
from PIL import Image, ImageTk

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

# Create a second label with the logo image, no text, and pack it on the window.C
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

# Open the image file named 'cryptopic.jpg'
sender = Image.open('cryptopic.jpg')

# Resize the image to 240x240 pixels
sender = sender.resize((240, 240))

# Convert the image into a format that Tkinter/CustomTkinter can display
label_image = ImageTk.PhotoImage(sender)

open_file = ctk.CTkImage(Image.open('open_file.png'), size=(70, 70))

# Create a photolabel with the cryptopic image, no text, and pack it on the window.
PhotoLabel = ctk.CTkLabel(left_middle, image=label_image, text="", width=247, height=247, fg_color="white")
PhotoLabel.pack(pady=10)

buttons_container = ctk.CTkFrame(bottom_frame, fg_color=frame_background)
buttons_container.pack(fill="x", expand=True, pady=15)

# Bottom frame button-1 - open_button
open_button  = ctk.CTkButton(buttons_container, image=open_file, text="", fg_color=frame_background)
open_button.pack(side="left",padx = 25)

# Bottom frame button-2 encrypt_button
encrypt_button = ctk.CTkButton(buttons_container, text="Button2", fg_color=frame_background)
encrypt_button.pack(side="left",padx = 25)

# Bottom frame button-3 decrypt_button
decrypt_button = ctk.CTkButton(buttons_container, text="Button3", fg_color=frame_background)
decrypt_button.pack(side="left",padx = 25)

root.mainloop()
