import tkinter as tk
from tkinter import messagebox
import pygame
import time

pygame.mixer.init()

def play_audio(binary_pin):
    duration_1 = 4.0
    duration_0 = 5

    for bit in binary_pin:
        if bit == '1':
            # Load and play audio file for 1
            pygame.mixer.music.load('sweet-kitty-meow.wav')
            pygame.mixer.music.play()
            time.sleep(duration_1)
            print(bit + " ")
        elif bit == '0':
            # Load and play audio file for 0
            pygame.mixer.music.load('sweet-kitty-meow.wav')
            pygame.mixer.music.play()
            time.sleep(duration_0)
            print(bit + " ")
    pygame.mixer.music.load('sweet-kitty-meow.wav')
    pygame.mixer.music.play()

def convert_to_binary(pin):
    # Convert pin to binary
    binary_pin = ''.join(format(int(digit), '04b') for digit in pin)
    return binary_pin
def confirm_pin():
    # Get pin from entry widget
    pin = pinBox.get()

    if len(pin) != 4 or not pin.isdigit():
        messagebox.showerror("Error", "Please enter a 4-digit numeric PIN.")
        return

    binary_pin = convert_to_binary(pin)

    pin_label = tk.Label(printPinsFrame, text=f"PIN: {pin}  |  Binary: {binary_pin}", font=("Arial", 12), fg="white", bg="black", padx=10, pady=5)
    pin_label.grid(row=2, column=0, sticky="w")
    play_audio(binary_pin)


root = tk.Tk()
root.title("Secret Notes with Miaou")
root.geometry("600x300")
root.config(bg="grey")

secretNotes = tk.Label(root, text="Secret Notes", fg="white", bg="black", font=('Arial bold', 18))
secretNotes.pack(padx=10)

root.rowconfigure(0, weight=0)
root.rowconfigure((1, 2), weight=1)

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)

secretNotes.grid(row = 0, columnspan = 2, sticky='we')

pinFrame = tk.Frame(root, bg="black")
pinFrame.grid(row = 1, columnspan = 2)

textLabel = tk.Label(pinFrame, text="Enter 4 digit PIN:", font=("Arial", 12), fg="white", bg="black")
textLabel.grid(row=1, column=0, padx=10, pady=10)

pinBox = tk.Entry(pinFrame, show="*", font=("Arial", 16))
pinBox.grid(row=1, column=1, padx=10, pady=10)

confirm_button = tk.Button(pinFrame, text="Confirm", font=("Arial", 12), bg="grey", fg="white", command=confirm_pin)
confirm_button.grid(row=1, column=2, padx=10, pady=10)

printPinsFrame = tk.Frame(root, bg="black")
printPinsFrame.grid(row = 2, columnspan=2)

root.mainloop()