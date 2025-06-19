from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk

# Connect to MySQL
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",       
        password="Honne1151@",    
        database="student_registration"
    )
    return conn

# Insert form data into MySQL
def insert_data(name, phone, gender, emergency, payment_mode, remember_me):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        sql = "INSERT INTO registrations (name, phone, gender, emergency_contact, payment_mode, remember_me) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, phone, gender, emergency, payment_mode, remember_me)
        cursor.execute(sql, values)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Registration saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

# Submit form handler
def submit_form():
    name = name_value.get()
    phone = phone_value.get()
    gender = gender_value.get()
    emergency = emergency_value.get()
    payment_mode = payment_value.get()
    remember_me = check_value.get()

    # Simple validation
    if name == "" or phone == "":
        messagebox.showwarning("Missing Info", "Name and Phone are required.")
        return

    insert_data(name, phone, gender, emergency, payment_mode, remember_me)


# new tab for viewing registered details
def view_registrations():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registrations")
    rows = cursor.fetchall()
    conn.close()

    view_window = Toplevel(root)
    view_window.title("All Registrations")
    view_window.geometry("700x400")

    tree = ttk.Treeview(view_window, columns=("ID", "Name", "Phone", "Gender", "Emergency", "Payment", "Remember"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Phone", text="Phone")
    tree.heading("Gender", text="Gender")
    tree.heading("Emergency", text="Emergency")
    tree.heading("Payment", text="Payment Mode")
    tree.heading("Remember", text="Remember Me")

    tree.pack(fill=BOTH, expand=True)

    for row in rows:
        tree.insert("", END, values=row)


# GUI Code
root = Tk()
root.geometry("400x400" \
"")
root.title("Student Registration Form")

Label(root, text="Python Registration Form", font="comicsansms 15 bold").grid(row=0, column=2, pady=10)

# Labels
Label(root, text="Name").grid(row=1, column=1)
Label(root, text="Phone").grid(row=2, column=1)
Label(root, text="Gender").grid(row=3, column=1)
Label(root, text="Emergency").grid(row=4, column=1)
Label(root, text="Payment Mode").grid(row=5, column=1)

# Variables
name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
emergency_value = StringVar()
payment_value = StringVar()
check_value = IntVar()

# Entry Fields
Entry(root, textvariable=name_value).grid(row=1, column=2)
Entry(root, textvariable=phone_value).grid(row=2, column=2)
Entry(root, textvariable=gender_value).grid(row=3, column=2)
Entry(root, textvariable=emergency_value).grid(row=4, column=2)
Entry(root, textvariable=payment_value).grid(row=5, column=2)

# Checkbox
Checkbutton(text="Remember me?", variable=check_value).grid(row=6, column=2)

# Submit Button
Button(text="Submit", command=submit_form).grid(row=7, column=2, pady=10)



#creating a button to see registrattions
Button(text="View Registrations", command=view_registrations).grid(row=8, column=2, pady=5)


root.mainloop()