import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import os

# Contor global pentru imagini
image_counter = 0

def capture_image():
    global image_counter
    file_path = f"/home/admin/Desktop/image{image_counter}.jpg"
    bash_command = f"libcamera-still -o {file_path}"
    try:
        subprocess.run(bash_command, shell=True, check=True)
        print(f"Image saved as {file_path}")
        image_counter += 1
        send_email(file_path)  # Apeleaz? func?ia de trimitere a e-mailului cu calea fi?ierului
    except subprocess.CalledProcessError as e:
        print(f"Failed to capture image: {e}")

def send_email(file_path):
    # Configura?ii e-mail
    sender_email = "smart.home777@yahoo.com"
    receiver_email = "alinsokolov.it@gmail.com"
    subject = "Last guest"
    body = "Vezi cine a trecut pe la tine si te-a cautat"
    password = "@dmin777admin"  # Parola ta de Yahoo

    print("Configura?ii e-mail setate")

    # Crearea mesajului e-mail
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    print("Mesaj e-mail creat")

    # Ata?area imaginii
    try:
        with open(file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(file_path)}",
            )
            msg.attach(part)
        print(f"Attachment {file_path} added successfully.")
    except Exception as e:
        print(f"Failed to attach file: {e}")
        return

    # Trimiterea e-mailului
    try:
        with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as server:
            print("Conectare la serverul SMTP")
            server.set_debuglevel(1)  # Set debug level to see detailed output
            server.ehlo()
            print("Comanda EHLO trimis?")
            server.login(sender_email, password)
            print("Autentificare reu?it?")
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Testarea func?iei
capture_image()
