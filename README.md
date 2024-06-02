# Job Application Web App with Python Flask

This is a simple web application built with Flask for submitting job applications. Users can fill out a form with their personal details and submit it. The submitted data is saved in a SQLite database and an email notification is sent to the applicant.

## Features

- Users can fill out a job application form with their personal details.
- Submitted data is stored in a SQLite database.
- Email notification is sent to the applicant after submitting the form.

## Installation

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    ```

2. **Navigate to the project directory:**

    ```sh
    cd Job-Application-Web-App-with-Flask
    ```

3. **Create a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

    ```sh
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```sh
    source venv/bin/activate
    ```

5. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

6. **Create a `.env` file in the project root directory and add the following environment variables:**

    ```plaintext
    SECRET_KEY=your_secret_key
    SQLALCHEMY_DATABASE_URI=sqlite:///database.db
    MAIL_SERVER=smtp.gmail.com
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME=your_email@example.com
    MAIL_PASSWORD=your_email_password
    ```

    Replace `your_secret_key`, `your_email@example.com`, and `your_email_password` with your own values.

7. **Run the Flask app:**

    ```sh
    python app.py
    ```

8. **Access the web application in your browser at `http://127.0.0.1:5000`.**

## Usage

- Open the web application in your browser.
- Fill out the job application form with your details.
- Click the submit button.
- You will receive a confirmation message on the web page.
- Check your email inbox for a confirmation email.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.
