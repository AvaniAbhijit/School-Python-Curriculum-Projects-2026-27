# CTkTextbox creates a large text box where users can type messages or information on line 80.
# Data_entry is Textbox created in the right middle frame.

# Task 1 : Solve why Data_entry is not allowing to type text into it.



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

def encrypt():
    print("Save some text")

def decrypt():
    print("Read some text")


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

# Create a textbox where users can type or display messages
Data_entry = ctk.CTkTextbox(right_middle, width=247, height=247)

# Place the textbox inside the frame and adjust its size automatically
# Data_entry.pack(fill="both", expand=True, pady=10)

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
encrypt_img = ctk.CTkImage(Image.open("encrypt.png"), size=(25, 25))
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
    command=encrypt,
    fg_color=frame_background
)
encrypt_button.pack(side="left", padx=25)

decrypt_button = ctk.CTkButton(
    buttons_container,
    text="Decrypt",
    image=decrypt_img,
    compound="left",
    command=decrypt,
    fg_color=frame_background
)
decrypt_button.pack(side="left", padx=25)

root.mainloop()
