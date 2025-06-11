import yagmail

# Gmail credentials
sender_email = "your_email@gmail.com"  # Replace with your Gmail address
sender_password = "your_password"     # Replace with your Gmail app password (not the Gmail password directly!)

# Recipient email(s)
recipients = ["bwhcoi2c@gmail.com",]  # Replace with recipient emails

# Load the HTML Template
with open("email_template.html", "r") as file:
    html_content = file.read()

# Subject of the email
subject = "💀 YOU HAVE BEEN HACKED 💀"

# Send the email
try:
    yag = yagmail.SMTP(user=sender_email, password=sender_password)
    yag.send(to=recipients, subject=subject, contents=html_content)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
