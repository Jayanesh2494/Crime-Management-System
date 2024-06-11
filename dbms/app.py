import tkinter as tk
from tkinter import messagebox
from dao import UserDAO, CrimeDAO
from models import User, Crime
from security_utils import hash_password, check_password
from PIL import Image, ImageTk


class CrimeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crime Management System")
        self.root.geometry("800x600")  
        self.user_dao = UserDAO()
        self.crime_dao = CrimeDAO()
        self.current_user_role = None

        self.create_login_frame()

    def create_login_frame(self):
        self.clear_frame()

        self.login_frame = tk.Frame(self.root, bg="#2e3f4f")
        self.login_frame.pack(fill="both", expand=True)

        tk.Label(self.login_frame, text="Login", font=("Helvetica", 16), bg="#2e3f4f", fg="white").pack(pady=10)

        tk.Label(self.login_frame, text="Username:", bg="#2e3f4f", fg="white").pack(pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.login_frame, text="Password:", bg="#2e3f4f", fg="white").pack(pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=5)

        tk.Label(self.login_frame, text="Role:", bg="#2e3f4f", fg="white").pack(pady=5)
        self.role_var = tk.StringVar(value='user')
        tk.Radiobutton(self.login_frame, text="User", variable=self.role_var, value='user', bg="#2e3f4f", fg="white").pack(pady=5)
        tk.Radiobutton(self.login_frame, text="Admin", variable=self.role_var, value='admin', bg="#2e3f4f", fg="white").pack(pady=5)

        tk.Button(self.login_frame, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.login_frame, text="Create Account", command=self.create_signup_frame).pack(pady=5)

    def create_signup_frame(self):
        self.clear_frame()

        self.signup_frame = tk.Frame(self.root, bg="#2e3f4f")
        self.signup_frame.pack(fill="both", expand=True)

        tk.Label(self.signup_frame, text="Sign Up", font=("Helvetica", 16), bg="#2e3f4f", fg="white").pack(pady=10)

        tk.Label(self.signup_frame, text="Username:", bg="#2e3f4f", fg="white").pack(pady=5)
        self.new_username_entry = tk.Entry(self.signup_frame)
        self.new_username_entry.pack(pady=5)

        tk.Label(self.signup_frame, text="Password:", bg="#2e3f4f", fg="white").pack(pady=5)
        self.new_password_entry = tk.Entry(self.signup_frame, show="*")
        self.new_password_entry.pack(pady=5)

        tk.Label(self.signup_frame, text="Role:", bg="#2e3f4f", fg="white").pack(pady=5)
        self.new_role_var = tk.StringVar(value='user')
        tk.Radiobutton(self.signup_frame, text="User", variable=self.new_role_var, value='user', bg="#2e3f4f", fg="white").pack(pady=5)
        tk.Radiobutton(self.signup_frame, text="Admin", variable=self.new_role_var, value='admin', bg="#2e3f4f", fg="white").pack(pady=5)

        tk.Button(self.signup_frame, text="Sign Up", command=self.signup).pack(pady=10)
        tk.Button(self.signup_frame, text="Back to Login", command=self.create_login_frame).pack(pady=5)

    def create_user_portal(self, username):
        self.current_user_role = 'user'
        self.clear_frame()

        self.user_frame = tk.Frame(self.root, bg="#2e3f4f")
        self.user_frame.pack(fill="both", expand=True)

        tk.Label(self.user_frame, text=f"Welcome, {username}", font=("Helvetica", 16), bg="#2e3f4f", fg="white").pack(pady=10)

        tk.Button(self.user_frame, text="File a Complaint", command=self.create_complaint_frame).pack(pady=10)
        tk.Button(self.user_frame, text="Track Complaints", command=self.track_complaints).pack(pady=10)
        tk.Button(self.user_frame, text="Logout", command=self.create_login_frame).pack(pady=10)

    def create_complaint_frame(self):
        self.clear_frame()

        self.complaint_frame = tk.Frame(self.root, bg="#2e3f4f")
        self.complaint_frame.pack(fill="both", expand=True)

        tk.Label(self.complaint_frame, text="File a Complaint", font=("Helvetica", 16), bg="#2e3f4f", fg="white").pack(pady=10)

        tk.Label(self.complaint_frame, text="Type:", bg="#2e3f4f", fg="white").pack(pady=5)
        self.type_entry = tk.Entry(self.complaint_frame)
        self.type_entry.pack(pady=5)

        tk.Label(self.complaint_frame, text="Description:", bg="#2e3f4f", fg="white").pack(pady=5)
        self.description_entry = tk.Entry(self.complaint_frame)
        self.description_entry.pack(pady=5)

        tk.Label(self.complaint_frame, text="Date:", bg="#2e3f4f", fg="white").pack(pady=5)
        self.date_entry = tk.Entry(self.complaint_frame)
        self.date_entry.pack(pady=5)

        tk.Label(self.complaint_frame, text="Location:", bg="#2e3f4f", fg="white").pack(pady=5)
        self.location_entry = tk.Entry(self.complaint_frame)
        self.location_entry.pack(pady=5)

        tk.Button(self.complaint_frame, text="Submit", command=self.file_complaint).pack(pady=10)
        tk.Button(self.complaint_frame, text="Back", command=self.create_user_portal).pack(pady=5)

    def create_admin_portal(self, username):
        self.current_user_role = 'admin'
        self.clear_frame()

        self.admin_frame = tk.Frame(self.root, bg="#2e3f4f")
        self.admin_frame.pack(fill="both", expand=True)

        tk.Label(self.admin_frame, text=f"Welcome Admin, {username}", font=("Helvetica", 16), bg="#2e3f4f", fg="white").pack(pady=10)

        tk.Button(self.admin_frame, text="Manage Users", command=self.manage_users).pack(pady=10)
        tk.Button(self.admin_frame, text="Manage Complaints", command=self.manage_complaints).pack(pady=10)
        tk.Button(self.admin_frame, text="View Reports", command=self.view_reports).pack(pady=10)
        tk.Button(self.admin_frame, text="Logout", command=self.create_login_frame).pack(pady=10)

    def file_complaint(self):
        crime_type = self.type_entry.get()
        description = self.description_entry.get()
        date = self.date_entry.get()
        location = self.location_entry.get()

        if not crime_type or not description or not date or not location:
            messagebox.showerror("Error", "All fields are required")
            return

        crime = Crime(crime_type, description, date, location)
        self.crime_dao.add_crime(crime)
        messagebox.showinfo("Success", "Complaint filed successfully!")
        self.create_user_portal()

    def manage_users(self):
        self.clear_frame()

        self.user_mgmt_frame = tk.Frame(self.root, bg="#2e3f4f")
        self.user_mgmt_frame.pack(fill="both", expand=True)

        tk.Label(self.user_mgmt_frame, text="Manage Users", font=("Helvetica", 16), bg="#2e3f4f", fg="white").pack(pady=10)

        # Add functionalities to manage users

        tk.Button(self.user_mgmt_frame, text="Back", command=self.create_admin_portal).pack(pady=10)

    def manage_complaints(self):
        self.clear_frame()

        self.complaint_mgmt_frame = tk.Frame(self.root, bg="#2e3f4f")
        self.complaint_mgmt_frame.pack(fill="both", expand=True)

        tk.Label(self.complaint_mgmt_frame, text="Manage Complaints", font=("Helvetica", 16), bg="#2e3f4f", fg="white").pack(pady=10)

        complaints = self.crime_dao.get_crimes()
        for crime in complaints:
            tk.Label(self.complaint_mgmt_frame, text=f"{crime['type']} - {crime['description']} - {crime['status']}", bg="#2e3f4f", fg="white").pack(pady=5)
            tk.Button(self.complaint_mgmt_frame, text="Resolve", command=lambda c=crime: self.resolve_complaint(c)).pack(pady=5)

        tk.Button(self.complaint_mgmt_frame, text="Back", command=self.create_admin_portal).pack(pady=10)

    def resolve_complaint(self, crime):
        self.crime_dao.update_crime_status(crime['_id'], 'Resolved')
        messagebox.showinfo("Success", "Complaint resolved!")
        self.manage_complaints()

    def view_reports(self):
        self.clear_frame()

        self.reports_frame = tk.Frame(self.root, bg="#2e3f4f")
        self.reports_frame.pack(fill="both", expand=True)

        tk.Label(self.reports_frame, text="Reports", font=("Helvetica", 16), bg="#2e3f4f", fg="white").pack(pady=10)

        # Visualization and report generation functionalities here

        tk.Button(self.reports_frame, text="Back", command=self.create_admin_portal).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()

        user = self.user_dao.find_user(username, role)
        if user and check_password(user['password'], password):
            if role == 'admin':
                self.create_admin_portal(username)
            else:
                self.create_user_portal(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def signup(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        role = self.new_role_var.get()

        if self.user_dao.find_user(username, role):
            messagebox.showerror("Error", "Username already exists")
            return

        hashed_password = hash_password(password)
        user = User(username, hashed_password, role)
        self.user_dao.add_user(user)
        messagebox.showinfo("Success", "Account created successfully!")
        self.create_login_frame()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CrimeManagementApp(root)
    root.mainloop()
