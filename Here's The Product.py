import tkinter as tk
from tkinter import messagebox

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Result: {product}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Multiplication App")
root.geometry("300x200")

# Input fields
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Button
tk.Button(root, text="Multiply", command=multiply).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run the app
root.mainloop()