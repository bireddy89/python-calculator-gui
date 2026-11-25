
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Input fields
tk.Label(root, text="First Number").pack()
num1 = tk.Entry(root)
num1.pack()

tk.Label(root, text="Second Number").pack()
num2 = tk.Entry(root)
num2.pack()

# Result label
result = tk.Label(root, text="Result: ", font=("Arial", 14))
result.pack(pady=10)

# Addition function
def addition():
    a = float(num1.get())
    b = float(num2.get())
    result.config(text="Result: " + str(a + b))

# Subtraction function
def subtraction():
    a = float(num1.get())
    b = float(num2.get())
    result.config(text="Result: " + str(a - b))

# Buttons
tk.Button(root, text="Addition (+)", command=addition).pack(pady=5)
tk.Button(root, text="Subtraction (-)", command=subtraction).pack(pady=5)

# Run application
root.mainloop()
