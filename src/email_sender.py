import os
import smtplib
from email.message import EmailMessage
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()


def send_email(to_email, subject, body, resume_path):
    """
    Send a job application email with resume attachment.
    """

    sender_email = os.getenv("GMAIL_EMAIL")
    app_password = os.getenv("GMAIL_APP_PASSWORD")

    # -----------------------------
    # Validate Configuration
    # -----------------------------
    if not sender_email:
        raise ValueError("❌ GMAIL_EMAIL not found in .env")

    if not app_password:
        raise ValueError("❌ GMAIL_APP_PASSWORD not found in .env")

    if not os.path.exists(resume_path):
        raise FileNotFoundError(f"❌ Resume not found: {resume_path}")

    # -----------------------------
    # Create Email
    # -----------------------------
    message = EmailMessage()

    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    message.set_content(body)

    # -----------------------------
    # Attach Resume
    # -----------------------------
    with open(resume_path, "rb") as f:
        message.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(resume_path),
        )

    print("\n" + "=" * 60)
    print("📧 EMAIL DETAILS")
    print("=" * 60)
    print(f"📤 Sender   : {sender_email}")
    print(f"📥 Receiver : {to_email}")
    print(f"📝 Subject  : {subject}")
    print("=" * 60)

    # -----------------------------
    # Send Email
    # -----------------------------
    try:
        print("\n📨 Connecting to Gmail...")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as smtp:

            print("✅ Connected")

            smtp.login(sender_email, app_password)

            print("✅ Login Successful")

            smtp.send_message(message)

            print("✅ Gmail accepted the email.")
            print(f"🕒 Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    except smtplib.SMTPAuthenticationError:
        raise Exception("❌ Gmail authentication failed. Check your App Password.")

    except smtplib.SMTPRecipientsRefused:
        raise Exception(f"❌ Recipient address rejected: {to_email}")

    except smtplib.SMTPException as e:
        raise Exception(f"❌ SMTP Error: {e}")

    except Exception as e:
        raise Exception(f"❌ Unexpected Error: {e}")