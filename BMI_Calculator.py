import tkinter as tk
from tkinter import messagebox


def classify(bmi):
    if bmi <= 16:
        return "Severely under-weight", "#B91C1C"
    elif bmi <= 18.5:
        return "Under-weight", "#D97706"
    elif bmi <= 25:
        return "Healthy", "#15803D"
    elif bmi <= 30:
        return "Overweight", "#D97706"
    else:
        return "Severely overweight", "#B91C1C"


def calculate(event=None):
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
        return

    if height <= 0 or weight <= 0:
        messagebox.showerror("Invalid input", "Height and weight must be greater than zero.")
        return

    height_m = height / 100
    bmi = weight / (height_m * height_m)
    label, color = classify(bmi)

    bmi_label.config(text=f"Your BMI: {bmi:.2f}")
    category_label.config(text=label, fg=color)


def clear():
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    bmi_label.config(text="")
    category_label.config(text="")
    height_entry.focus()


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("340x330")
root.resizable(False, False)
root.configure(bg="white")

tk.Label(root, text="BMI Calculator", font=("Segoe UI", 18, "bold"),
         bg="white", fg="#1D4ED8").pack(pady=(20, 10))

tk.Label(root, text="Height (cm)", font=("Segoe UI", 11), bg="white").pack()
height_entry = tk.Entry(root, font=("Segoe UI", 12), justify="center", width=18)
height_entry.pack(pady=(2, 10))

tk.Label(root, text="Weight (kg)", font=("Segoe UI", 11), bg="white").pack()
weight_entry = tk.Entry(root, font=("Segoe UI", 12), justify="center", width=18)
weight_entry.pack(pady=(2, 14))

buttons = tk.Frame(root, bg="white")
buttons.pack()
tk.Button(buttons, text="Calculate", command=calculate, font=("Segoe UI", 11, "bold"),
          bg="#2563EB", fg="white", relief="flat", padx=14, pady=4).grid(row=0, column=0, padx=5)
tk.Button(buttons, text="Clear", command=clear, font=("Segoe UI", 11),
          relief="flat", padx=14, pady=4).grid(row=0, column=1, padx=5)

bmi_label = tk.Label(root, text="", font=("Segoe UI", 14, "bold"), bg="white")
bmi_label.pack(pady=(18, 2))
category_label = tk.Label(root, text="", font=("Segoe UI", 13), bg="white")
category_label.pack()

root.bind("<Return>", calculate)
height_entry.focus()
root.mainloop()