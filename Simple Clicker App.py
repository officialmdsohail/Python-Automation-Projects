import tkinter as tk

count = 0

def click():
    global count
    count += 1
    label.config(text=f"Clicks: {count}")

root = tk.Tk()
root.title("Click Counter")

label = tk.Label(root, text="Clicks: 0", font=("Arial", 20))
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=click)
button.pack()

root.mainloop()