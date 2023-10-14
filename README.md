# Employee Directory - Django Project for CMPSC 487W

## Introduction
This project is a simple Employee Directory developed using Django. It allows users to view a list of employees, add new employees, edit existing employee details, and search for employees by their name or ID.

## Features
- **View Employees**: Display a list of all employees with their details.
- **Add Employees**: A form to add new employees to the directory. Employee IDs are generated automatically.
- **Edit Employees**: Allows editing of an employee's details except for their unique ID.
- **Search**: Users can search for employees using either their name or their unique ID.
- **Sort**: Employees can be sorted by their name or ID.

## Installation and Setup
1. Clone the repository or download the project to your local machine.
2. Navigate to the project's root directory in your terminal.
3. Run `pip install -r requirements.txt` to install the necessary dependencies.
4. Make sure to set up your database configurations in `settings.py`.
5. Run `python manage.py migrate` to apply migrations.
6. Start the development server with `python manage.py runserver`.
7. Visit `http://127.0.0.1:8000/` in your browser to access the application.

## Usage
- On the homepage, you'll see a list of all employees.
- You can use the 'Add Employee' button to navigate to the form for adding a new employee.
- Click on 'Edit' next to any employee to modify their details.
- Use the search bar to find employees by name or ID.

## Directory Structure
-employee_dir: Main application directory containing models, views, templates, and static/media files.
-project2: Main project configuration directory.
-media: Directory for storing uploaded images.
-static: Directory for static files like stylesheets, scripts, and other assets.


## Disclaimer
All characters, images, and related content from "Silicon Valley" are trademarks of HBO and are used here for educational and demonstrative purposes only. This project is not affiliated with or endorsed by HBO, and the developer claims no ownership over any copyrighted content.


