import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def submit_ticket():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    source = combo_source.get()
    destination = combo_destination.get()
    date = date_entry.get()
    travel_class = combo_class.get()
    ticket_type = ticket_type_var.get()
    id_number = entry_id.get()
    payment_mode = payment_var.get()

    if not name or not age or not source or not destination or not date:
        messagebox.showerror("Error", "Please fill all required fields.")
        return

    if ticket_type == "Tatkal" and not id_number:
        messagebox.showerror("Error", "ID number is required for Tatkal.")
        return

    try:
        int(age)
    except ValueError:
        messagebox.showerror("Error", "Age must be a number.")
        return

    summary = f"""
    🎫 Ticket Booked Successfully!

    Passenger Name : {name}
    Age            : {age}
    Gender         : {gender}
    From           : {source}
    To             : {destination}
    Date           : {date}
    Class          : {travel_class}
    Ticket Type    : {ticket_type}
    Payment Mode   : {payment_mode}
    """

    if ticket_type == "Tatkal":
        summary += f"ID Number      : {id_number}\n"

    messagebox.showinfo("Booking Confirmation", summary)

def reset_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set("")
    combo_source.set("")
    combo_destination.set("")
    combo_class.set("")
    ticket_type_var.set("Normal")
    entry_id.delete(0, tk.END)
    entry_id.config(state=tk.DISABLED)
    payment_var.set("")

def toggle_id_entry(*args):
    if ticket_type_var.get() == "Tatkal":
        entry_id.config(state=tk.NORMAL)
    else:
        entry_id.delete(0, tk.END)
        entry_id.config(state=tk.DISABLED)

# ----------------- GUI SETUP ----------------- #

root = tk.Tk()
root.title("Railway Ticket Booking")
root.geometry("480x720")
root.configure(bg="#f0f4f7")

tk.Label(root, text="🚆 Railway Ticket Booking", font=("Arial", 16, "bold"), bg="#f0f4f7", fg="#003366").pack(pady=10)

# Passenger Name
tk.Label(root, text="Passenger Name:", bg="#f0f4f7").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack()

# Age
tk.Label(root, text="Age:", bg="#f0f4f7").pack(pady=(10, 0))
entry_age = tk.Entry(root, width=10)
entry_age.pack()

# Gender
tk.Label(root, text="Gender:", bg="#f0f4f7").pack(pady=(10, 0))
gender_var = tk.StringVar()
frame_gender = tk.Frame(root, bg="#f0f4f7")
frame_gender.pack()
tk.Radiobutton(frame_gender, text="Male", variable=gender_var, value="Male", bg="#f0f4f7").pack(side=tk.LEFT)
tk.Radiobutton(frame_gender, text="Female", variable=gender_var, value="Female", bg="#f0f4f7").pack(side=tk.LEFT)
tk.Radiobutton(frame_gender, text="Other", variable=gender_var, value="Other", bg="#f0f4f7").pack(side=tk.LEFT)

# Source Station
tk.Label(root, text="From (Source):", bg="#f0f4f7").pack(pady=(10, 0))
combo_source = ttk.Combobox(root, values=["Delhi", "Mumbai", "Chennai", "Kolkata", "Bengaluru"])
combo_source.pack()

# Destination Station
tk.Label(root, text="To (Destination):", bg="#f0f4f7").pack(pady=(10, 0))
combo_destination = ttk.Combobox(root, values=["Delhi", "Mumbai", "Chennai", "Kolkata", "Bengaluru"])
combo_destination.pack()

# Date Picker
tk.Label(root, text="Date of Journey:", bg="#f0f4f7").pack(pady=(10, 0))
date_entry = DateEntry(root, date_pattern="dd/mm/yyyy", width=18)
date_entry.pack()

# Class
tk.Label(root, text="Class:", bg="#f0f4f7").pack(pady=(10, 0))
combo_class = ttk.Combobox(root, values=["Sleeper", "AC 3 Tier", "AC 2 Tier", "First Class", "General"])
combo_class.pack()

# Ticket Type
tk.Label(root, text="Ticket Type:", bg="#f0f4f7").pack(pady=(10, 0))
ticket_type_var = tk.StringVar(value="Normal")
frame_type = tk.Frame(root, bg="#f0f4f7")
frame_type.pack()
tk.Radiobutton(frame_type, text="Normal", variable=ticket_type_var, value="Normal", bg="#f0f4f7").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_type, text="Tatkal", variable=ticket_type_var, value="Tatkal", bg="#f0f4f7").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_type, text="Local", variable=ticket_type_var, value="Local", bg="#f0f4f7").pack(side=tk.LEFT, padx=10)

# ID Number for Tatkal
tk.Label(root, text="ID Number (Tatkal only):", bg="#f0f4f7").pack(pady=(10, 0))
entry_id = tk.Entry(root, width=30, state=tk.DISABLED)
entry_id.pack()
ticket_type_var.trace_add("write", toggle_id_entry)

# Payment Mode
tk.Label(root, text="Payment Mode:", bg="#f0f4f7").pack(pady=(10, 0))
payment_var = tk.StringVar()
combo_payment = ttk.Combobox(root, textvariable=payment_var, values=["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash"])
combo_payment.pack()

# Buttons
frame_buttons = tk.Frame(root, bg="#f0f4f7")
frame_buttons.pack(pady=20)
btn_submit = tk.Button(frame_buttons, text="Submit", width=12, bg="#007acc", fg="white", command=submit_ticket)
btn_submit.pack(side=tk.LEFT, padx=10)
btn_reset = tk.Button(frame_buttons, text="Reset", width=12, bg="#888888", fg="white", command=reset_form)
btn_reset.pack(side=tk.LEFT, padx=10)

root.mainloop()