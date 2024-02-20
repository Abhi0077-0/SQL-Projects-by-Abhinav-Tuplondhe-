import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
# import base64

from dotenv import load_dotenv


PORT = 587
email_server = "smtp.gmail.com"

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables

sender_email = "now.official1@gmail.com"
passkey = "oonbdppqpysalzpp"


def send_email(subject, receiver_email, name, company_name):
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Abhinav Tuplondhe", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Dear {name},

        I hope this email finds you well. I am writing to express my interest in the Data Analyst position advertised by {company_name}. 
        With a background in [mention relevant education or experience, if any], I am excited about the opportunity to contribute to your team and utilize my skills in data analysis.

        I have attached my resume for your review, which provides further detail on my qualifications and experiences. 
        I am particularly drawn to this position at {company_name} because of [mention specific reasons, such as company culture, projects, or values that align with your own].

        I am confident that my analytical skills, attention to detail, and passion for problem-solving make me a strong candidate for this role. 
        I am eager to discuss how my background, skills, and experiences align with the needs of your team.

        Thank you for considering my application. I look forward to the possibility of discussing how I can contribute to {company_name} as a Data Analyst.

        Warm regards,
        Abhinav Tuplondhe
        abhinavtuplondhe77@gmail.com
        +91 9975843832 """

    )

    with smtplib.SMTP(email_server, PORT) as server:
        server.starttls()

        # encoded_password = base64.b64encode(passkey.encode()).decode()

        server.login(sender_email, passkey)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    send_email(
        subject="Hello buddy",
        name="Abhinav",
        receiver_email="abhinavtuplondhe77@gmail.com",
        company_name="Google"
    )
