# A function is a block of code that does a specific task whenever we call it.
# def open_image() function we used here for opening the image when button get clicked.
# filedialog is a special tool in Python that opens a window so the user can choose a file from the computer.

# Task 1: Declare encrypt() and decrypt() function, print some msg inside the functions on line 42 and 45.
# Task 2: Call encrypt function on line 125 and decrypt function on line 135.



import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog


frame_background = "dimgrey"
root = ctk.CTk()
root.geometry("600x500")

root.title("Crypto Message App")

file_types = [("PNG files", "*.png")]
file_path=""
def open_image():

    global file_path

    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=file_types
    )

    if file_path:
        image = Image.open(file_path)

        image = image.resize((240, 240))

        label_image = ImageTk.PhotoImage(image)

        PhotoLabel.configure(image=label_image)

        PhotoLabel.image = label_image





top_frame = ctk.CTkFrame(root, fg_color=frame_background, height=80)
top_frame.pack(fill="x", pady=5)

logo = ctk.CTkImage(Image.open('logo.png'), size=(120, 120))
orchids_image = ctk.CTkImage(Image.open('orchids.png'), size=(100, 100))

logo_image = ctk.CTkLabel(top_frame, image=logo, text="", fg_color=frame_background)
logo_image.pack(side="left", padx=(10, 0))

logo_orchids_image = ctk.CTkLabel(top_frame, image=orchids_image, text="", fg_color=frame_background)
logo_orchids_image.pack(side="right", padx=(10, 0))

message_label = ctk.CTkLabel(
    top_frame,
    text="Message Encrypter",
    font=("Cascadia Code SemiBold", 20, "bold"),
    text_color="white"
)
message_label.pack(side="left", padx=(70,0))

middle_frame = ctk.CTkFrame(root, fg_color=frame_background)
middle_frame.pack(fill="x", expand=True)

bottom_frame = ctk.CTkFrame(root, fg_color=frame_background)
bottom_frame.pack(fill="x")

left_middle = ctk.CTkFrame(middle_frame, fg_color="Black", width=260)
left_middle.pack(side="left", padx=(25, 5), fill="both")

right_middle = ctk.CTkFrame(middle_frame, fg_color="White", width=260)
right_middle.pack(side="right", padx=(5, 25), fill="both")

message_label1 = ctk.CTkLabel(
    right_middle,
    text="Enter Secret Message",
    font=("Cascadia Code SemiBold", 20, "bold"),
    text_color="Black"
)
message_label1.pack(fill="x", pady=5)

sender = Image.open('cryptopic.jpg')

sender = sender.resize((240, 240))

label_image = ImageTk.PhotoImage(sender)

PhotoLabel = ctk.CTkLabel(
    left_middle,
    image=label_image,
    text="",
    width=247,
    height=247,
    fg_color="white"
)
PhotoLabel.pack(pady=10)

buttons_container = ctk.CTkFrame(bottom_frame, fg_color=frame_background)
buttons_container.pack(fill="x", expand=True, pady=15)

open_img = ctk.CTkImage(Image.open("open_file.png"), size=(25, 25))
encrypt_img = ctk.CTkImage(Image.open("encryption.png"), size=(25, 25))
decrypt_img = ctk.CTkImage(Image.open("decrypt.png"), size=(25, 25))

open_button = ctk.CTkButton(
    buttons_container,
    text="Open",
    image=open_img,
    compound="left",
    command=open_image,
    fg_color=frame_background
)
open_button.pack(side="left", padx=25)

encrypt_button = ctk.CTkButton(
    buttons_container,
    text="Encrypt",
    image=encrypt_img,
    compound="left",

    fg_color=frame_background
)
encrypt_button.pack(side="left", padx=25)

decrypt_button = ctk.CTkButton(
    buttons_container,
    text="Decrypt",
    image=decrypt_img,
    compound="left",

    fg_color=frame_background
)
decrypt_button.pack(side="left", padx=25)

root.mainloop()
