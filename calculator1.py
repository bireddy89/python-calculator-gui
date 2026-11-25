
import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Calculator App")
root.geometry("350x400")
root.resizable(False, False)
root.configure(bg="lightblue")

# Heading
heading = tk.Label(
    root,
    text="My Calculator",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)
heading.pack(pady=15)

# First number
tk.Label(root, text="Enter First Number",
         bg="lightblue").pack()
num1 = tk.Entry(root, font=("Arial", 12))
num1.pack(pady=5)

# Second number
tk.Label(root, text="Enter Second Number",
         bg="lightblue").pack()
num2 = tk.Entry(root, font=("Arial", 12))
num2.pack(pady=5)

# Result display
result = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
result.pack(pady=15)

# Calculation function
def calculate(operation):
    try:
        a = float(num1.get())
        b = float(num2.get())

        if operation == "+":
            answer = a + b

        elif operation == "-":
            answer = a - b

        elif operation == "*":
            answer = a * b

        elif operation == "/":
            if b == 0:
                messagebox.showerror(
                    "Error",
                    "Cannot divide by zero!"
                )
                return
            answer = a / b

        result.config(text="Result: " + str(answer))

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers!"
        )

# Operation buttons
tk.Button(root, text="Addition (+)",
          width=20, command=lambda: calculate("+")).pack(pady=5)

tk.Button(root, text="Subtraction (-)",
          width=20, command=lambda: calculate("-")).pack(pady=5)

tk.Button(root, text="Multiplication (*)",
          width=20, command=lambda: calculate("*")).pack(pady=5)

tk.Button(root, text="Division (/)",
          width=20, command=lambda: calculate("/")).pack(pady=5)

# Start application
root.mainloop()
