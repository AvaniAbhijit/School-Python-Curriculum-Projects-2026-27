# PIL stands for Python Imaging Library, which is used to open, edit, and work with images in Python.

# Image.open('logo.png') opens the image file logo.png so it can be displayed or edited in the program
# CTkImage(Image.open('logo.png'), size=(120,120)) converts the image so that it can be displayed
# inside CustomTkinter Label or Button and resizes it to 120 × 120 pixels on line 35.

# In CustomTkinter, images cannot be placed directly on the window.
# So we attach the image to a CTkLabel widget, and the label displays the image on the screen.

# CTkLabel(top_frame, image=logo, text="") creates a label to display the logo
# inside top_frame, and pack() places it on the left side of the frame.

# Task : Uncomment the line 36 and Add an image to the left side of the top_frame on line 40 onwards.
#       1. Use orchids_image as the image.
#       2. Set text="" so only the image is shown.
#       3. Set fg_color to frame_background.
#       4. Use pack() to place the image on the left side of the frame.
#       5. Add padding padx=(10, 20)

import customtkinter as ctk
from PIL import Image        # A library to work with pictures

frame_background = "dimgrey"
root = ctk.CTk()
root.geometry("600x500")

root.title("Crypto Message App")

# Creating 3 frames for layout
top_frame = ctk.CTkFrame(root, fg_color=frame_background, height=80)
top_frame.pack(fill="x", pady=5)


#Loading Images
logo = ctk.CTkImage(Image.open('logo.png'), size=(120, 120))  # Open the image and set its size
#orchids_image = ctk.CTkImage(Image.open('orchids.png'), size=(100, 100))

# Create a first label with the logo image, no text, and pack it on the window.
logo_image = ctk.CTkLabel(top_frame, image=logo, text="", fg_color=frame_background)
logo_image.pack(side="left", padx=(10, 0))

# Create a second label with the logo image, no text, and pack it on the window.



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
root.mainloop()
