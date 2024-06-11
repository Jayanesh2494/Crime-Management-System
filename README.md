**Crime Management System**
This is a Crime Management System built using Python and MongoDB. It provides functionalities for users to file complaints and track them, while admins can manage users, complaints, and generate reports.

**Features**
User Registration and Authentication
Role-based Access Control (User and Admin roles)
File and Track Complaints (Users)
Manage Users and Complaints (Admins)
Generate Reports (Admins)
Password Encryption and Secure Authentication

**Technologies Used****
Python
Tkinter for GUI
MongoDB for database
bcrypt for password hashing

**Installation**
Clone the repository:
git clone https://github.com/your-username/crime-management-system.git
cd crime-management-system

Install the required packages:
pip install -r requirements.txt

Set up MongoDB:
Ensure you have MongoDB installed and running on your local machine. The default connection string is mongodb://localhost:27017/. You can modify this in the db.py file if needed.

Configuration
Ensure you have a config.py file with the following content to manage your MongoDB connection string:

MONGO_URI = 'mongodb://localhost:27017/crime_management_system'
Running the Application

**Start the application:**
python app.py

Log in or Sign up:

User: Sign up and log in to file and track complaints.
Admin: Log in to manage users and complaints, and to generate reports.

Project Structure

crime-management-system/
│
├── config/
│   └── db.py              # MongoDB connection
├── dao/
│   ├── user_dao.py        # Data access object for users
│   └── crime_dao.py       # Data access object for crimes
├── models/
│   ├── user.py            # User model
│   └── crime.py           # Crime model
├── security/
│   └── security_utils.py  # Password hashing and checking
├── app.py                 # Main application file
├── requirements.txt       # List of dependencies
└── README.md              # Readme file

**Usage**
User Actions
Sign Up: Create a new user or admin account.
Log In: Log in with your credentials.
File a Complaint: File a new complaint specifying the crime type, description, date, and location.
Track Complaints: View the status of your filed complaints.
Admin Actions
Manage Users: View and manage user accounts.
Manage Complaints: View and manage filed complaints, including updating their status.
Generate Reports: View reports and statistics about the complaints.

**Contributing**
Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature-name).
Open a pull request.

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

**Acknowledgements**
MongoDB
Tkinter
bcrypt
