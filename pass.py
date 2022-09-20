from tkinter import *
from random import randint

root = Tk()
root.title("Random Password Generator")
root.geometry("400x400")

# Creating random password from list of characters in ASCII (https://theasciicode.com.ar/)
my_pass = chr(randint(33,126))

# Generate random strong Password
def new_rand():

    # Clear our entry box
    pw_entry.delete(0, END)

    # Get PW Lenght and convert to integer
    pw_length = int(my_entry.get())

    # Create a variable to hold our password
    my_pass = ''

    # Loop Through password Length
    for x in range(pw_length):
        my_pass += chr(randint(33,126))

    # Output pasword to the screen
    pw_entry.insert(0,my_pass)

    # Copy to clipboard
def copy():
    # Clear the clipboard
    root.clipboard_clear()
    # Copy to clipboard
    root.clipboard_append(pw_entry.get())

# Label Frame
label = LabelFrame(root, text="Password Character Length")
label.pack(pady=20)

# Create Entry Box to desginate number of characters
my_entry = Entry(label, font=("Times New Roman", 30))
my_entry.pack(pady=20, padx=20)


# Creating the Entry Box
pw_entry = Entry(root, font=("Times New Roman", 30), bd=0, bg="grey85")
pw_entry.pack(pady=20)

# Create a frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Creating our buttons
my_button = Button(my_frame, text="Generate Random Password", command=new_rand)
my_button.grid(row=0, column=0, padx=5)


clip_button = Button(my_frame, text="Copy to clipboard", command=copy)
clip_button.grid(row=0, column=1, padx=5)

root.mainloop()
