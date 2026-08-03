# Smart Resume Builder

#### Video Demo: https://www.youtube.com/watch?v=UpoCshCAWDA

#### Description:

**Smart Resume Builder** is a web-based application developed as my final project for CS50x. The purpose of this project is to simplify the process of creating a professional resume. Many students and beginners find it difficult to design a clean and organized resume, especially if they have little experience with formatting or design tools. This application provides a simple interface where users can enter their personal information, education, skills, work experience, and other details into an easy-to-use form. Once the form is submitted, the application automatically generates a well-structured resume that is ready to print.

The project was developed using **Python with Flask** for the backend and **HTML, CSS, and JavaScript** for the frontend. Flask is responsible for receiving the data entered by the user and rendering it into a resume template. The frontend focuses on providing a clean, responsive, and user-friendly interface.

## Project Features

The application includes several features that make the resume creation process simple and efficient.

* A modern and clean home page that introduces the application.
* A resume form where users can enter their personal information.
* Automatic generation of a professional resume after submitting the form.
* A print button that allows the user to print the generated resume directly from the browser.
* Basic form validation using HTML required fields.
* JavaScript functions that improve the user experience, including confirmation messages, alerts, and printing functionality.
* Responsive design that works on different screen sizes.

## Project Structure

The project is organized into multiple files and folders, each with a specific responsibility.

### app.py

This is the main Flask application. It defines the application routes, receives the submitted form data, and sends the information to the resume template. It acts as the connection between the frontend and the backend.

### templates/home.html

This file contains the landing page of the application. It welcomes users and provides navigation to begin creating a resume.

### templates/resume_form.html

This page contains the form where users enter their personal information, including their name, contact information, education, skills, and work experience.

### templates/resume.html

This template displays the completed resume using the information submitted by the user. Flask passes the entered values to this template so they appear in the correct sections of the resume.

### static/css/style.css

This stylesheet controls the appearance of the entire application. It is responsible for colors, spacing, typography, responsive layout, buttons, forms, and the resume design itself.

### static/js/script.js

This JavaScript file provides interactive functionality such as displaying alerts, confirming form reset actions, and printing the generated resume.

### static/images/

This folder contains screenshots used inside the GitHub repository to demonstrate the application's interface.

## Design Choices

While developing this project, I wanted the application to remain simple and easy to use. Instead of requiring users to learn complicated design software, they only need to fill out a form and immediately receive a formatted resume.

I chose **Flask** because it is lightweight, beginner-friendly, and integrates very well with HTML templates through Jinja. Since the application does not require user authentication or a database, Flask provides exactly the level of complexity needed without adding unnecessary overhead.

For the frontend, I used plain HTML, CSS, and JavaScript instead of frameworks. This decision helped me strengthen the core web development skills that I learned throughout CS50. It also keeps the project lightweight and easy to understand.

The project currently does not store resumes in a database. Instead, the entered information exists only during the current session and is immediately rendered into the resume template. This design keeps the application simple while still demonstrating the integration between frontend forms and backend processing.

## Challenges

One of the biggest challenges during development was passing user input from the HTML form to Flask and then displaying it correctly inside the resume template. Another challenge was designing a layout that looks clean both on screen and when printed.

I also spent time improving the CSS so that the generated resume appears organized and readable without requiring additional formatting by the user.

## Future Improvements

Although the current application successfully generates resumes, there are several improvements that could be added in future versions.

Possible future features include:

* Multiple professional resume templates.
* Exporting resumes directly as PDF files.
* Saving resumes in an SQLite database.
* User accounts and authentication.
* Uploading a profile photo.
* Editing previously created resumes.
* Downloading resumes in different styles and formats.
* More advanced input validation.

## How to Run the Project

1. Clone the repository.

```bash
git clone https://github.com/your-username/ResumeGen.git
```

2. Open the project folder.

```bash
cd ResumeGen
```

3. Install Flask.

```bash
pip install flask
```

4. Run the application.

```bash
python app.py
```

5. Open your browser and visit:

```
http://127.0.0.1:5000
```

## Technologies Used

* Python
* Flask
* HTML5
* CSS3
* JavaScript

## AI Acknowledgment

During the development of this project, I used AI tools, including ChatGPT, as a learning assistant to help explain concepts, debug errors, and improve documentation. All design decisions, implementation, testing, and final integration were completed by me.

## Author

**Hasnaa Taher**

Faculty of Computers and Artificial Intelligence

This project was developed as the final project for **CS50x: Introduction to Computer Science**.
