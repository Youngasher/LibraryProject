import tkinter as tk
import sqlite3
import mysql.connector
from tkinter import Frame, Label, Entry, Button, messagebox,LEFT,RIGHT
import os
from datetime import date
from tkinter import filedialog
from tkinter import ttk
import re
#import openpyxl , xlrd
#mport pathlibs
#from openpyxl import Workbook
from tkinter import *
from PIL import Image, ImageTk

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library_manager"
)

# Create a cursor object to execute SQL queries
cursor = mydb.cursor()

def register():
    global register_screen
    global register_frame
    register_screen = Toplevel(main_screen, bg="#000000")
    register_screen.title("Register")
    register_screen.geometry("1920x1080")

    global username
    global password
    global username_entry
    global password_entry   

    username = StringVar()
    password = StringVar()

    # Open the image file for the register frame
    image = Image.open("atuuuu.png")
    photo_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(register_screen, image=photo_image, height="100", width="100", bg="#f4d66a")
    image_label.image = photo_image  # Keep a reference to avoid garbage collection
    image_label.pack(side=LEFT, fill=BOTH, expand=True)
    #Label(register_screen, text="", bg="#000000").pack() 

    register_frame = Frame(register_screen, bg="#F8F4F1")
    register_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    Label(register_frame, pady=200,  text="Please enter details below", font=("Poppins", 20), bg="#F8F4F1" ,fg="#2563a8").pack()
    Label(register_frame, text="" ,bg="#F8F4F1").pack()

    # Open the image file for the register_frame frame
    image_frame = Image.open("avatar.png")
    photo_image_frame = ImageTk.PhotoImage(image_frame)
    image_label_frame = tk.Label(register_frame, image=photo_image_frame, height="80", width="80", bg="#F8F4F1")
    image_label_frame.image = photo_image_frame  # Keep a reference to avoid garbage collection
    image_label_frame.pack()
    Label(register_frame, text="", pady=10, bg="#F8F4F1").pack()

    Label(register_frame, text="Username * ", font=("Poppins", 16), bg="#F8F4F1" ,fg="#2563a8").pack()
    username_entry = Entry(register_frame, textvariable=username)
    username_entry.pack()
    Label(register_frame, text="", bg="#F8F4F1").pack()

    Label(register_frame, text="Password * " , font=("Poppins", 16), bg="#F8F4F1" ,fg="#2563a8").pack()
    password_entry = Entry(register_frame, textvariable=password, show='*')
    password_entry.pack()

    Label(register_frame, text="", bg="#F8F4F1").pack()
    Button(register_frame, text="Register", width=10, height=1, bg="#f4d66a", command=register_user).pack()

def register_user():
    # Get username and password from entry fields
    username_info = username.get()
    password_info = password.get()

    sql = "INSERT INTO user (id, username, password) VALUES (NULL, %s, %s)"
    val = (username_info, password_info)
    try:
        cursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Success", "Registration Successful")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error during registration: {err}")

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    # Check if both username and password fields are not empty
    # if username_info and password_info:
    #     # Open the credentials file
    #     with open("credentials.txt", "r") as file:
    #         # Read all lines from the file
    #         credentials = file.read().splitlines()

    #     # Check if the username already exists
    #     if username_info in credentials:
    #         messagebox.showerror("Error", "Username already exists. Please choose a different one.")
    #     else:
    #         # Append the new username and password to the file
    #         with open("credentials.txt", "a") as file:
    #             file.write(username_info + "\n")
    #             file.write(password_info + "\n")

    #         # Clear entry fields
    #         username_entry.delete(0, END)
    #         password_entry.delete(0, END)

    #         # Inform the user about successful registration
    #         messagebox.showinfo("Success", "Registration successful.")
    # else:
    #     # Show a message indicating that both fields are required
    #     messagebox.showerror("Error", "Please enter both username and password.")


def login():
    global login_screen
    login_screen = Toplevel(main_screen, bg="#bac8d8")
    login_screen.title("Login")
    login_screen.geometry("1920x1080")

    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    username_verify = StringVar()
    password_verify = StringVar()

    # Open the image file for the register frame
    image = Image.open("atuuuu.png")
    photo_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(login_screen, image=photo_image, height="100", width="100", bg="#f4d66a")
    image_label.image = photo_image  # Keep a reference to avoid garbage collection
    image_label.pack(side=LEFT, fill=BOTH, expand=True)
    #Label(register_screen, text="", bg="#000000").pack()

    login_frame = Frame(login_screen, bg="#F8F4F1")
    login_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    Label(login_frame, pady=200, text="Please enter details below to login", font=("Poppins", 18), bg="#F8F4F1" ,fg="#000000").pack()
    Label(login_frame, text="", bg="#F8F4F1").pack()

    # Open the image file for the register_frame frame
    image_frame = Image.open("avatar.png")
    photo_image_frame = ImageTk.PhotoImage(image_frame)
    image_label_frame = tk.Label(login_frame, image=photo_image_frame, height="80", width="80", bg="#F8F4F1")
    image_label_frame.image = photo_image_frame  # Keep a reference to avoid garbage collection
    image_label_frame.pack()
    Label(login_frame, text="", pady=10, bg="#F8F4F1").pack()

    Label(login_frame, text="Username * ", font=("Poppins", 12), bg="#F8F4F1" ,fg="#000000").pack()
    username_login_entry = Entry(login_frame, textvariable=username_verify)
    username_login_entry.pack()

    Label(login_frame, text="Password * ", font=("Poppins", 12), bg="#F8F4F1" ,fg="#000000").pack()
    password_login_entry = Entry(login_frame, textvariable=password_verify, show='*')
    password_login_entry.pack()

    button_font=("bold")

    Label(login_frame, text="", bg="#F8F4F1").pack()
    Button(login_frame, text="Login", font=button_font, bg="#f4d66a", width=10, height=1, command=login_verification).pack()

def login_verification():
    username1 = username_verify.get()
    password1 = password_verify.get()

    sql = "SELECT * FROM user WHERE username = %s AND password = %s"
    val = (username1, password1)
    cursor.execute(sql, val)
    user = cursor.fetchone()

    if user:
        administration_menu() 
    else:
        password_not_recognised()

    # Check if both username and password fields are not empty
    # if username1 and password1:
    #     # Open the credentials file
    #     with open("credentials.txt", "r") as file1:
    #         # Read all lines from the file
    #         verify = file1.read().splitlines()

    #     # Check if username exists in the list of usernames
    #     if username1 in verify:
    #         # Find the index of the username in the list
    #         index = verify.index(username1)
    #         # Check if the password matches the password stored in the next line
    #         if password1 == verify[index + 1]:
    #             login_sucess()
    #         else:
    #             password_not_recognised()
    #     else:
    #         user_not_found()
    # else:
    #     # Show a message indicating that both fields are required
    #     messagebox.showerror("Error", "Please enter both username and password.")


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen, pady=100, bg="#f4d66a")
    login_success_screen.title("Success")
    login_success_screen.geometry("1920x1080")

    # Open the image file for the register_frame frame
    image_frame = Image.open("atuuuu.png")
    photo_image_frame = ImageTk.PhotoImage(image_frame)
    image_label_frame = tk.Label(login_success_screen, image=photo_image_frame, height="500", width="450", bg="#f4d66a")
    image_label_frame.image = photo_image_frame  # Keep a reference to avoid garbage collection
    image_label_frame.pack()
    Label(login_success_screen, text="", pady=10, bg="#f4d66a").pack()

    Label(login_success_screen, text="Welcome To ATU Library Management System", font=("Poppins", 21), bg="#f4d66a" ,fg="#000000").pack()
    Label(login_success_screen, text="", bg="#f4d66a").pack()

    Label(login_success_screen, text="It is our pleasure to welcome you to ATU’s Library where your successful performance in the Technical University’s unique programmes \n \
          is of paramount importance to us. The library’s prime responsibility is to provide high quality, up-to-date and relevant information\n \
          resources and learning and research needs of students, staff and faculty of the Premier Technical University. Our wide range of information services and products are \n \
          specifically designed with the view to enhancing the academic excellence of our students in particular.\n \
          We, therefore, encourage you to take advantage of our rich information resources that are available both in print and electronic formats for your studies. Our supportive, \n \
          responsible and respectful staff would always be available to assist you to develop your information literacy skills for \n \
          your lifelong learning. We would be pleased to receive your feedback to enable us to improve our services all the time.\n \
          ", font=("Poppins", 13), bg="#f4d66a" ,fg="#000000").pack()
    Label(login_success_screen, text="", bg="#f4d66a").pack()

    # Label(login_success_screen, text="Login Success", bg="#70ff70").pack()
    Button(login_success_screen, text="Continue", command=open_administration_menu).pack()

    # Label(login_success_screen, text="Login Success", bg="#70ff70").pack()
    # Button(login_success_screen, text="OK", command=open_administration_menu).pack()

    # Label(login_success_screen, text="Login Success", bg="#70ff70").pack()
    # Button(login_success_screen, text="OK", command=open_administration_menu).pack()

def open_administration_menu():
    login_success_screen.destroy()
    administration_menu()

def delete_login_success():
    login_success_screen.destroy()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen) 
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()
    
def administration_menu():
    global admin_screen
    admin_screen = tk.Tk()
    admin_screen.title("Administrator Main Menu-Library Management System")
    admin_screen.geometry("1920x1080")

    # Set background color
    admin_screen.configure(bg="#f4d66a")  # Set the background color to white

    # Create two frames for admin options and report options
    admin_frame = Frame(admin_screen, bg="#f4d66a")
    report_frame = Frame(admin_screen, bg="#f4d66a")

    Label(admin_screen, text="Welcome To ATU Library Management System", pady=10, font=("Poppins", 21), bg="#f4d66a" ,fg="#000000").pack()

    # Create labels for the frames
    admin_label = LabelFrame(admin_frame, text="Admin Options")
    report_label = LabelFrame(report_frame, text="Report Options")

    # Create buttons for the admin options
    add_user_button = Button(admin_label, width=60, height=6, padx=20, pady=5, text="Add A New User" ,bg="#e8ecf2", command=add_new_users)
    unlock_user_button = Button(admin_label, width=60, height=6, padx=20, pady=5, text="Unlock User Utility",bg="#d1dae5", command=users_underlock)
    user_maintenance_button = Button(admin_label, width=60, height=6, padx=20, pady=5, text="User Maintenance", bg="#bac8d8", command=user_maintenance)
    change_password_button = Button(admin_label, width=60, height=6, padx=20, pady=5, text="Change User Password", bg="#a4b6cb", command=change_password)
    take_backup_button = Button(admin_label, width=60, height=6, padx=20, pady=5, text="Take Backup", bg="#8da4be", command=create_user_input_form)
    exit_button = Button(admin_label, width=60, height=6, padx=20, pady=5, text="Exit", bg="#7692b1", command=admin_screen.destroy)

    # Create buttons for the report options
    view_book_code_listing = Button(report_label, width=60, height=6, padx=10, pady=5, text="View Book Code Listing",bg="#7692b1", command=view_book_codeListing)
    view_user_listing = Button(report_label, width=60, height=6, padx=10, pady=5, text="View User Listing",bg="#8da4be",  command=view_userListing)
    view_book_type_listing = Button(report_label, width=60, height=6, padx=10, pady=5, text="View Book Type Listing",bg="#a4b6cb", command=Edit_book_detail)
    types_options = Label(report_label, width=60, height=1, padx=10, pady=5, text="Types Options")
    add_charges = Button(report_label, width=60, height=6, padx=10, pady=5, text="Add Charges",bg="#bac8d8", command=add_Charge_menu)
    add_new_book_type = Button(report_label, width=60, height=5, padx=10, pady=5, text="Add New Book Type", bg="#d1dae5", command=add_book_menu)
    add_new_book_code = Button(report_label, width=60, height=5, padx=10, pady=5, text="Add New Book Code", bg="#e8ecf2", command=add_book_code)

    # Pack the labels and buttons into their respective frames using grid
    admin_label.grid(row=0, column=0, padx=10, pady=10)
    add_user_button.grid(row=0, column=0, padx=10, pady=5)
    unlock_user_button.grid(row=1, column=0, padx=10, pady=5)
    user_maintenance_button.grid(row=2, column=0, padx=10, pady=5)
    change_password_button.grid(row=3, column=0, padx=10, pady=5)
    take_backup_button.grid(row=4, column=0, padx=10, pady=5)
    exit_button.grid(row=5, column=0, padx=10, pady=5)

    report_label.grid(row=0, column=0, padx=10, pady=10)
    view_book_code_listing.grid(row=0, column=0, padx=10, pady=5)
    view_user_listing.grid(row=1, column=0, padx=10, pady=5)
    view_book_type_listing.grid(row=2, column=0, padx=10, pady=5)
    types_options.grid(row=3, column=0, padx=10, pady=5)
    add_charges.grid(row=4, column=0, padx=10, pady=5)
    add_new_book_type.grid(row=5, column=0, padx=10, pady=5)
    add_new_book_code.grid(row=6, column=0, padx=10, pady=5)

    # Pack the frames into the main window
    admin_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=170 , pady=120 )
    report_frame.pack(side=RIGHT, fill=BOTH, expand=True  , pady=120)

    admin_screen.mainloop()





    
def add_Charge_menu():
    global add_charge_screen
    add_charge_screen=tk.Toplevel(main_screen)
    add_charge_screen.title("Add New Charges")
    add_charge_screen.geometry("350x200")
# Heading label
    heading_label = Label(add_charge_screen, text="Charges Details", fg="blue")
    heading_label.grid(row=0, columnspan=2, pady=10)  # Use grid layout with columnspan=2

# Create labels and entry fields for Charge details (using grid layout)
    charge_no_label = Label(add_charge_screen, text="Charge No.:")
    charge_no_label.grid(row=1, column=0)

    charge_no_entry = Entry(add_charge_screen)
    charge_no_entry.grid(row=1, column=1, padx=5)  # Add padding between label and entry
    charge_desc_label = Label(add_charge_screen, text="Charge Desc.:")
    charge_desc_label.grid(row=2, column=0)

    charge_desc_entry = Entry(add_charge_screen)
    charge_desc_entry.grid(row=2, column=1, padx=5)  # Add padding between label and entry

    charge_amt_label = Label(add_charge_screen, text="Charge Amt.:")
    charge_amt_label.grid(row=3, column=0)

    charge_amt_entry = Entry(add_charge_screen)
    charge_amt_entry.grid(row=3, column=1, padx=5)  # Add padding between label and entry

# Create buttons (Add, Ignore, Exit)
    button_frame = Frame(add_charge_screen)  # Create a separate frame for buttons
    button_frame.grid(row=4, columnspan=2, pady=10)  # Use grid layout

    add_button = Button(button_frame, text="Add", width=10)
    add_button.pack(side=LEFT, padx=5)  # Pack within button_frame

    ignore_button = Button(button_frame, text="Ignore", width=10)
    ignore_button.pack(side=LEFT, padx=5)  # Pack within button_frame

    exit_button = Button(button_frame, text="Exit", width=10, command=add_charge_screen.destroy)
    exit_button.pack(side=LEFT, padx=5)  # Pack within button_frame    
    
def add_book_menu():
    global add_new_book_screen
    add_new_book_screen=tk.Toplevel(main_screen)
    add_new_book_screen.title("Add New Book Type")
    add_new_book_screen.geometry("300x180")
# Heading label
    heading_label = Label(add_new_book_screen, text="Book Type Details")
    heading_label.grid(row=0, columnspan=2, pady=10)  # Use grid layout with columnspan=2

# Create labels and entry fields for Book details (using grid layout)
    type_no_label = Label(add_new_book_screen, text="Type No.")
    type_no_label.grid(row=1, column=0)

    type_no_entry = Entry(add_new_book_screen)
    type_no_entry.grid(row=1, column=1, padx=5)  # Add padding between label and entry
    type_desc_label = Label(add_new_book_screen, text="Description")
    type_desc_label.grid(row=2, column=0)

    type_desc_entry = Entry(add_new_book_screen)
    type_desc_entry.grid(row=2, column=1, padx=5)  # Add padding between label and entry


# Create buttons (Add, Ignore, Exit)
    button_frame = Frame(add_new_book_screen)  # Create a separate frame for buttons
    button_frame.grid(row=4, columnspan=2, pady=10)  # Use grid layout

    add_button = Button(button_frame, text="Add", width=10)
    add_button.pack(side=LEFT, padx=5)  # Pack within button_frame

    ignore_button = Button(button_frame, text="Ignore", width=10)
    ignore_button.pack(side=LEFT, padx=5)  # Pack within button_frame

    exit_button = Button(button_frame, text="Exit", width=10, command=add_new_book_screen.destroy)
    exit_button.pack(side=LEFT, padx=5)  # Pack within button_frame    
        
def add_book_code():
    global add_new_book_code
    add_new_book_code = tk.Toplevel(main_screen)
    add_new_book_code.title("Add New Book Type")
    add_new_book_code.geometry("300x180")

    # Heading label
    heading_label = tk.Label(add_new_book_code, text="Book Code Details")
    heading_label.grid(row=0, columnspan=2, pady=10)

    # Create labels and entry fields for Book details (using grid layout)
    type_no_label = tk.Label(add_new_book_code, text="Book Code")
    type_no_label.grid(row=1, column=0)

    type_no_entry = tk.Entry(add_new_book_code)
    type_no_entry.grid(row=1, column=1, padx=5)

    type_desc_label = tk.Label(add_new_book_code, text="Description")
    type_desc_label.grid(row=2, column=0)

    type_desc_entry = tk.Entry(add_new_book_code)
    type_desc_entry.grid(row=2, column=1, padx=5)

    # Create buttons (Add, Ignore, Exit)
    button_frame = tk.Frame(add_new_book_code)
    button_frame.grid(row=4, columnspan=2, pady=10)

    def add_book_to_db():
        # Fetch the inputs from the form
        book_code = type_no_entry.get()
        description = type_desc_entry.get()

        # Create a cursor object
        cursor = mydb.cursor()

        # Prepare the SQL query to insert the new book type number and description
        query = "INSERT INTO book_types (book_code, description) VALUES (%s, %s)"

        # Execute the query
        cursor.execute(query, (book_code, description))

        # Commit the transaction
        mydb.commit()

        # Close the cursor and connection
        cursor.close()
        mydb.close()

        # Optionally, show a success message
        tk.messagebox.showinfo("Success", "Book type added successfully.")

    add_button = tk.Button(button_frame, text="Add", width=10, command=add_book_to_db)
    add_button.pack(side=tk.LEFT, padx=5)

    ignore_button = tk.Button(button_frame, text="Ignore", width=10)
    ignore_button.pack(side=tk.LEFT, padx=5)

    exit_button = tk.Button(button_frame, text="Exit", width=10, command=add_new_book_code.destroy)
    exit_button.pack(side=tk.LEFT, padx=5)
        
def user_maintenance():
    user_maintenance_screen = tk.Toplevel(main_screen)
    user_maintenance_screen.title("User Maintenance")
    user_maintenance_screen.geometry("600x500")

    # Function to create a label frame
    def create_label_frame(parent, text):
        frame = tk.LabelFrame(parent, text=text, font=("Helvetica", 12, "bold"))
        frame.grid(padx=10, pady=10, sticky="nsew")
        return frame

    # User ID
    user_id_label = tk.Label(user_maintenance_screen, text="User ID:")
    user_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    user_id_entry = tk.Entry(user_maintenance_screen)
    user_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Personal Details Frame
    personal_frame = create_label_frame(user_maintenance_screen, "Personal Details")

    labels = ["User Name:", "Address Line 1:", "Address Line 2:"]
    for i, label_text in enumerate(labels):
        label = tk.Label(personal_frame, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(personal_frame)
        entry.grid(row=i, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

    phone_label = tk.Label(personal_frame, text="Phone:")
    phone_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    phone_entry = tk.Entry(personal_frame)
    phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    cell_label = tk.Label(personal_frame, text="Cell:")
    cell_label.grid(row=3, column=2, padx=10, pady=5, sticky="e")
    cell_entry = tk.Entry(personal_frame)
    cell_entry.grid(row=3, column=3, padx=10, pady=5, sticky="ew")

    email_label = tk.Label(personal_frame, text="Email:")
    email_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
    email_entry = tk.Entry(personal_frame)
    email_entry.grid(row=4, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

    # User Right Update Frame
    rights_frame = create_label_frame(user_maintenance_screen, "User Right Update")

    rights_labels = ["Admin Rights:", "Librarian Rights:", "User Rights:"]
    for i, right in enumerate(rights_labels):
        label = tk.Label(rights_frame, text=right)
        label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(rights_frame)
        entry.grid(row=i, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

    # Buttons
    button_frame = tk.Frame(user_maintenance_screen)
    button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

    update_button = tk.Button(button_frame, text="Update", width=10, command=lambda: print("Update"))
    update_button.grid(row=0, column=0, padx=10)

    ignore_button = tk.Button(button_frame, text="Ignore", width=10, command=lambda: print("Ignore"))
    ignore_button.grid(row=0, column=1, padx=10)

    exit_button = tk.Button(button_frame, text="Exit", width=10, command=user_maintenance_screen.destroy)
    exit_button.grid(row=0, column=2, padx=10)


# Call the function to display the user maintenance screen
#user_maintenance()


    
def change_password_logic(old_password_entry, new_password_entry, confirm_password_entry):
    # Retrieve old, new, and confirm passwords
    old_password = old_password_entry.get()
    new_password = new_password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Check if old password is correct
    if old_password != "asher123":  # Assuming password1 represents the current password
        messagebox.showerror("Error", "Incorrect old password")
        return change_password

    # Check if new password matches the confirmation
    if new_password != confirm_password:
        messagebox.showerror("Error", "New password and confirmation do not match")
        return

    # Check the strength of the new password
    if not is_strong_password(new_password):
        messagebox.showerror("Error", "New password is not strong enough")
        return

    # Password change logic goes here
    # Assuming it's successful, you can show a success message
    messagebox.showinfo("Success", "Password changed successfully")

def change_password():
    global password_change
    password_change = tk.Toplevel(main_screen, padx=10, pady=10)
    password_change.title("Change Password")

    # User details section
    user_details_label = Label(password_change, text="User Details", font=("Arial", 14))
    user_details_label.grid(row=0, columnspan=2, pady=5)

    user_id_label = Label(password_change, text="User ID:")
    user_id_label.grid(row=1, column=0, padx=5, pady=5)

    user_id_value_label = Label(password_change, text="--")  # Placeholder value
    user_id_value_label.grid(row=1, column=1, padx=5, pady=5)

    # Old password section
    old_password_label = Label(password_change, text="Old Password:")
    old_password_label.grid(row=2, column=0, padx=5, pady=5)

    old_password_entry = Entry(password_change, show="*")  # Hide characters for security
    old_password_entry.grid(row=2, column=1, padx=5, pady=5)

    # New password section
    new_password_label = Label(password_change, text="New Password:")
    new_password_label.grid(row=3, column=0, padx=5, pady=5)

    new_password_entry = Entry(password_change, show="*")  # Hide characters for security
    new_password_entry.grid(row=3, column=1, padx=5, pady=5)

    # Confirm password section
    confirm_password_label = Label(password_change, text="Confirm Password:")
    confirm_password_label.grid(row=4, column=0, padx=5, pady=5)

    confirm_password_entry = Entry(password_change, show="*")  # Hide characters for security
    confirm_password_entry.grid(row=4, column=1, padx=5, pady=5)
    
   

    # Button frame
    button_frame = Frame(password_change)
    button_frame.grid(row=5, columnspan=2, pady=10)

    change_button = Button(button_frame, text="Change Password", width=15, command=lambda: change_password_logic(old_password_entry, new_password_entry, confirm_password_entry))
    change_button.pack(side=LEFT, padx=10, pady=5)

    ignore_button = Button(button_frame, text="Ignore", width=10,command=password_change.destroy)
    ignore_button.pack(side=LEFT, padx=10, pady=5)
    
    exit_button = Button(button_frame, text="Exit", width=10, command=password_change.destroy)
    exit_button.pack(side=LEFT, padx=10, pady=5)
    
    
    
def is_strong_password(password):
    # Password strength criteria: at least 8 characters, contains uppercase, lowercase, digit, and special character
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*()_+{}|:<>?~-]", password):
        return False
    return True
    
    


# Define listbox_page as a global variable
listbox_page = None

def unlock_user():
    selected_index = locked_users_listbox.curselection()
    if selected_index:
        selected_user = locked_users_listbox.get(selected_index)
        # Your unlock user logic here
        messagebox.showinfo("Success", f"User '{selected_user}' unlocked successfully.")
    else:
        messagebox.showerror("Error", "Please select a user to unlock.")

def exit_page():
    listbox_page.destroy()

def users_underlock():
    global listbox_page
    listbox_page = tk.Toplevel(main_screen)
    listbox_page.title("Locked Users Page")
    listbox_page.geometry("450x300")

    # Title Label
    title_label = tk.Label(listbox_page, text="Locked Users", font=("Arial", 14))
    title_label.pack(pady=10)
    
    # Listbox to display locked users
    locked_users = ["User1", "User2", "User3"]  # Example locked users
    global locked_users_listbox
    locked_users_listbox = tk.Listbox(listbox_page)
    for user in locked_users:
        locked_users_listbox.insert(tk.END, user)
    locked_users_listbox.pack(pady=10)
    
    # Button frame
    button_frame = Frame(listbox_page)
    button_frame.pack(pady=10)

    unlock_button = tk.Button(button_frame, text="Unlock User", width=10, command=unlock_user)
    unlock_button.pack(side=tk.LEFT, padx=10, pady=5)
    
    exit_button = tk.Button(button_frame, text="Exit", width=10, command=exit_page)
    exit_button.pack(side=tk.LEFT, padx=10, pady=5)


# Create the main window
def Edit_book_detail():
    global edit_book
    edit_book = tk.Toplevel(main_screen)
    edit_book.title("Edit Book Details")
    edit_book.geometry("600x400")

    # Create a frame for the window content
    frame = tk.Frame(edit_book)
    frame.pack(fill=tk.BOTH, expand=True)

    # Title Label
    title_label = tk.Label(frame, text="Edit Book Details", font=("Arial", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=4, pady=10)

    # Serial No. Label and Textfield
    serial_label = tk.Label(frame, text="Serial No.:", font=("Arial", 12))
    serial_label.grid(row=1, column=0, padx=10, pady=5)

    serial_entry = tk.Entry(frame, font=("Arial", 12))
    serial_entry.grid(row=1, column=1, padx=10, pady=5)

    # Create a LabelFrame for Book Details
    book_detail_frame = tk.LabelFrame(frame, text="Book Details", font=("Arial", 12, "bold"))
    book_detail_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

    # Book Name Label and Textfield
    book_name_label = tk.Label(book_detail_frame, text="Book Name:", font=("Arial", 12))
    book_name_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

    book_name_entry = tk.Entry(book_detail_frame, font=("Arial", 12))
    book_name_entry.insert(0, "Education")  # Set default text
    book_name_entry.grid(row=3, column=1, columnspan=3, padx=10, pady=5, sticky="w")

    # Author Name Label and Textfield
    author_name_label = tk.Label(book_detail_frame, text="Author Name:", font=("Arial", 12))
    author_name_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

    author_name_entry = tk.Entry(book_detail_frame, font=("Arial", 12))
    author_name_entry.grid(row=4, column=1, columnspan=3, padx=10, pady=5, sticky="w")

    # Book Des Label and Textfield with Change Picture Button
    book_des_label = tk.Label(book_detail_frame, text="Book Description:", font=("Arial", 12))
    book_des_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

    book_des_entry = tk.Entry(book_detail_frame, font=("Arial", 12))
    book_des_entry.grid(row=5, column=1, columnspan=2, padx=10, pady=5, sticky="w")

    change_picture_button = tk.Button(book_detail_frame, text="Change Picture", font=("Arial", 12))
    change_picture_button.grid(row=5, column=3, padx=10, pady=5, sticky="w")

    # Book Type Label and Dropdown
    book_type_label = tk.Label(book_detail_frame, text="Book Type:", font=("Arial", 12))
    book_type_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")

    book_type_combobox = ttk.Combobox(book_detail_frame, state="readonly", font=("Arial", 10), width=5)
    book_type_combobox['values'] = (1, 2, 3, 4, 5)  # Example numeric values
    book_type_combobox.current(0)  # Set default value
    book_type_combobox.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    # Uneditable Book Type Textfield
    book_type_entry = tk.Entry(book_detail_frame, font=("Arial", 10), state="readonly", width=20, bg="#ff0000")  # Red background
    book_type_entry.grid(row=6, column=2,sticky="w")

    # Book Code Label and Dropdown
    book_code_label = tk.Label(book_detail_frame, text="Book Code:", font=("Arial", 12))
    book_code_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")

    book_code_combobox = ttk.Combobox(book_detail_frame, state="readonly", font=("Arial", 10), width=5)
    book_code_combobox['values'] = (101, 102, 103, 104)  # Example numeric values
    book_code_combobox.current(0)  # Set default value
    book_code_combobox.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    # Uneditable Book Code Textfield
    book_code_entry = tk.Entry(book_detail_frame, font=("Arial", 10), state="readonly", width=20, bg="#00ff00")  # Green background
    book_code_entry.grid(row=7, column=2,sticky="w")



        # Bind the update functions to dropdown selection events
    def update_book_type_name(event):
        book_type = book_type_combobox.get()
        book_type_name = ""
        if book_type == "1":
            book_type_name = "Education"
        elif book_type == "2":
            book_type_name = "Fiction"
        elif book_type == "3":
            book_type_name = "Science"
        elif book_type == "4":
            book_type_name = "History"
        elif book_type == "5":
            book_type_name = "Biography"
        book_type_entry.config(state="normal")
        book_type_entry.delete(0, tk.END)
        book_type_entry.insert(0, book_type_name)
        book_type_entry.config(state="readonly")

    def update_book_code_name(event):
        book_code = book_code_combobox.get()
        book_code_name = ""
        if book_code == "101":
            book_code_name = "ABC"
        elif book_code == "102":
            book_code_name = "DEF"
        elif book_code == "103":
            book_code_name = "GHI"
        elif book_code == "104":
            book_code_name = "JKL"
        book_code_entry.config(state="normal")
        book_code_entry.delete(0, tk.END)
        book_code_entry.insert(0, book_code_name)
        book_code_entry.config(state="readonly")

    book_type_combobox.bind("<<ComboboxSelected>>", update_book_type_name)
    book_code_combobox.bind("<<ComboboxSelected>>", update_book_code_name)

    # Publish Name Label and Textfield
    publish_name_label = tk.Label(book_detail_frame, text="Publish Name:", font=("Arial", 12))
    publish_name_label.grid(row=8, column=0, padx=10, pady=5, sticky="e")

    publish_name_entry = tk.Entry(book_detail_frame, font=("Arial", 12))
    publish_name_entry.grid(row=8, column=1, columnspan=3, padx=10, pady=5, sticky="w")

    # Lab Name Label and Textfield
    lab_name_label = tk.Label(book_detail_frame, text="Lab Name:", font=("Arial", 12))
    lab_name_label.grid(row=8, column=2, padx=10, pady=5, sticky="e")

    lab_name_entry = tk.Entry(book_detail_frame, font=("Arial", 12))
    lab_name_entry.grid(row=8, column=3, columnspan=3, padx=10, pady=5, sticky="w")

    # Buttons
    edit_button = tk.Button(frame, text="Edit", width=10, command=lambda: print("Update"))
    edit_button.grid(row=10, column=0, padx=10, pady=20)

    ignore_button = tk.Button(frame, text="Ignore", width=10, command=lambda: print("Ignore"))
    ignore_button.grid(row=10, column=1, padx=10, pady=20)

    exit_button = tk.Button(frame, text="Exit", width=10, command=edit_book.destroy)
    exit_button.grid(row=10, column=2, padx=10, pady=20)


def view_book_codeListing():
    # Create a new window for viewing book code listing
    book_code_window = tk.Toplevel()
    book_code_window.title("Book Code Listing")
    book_code_window.geometry("600x400")

    # Add labels and fields to display book codes
    book_codes = ["101 - Book A", "102 - Book B", "103 - Book C", "104 - Book D"]  # Example book codes
    for i, book_code in enumerate(book_codes):
        label = tk.Label(book_code_window, text=book_code, font=("Arial", 12))
        label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

def view_userListing():
    # Create a new window for viewing user listing
    user_listing_window = tk.Toplevel()
    user_listing_window.title("User Listing")
    user_listing_window.geometry("600x400")

    # Create a cursor object
    cursor = mydb.cursor()

    # Prepare the SQL query to fetch all students
    query = "SELECT first_name, last_name FROM students"

    # Execute the query
    cursor.execute(query)

    # Fetch all the records
    records = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    mydb.close()

    # Add labels and fields to display user listing
    for i, record in enumerate(records):
        user = f"{record[0]} {record[1]}" # Assuming first_name and last_name are the columns you want to display
        label = tk.Label(user_listing_window, text=user, font=("Arial", 12))
        label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
# Example usage:
# view_book_code_listing()  # Call this function to view the book code listing
# view_user_listing()  # Call this function to view the user listing


def create_user_input_form():
    def save_user_details():
        global user_add
        user_add = tk.Toplevel(main_screen)
        user_add.title("Edit Book Details")
        user_add.geometry("600x400")

        frame = tk.Frame(edit_book)
        frame.pack(fill=tk.BOTH, expand=True)

        # Create labels and entry fields
        tk.Label(frame, text="First Name:").pack()
        first_name_entry = tk.Entry(frame)
        first_name_entry.pack()

        tk.Label(frame, text="Last Name:").pack()
        last_name_entry = tk.Entry(frame)
        last_name_entry.pack()

        tk.Label(frame, text="Age:").pack()
        age_entry = tk.Entry(frame)
        age_entry.pack()

        # Button to save user details
        tk.Button(frame, text="Save", command=save_user_details).pack()

        # Run the GUI
        frame.mainloop()

# Call the function to create the user input form
create_user_input_form()

def add_student(first_name, last_name, title, age, nationality, registration_status, completed_courses, semesters, terms_accepted):
    # This is where you would add the code to insert the data into your database
    try:
        cursor = mydb.cursor()

        # Prepare the SQL query
        query = """
        INSERT INTO students (id, first_name, last_name, title, age, nationality, registration_status, completed_courses, semesters, terms_accepted)
        VALUES (NULL, %s, %s, %s, %s, %s, "Yes", %s, %s, "Yes")
        """

        # Execute the query
        cursor.execute(query, (first_name, last_name, title, age, nationality, completed_courses, semesters))

        # Commit the transaction
        mydb.commit()

        # Close the connection
        cursor.close()
        mydb.close()

        # Optionally, show a success message
        tk.messagebox.showinfo("Success", "User data added successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        tk.messagebox.showerror("Error", "Failed to add user data.")


    print(f"Adding student: {first_name} {last_name}")


def add_new_users():
    global add_new_user
    global first_name_entry
    global last_name_entry
    global title_combobox
    global age_spinbox
    global nationality_combobox
    global reg_status_var
    global numcourses_spinbox
    global numsemesters_spinbox
    global accept_var
    add_new_user = tk.Toplevel(main_screen)
    add_new_user.title("Data Entry Form")
    add_new_user.geometry("600x400")
    
    # Create a frame for the window content
    frame = tk.Frame(add_new_user)
    frame.pack()

    # Saving User Info
    user_info_frame = tk.LabelFrame(frame, text="User Information")
    user_info_frame.grid(row=0, column=0, padx=20, pady=10)

    first_name_label = tk.Label(user_info_frame, text="First Name")
    first_name_label.grid(row=0, column=0)
    last_name_label = tk.Label(user_info_frame, text="Last Name")
    last_name_label.grid(row=0, column=2)

    first_name_entry = tk.Entry(user_info_frame)
    first_name_entry.grid(row=1, column=0)
    last_name_entry = tk.Entry(user_info_frame)
    last_name_entry.grid(row=1, column=2)

    title_label = tk.Label(user_info_frame, text="Title")
    title_label.grid(row=2, column=0)
    title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
    title_combobox.grid(row=3, column=0)

    age_label = tk.Label(user_info_frame, text="Age")
    age_label.grid(row=2, column=2)
    age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=110)
    age_spinbox.grid(row=3, column=2)

    nationality_label = tk.Label(user_info_frame, text="Nationality")
    nationality_label.grid(row=2, column=1)
    nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
    nationality_combobox.grid(row=3, column=1)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Saving Course Info
    courses_frame = tk.LabelFrame(frame, text="Course Information")
    courses_frame.grid(row=1, column=0, padx=20, pady=10)

    registered_label = tk.Label(courses_frame, text="Registration Status")
    registered_label.grid(row=0, column=0)

    reg_status_var = tk.StringVar(value="Not Registered")
    registered_check = tk.Checkbutton(courses_frame, text="Currently Registered", variable=reg_status_var, onvalue="Registered", offvalue="Not registered")
    registered_check.grid(row=1, column=0)

    numcourses_label = tk.Label(courses_frame, text="# Completed Courses")
    numcourses_label.grid(row=0, column=1)
    numcourses_spinbox = tk.Spinbox(courses_frame, from_=0, to='infinity')
    numcourses_spinbox.grid(row=1, column=1)

    numsemesters_label = tk.Label(courses_frame, text="# Semesters")
    numsemesters_label.grid(row=0, column=2)
    numsemesters_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
    numsemesters_spinbox.grid(row=1, column=2)

    for widget in courses_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Accept terms
    terms_frame = tk.LabelFrame(frame, text="Terms & Conditions")
    terms_frame.grid(row=2, column=0, padx=20, pady=10)

    accept_var = tk.StringVar(value="Not Accepted")
    terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
    terms_check.grid(row=0, column=0)

    # Button
    button = tk.Button(frame, text="Enter data", command=lambda: submit_data())
    button.grid(row=3, column=0, padx=20, pady=10)


def submit_data():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()
    registration_status = reg_status_var.get()
    completed_courses = numcourses_spinbox.get()
    semesters = numsemesters_spinbox.get()
    terms_accepted = accept_var.get()

    add_student(first_name, last_name, title, age, nationality, registration_status, completed_courses, semesters, terms_accepted)

def main_account_screen():
    global main_screen
    main_screen = tk.Tk()
    main_screen.geometry("1920x1080")
    main_screen.title("Account Login")

    # Create the login and registration section
    login_frame = tk.Frame(main_screen ,pady=200, bg="#2563a8")
    login_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    Label(login_frame, text="Choose Login Or Register", bg="#2563a8", width="30", height="2", font=("Poppins", 18), fg="#fff").pack()
    Label(login_frame, text="" , bg="#2563a8" ).pack()

    # Open the image file
    image = Image.open("atuu.png")

    # Convert the image to a format supported by tkinter
    photo_image = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = tk.Label(login_frame, image=photo_image, height="80", width="80", bg="#2563a8")
    image_label.pack()
    Label(login_frame, text="",pady=10, bg="#2563a8").pack() 

    Button(login_frame, text="Login", height="2", width="30", command=login, font=("Arial", 12), bg="#f4d66a" , fg="#2563a8").pack()
    Label(login_frame, text="",pady=5, bg="#2563a8").pack() 

    Button(login_frame, text="Register", height="2", width="30", command=register, font=("Arial", 12), bg="#f4d66a" ,fg="#2563a8").pack()

    # Create the gif display section
    gif_frame = tk.Frame(main_screen)
    gif_frame.pack(side=LEFT, fill=BOTH, expand=True)
    gif_lb = tk.Label(gif_frame,  bg="#f4d66a")
    gif_lb.pack(fill=BOTH, expand=True)
    ready_gif(gif_lb, login_frame)  

    main_screen.mainloop()

def ready_gif(label, login_frame):  
    print('Started')
    gif_file = Image.open('gif11.gif')

    gif_frames = []
    for r in range(0, gif_file.n_frames):
        gif_file.seek(r)
        gif_frames.append(gif_file.copy())

    frame_delay = gif_file.info['duration']
    print('Completed')
    play_gif(label, gif_frames, frame_delay, login_frame)  

def play_gif(label, frames, delay, login_frame, count=-1):  
    if count >= len(frames) - 1:
        count = -1

    count += 1
    current_frame = ImageTk.PhotoImage(frames[count])
    label.config(image=current_frame)
    label.image = current_frame
    main_screen.after(delay, play_gif, label, frames, delay, login_frame, count)

if __name__ == "__main__":
    frame_count = -1
    main_account_screen()
