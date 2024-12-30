import tkinter as tk
import random

def impress_crush():
    pickup_lines = [
        "Are you French? Because Eiffel for you.",
        "Are you made of copper and tellurium? Because you're Cu-Te.",
        "Is your name Google? Because you've got everything I've been searching for.",
        "Do you believe in love at first sight, or should I walk by again?",
        "Are you a magician? Because whenever I look at you, everyone else disappears.",
        "Do you have a map?Because I keep getting lost in your eyes.",
        "Excuse me, uhm, but I think you dropped something: my jaw"
        ]
    
    pickup_line = random.choice(pickup_lines)
    label.config(text = pickup_line)
    
window = tk.Tk()
window.title("Win Their Heart<3")
window.geometry("400x300")

label = tk.Label(window, text = "Click the button for a romantic pickup line.")
label.pack(pady = 20)

button = tk.Button(window, text = "Click Me", command = impress_crush)
button.pack()

window.mainloop()