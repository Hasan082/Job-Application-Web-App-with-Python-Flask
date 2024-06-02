# Job Application Web App with Python Flask

This is a simple web application built using Flask that allows users to submit job applications. The application saves the submitted data to a SQLite database and sends a confirmation email to the applicant.

## Features

- Form submission for job applications
- Data storage in a SQLite database
- Sending confirmation emails using Flask-Mail

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have Python 3.x installed.
- You have installed the required Python packages. (See Installation section)

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd job-application-web-app
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install Flask Flask-SQLAlchemy Flask-Mail
    ```

## Configuration

1. **Configure your email settings:**

    Open `app.py` and configure the email settings with your own email credentials:

    ```python
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = "your-email@gmail.com"
    app.config["MAIL_PASSWORD"] = "your-app-password"
    ```

    Make sure to use an app-specific password if two-factor authentication is enabled for your Gmail account.

2. **Set the secret key:**

    The secret key is used by Flask to encrypt session data. You can set it to any random string:

    ```python
    app.config["SECRET_KEY"] = "jobApplication"
    ```

## Running the Application

1. **Initialize the database:**

    Before running the application, you need to create the database. Run the following commands:

    ```bash
    export FLASK_APP=app
    flask shell
    from app import db
    db.create_all()
    exit()
    ```

2. **Run the application:**

    ```bash
    python app.py
    ```

    The application will be accessible at `http://127.0.0.1:5000`.

## Project Structure

```
job-application-web-app/
│
├── app.py                   # Main application file
├── database.db              # SQLite database file (generated after running the app)
├── templates/
│   └── index.html           # HTML template for the job application form
├── static/
│   └── css/
│       └── style.css        # Custom CSS file
└── venv/                    # Virtual environment directory
```

## Usage

1. Navigate to the application URL in your web browser.
2. Fill in the job application form with the required details.
3. Submit the form.
4. You will receive a confirmation email containing the details of your application.

## Error Handling

- If there are any issues with sending the email, an error message will be displayed on the webpage.

## Contributing

If you want to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is open-source and available under the [MIT License](https://opensource.org/license/mit).

## Contact

If you have any questions, feel free to contact me at [dr.has82@gmail.com](mailto:dr.has82@gmail.com).
