
from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox
from captcha.image import ImageCaptcha

# Create ImageCaptcha instance with fonts
image = ImageCaptcha(fonts=[
    'E:/Python/Python_Projects/Captcha_Generator/fonts/ChelseaMarketsr.ttf',
    'E:/Python/Python_Projects/Captcha_Generator/fonts/DejaVuSanssr.ttf'
])

# Generate random number
random_text = str(randint(100000, 999999))
image.write(random_text, 'out.png')

# Function to verify captcha input
def verify():
    global random_text
    user_input = t1.get("1.0", END).strip()  # Get text and remove extra spaces/newlines
    if user_input == random_text:
        messagebox.showinfo("Success", "Verified")
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()

# Function to refresh the captcha
def refresh():
    global random_text, photo
    random_text = str(randint(100000, 999999))
    image.write(random_text, 'out.png')

    # Update Label Image
    photo = PhotoImage(file="out.png")  # Create a new instance to avoid garbage collection
    l1.config(image=photo)
    l1.image = photo  # Keep a reference to avoid being garbage collected

# Tkinter GUI Setup
root = Tk()
root.title("Captcha Verification")

# Load initial captcha image
photo = PhotoImage(file="out.png")
l1 = Label(root, image=photo, height=100, width=200)
t1 = Text(root, height=2, width=20)

# Buttons
b1 = Button(root, text="Submit", command=verify)
b2 = Button(root, text="Refresh", command=refresh)

# Layout
l1.pack(pady=10)
t1.pack(pady=5)
b1.pack(pady=5)
b2.pack(pady=5)

root.mainloop()
