# Flask Email Sender

This Flask application allows you to send emails through a simple web interface. It uses the Flask web framework, and emails are sent via Gmail SMTP. Below is a brief overview of the project:

## Getting Started

### Prerequisites

- Python installed on your machine.
- Flask and required dependencies installed. You can install them using the following command:

    ```bash
    pip install flask
    ```

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flask-email-sender.git
    cd flask-email-sender
    ```

2. Run the application:

    ```bash
    python app.py
    ```

3. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

1. Access the web interface by visiting [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
2. Fill out the email sender, receiver, subject, and body fields.
3. Click the "Send Email" button to send the email.

## Configuration

In the `app.py` file, find the `send_email` function. Replace `'your_password'` with your actual Gmail password. Note: It's recommended to use an application-specific password instead of your main Gmail password.

```python
smtp.login(email_sender, 'your_password')
```

## Important Note

- This application uses Gmail's SMTP server. Make sure to enable "Less secure app access" in your Gmail account settings.
- For enhanced security, consider using an application-specific password for SMTP authentication.

## Contributing

Feel free to contribute by submitting issues or pull requests.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Acknowledgments

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Python Email Message Library: [https://docs.python.org/3/library/email.message.html](https://docs.python.org/3/library/email.message.html)
- SMTP Library: [https://docs.python.org/3/library/smtplib.html](https://docs.python.org/3/library/smtplib.html)
