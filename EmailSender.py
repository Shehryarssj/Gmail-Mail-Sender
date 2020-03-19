import smtplib, time
from validate_email import validate_email
from email.message import EmailMessage



def login(mail, passwrd):
    try:
        smtp.login(mail, passwrd)
        print("Logged in successfully")
    except Exception:
        print("Invalid credentials, couldn't login")
        return 0

def loginCheck(check):
    while check == 0:
        tryAgain = input("Enter y to try login again or n to exit: ")
        if tryAgain == "y":
            email = input("Enter email address: ").strip()
            password = input("Enter password: ").strip()
            check = login(email, password)
        else:
            print("Bye")
            time.sleep(3)
            quit()

def check_recipent():
    r = input("Enter email address of recipent: ").strip()
    recipent_exist = validate_email(r)
    while recipent_exist == False:
        r = input("Enter a valid email address of recipent: ").strip()
        recipent_exist = validate_email(r)
    return r

def send(message):
    smtp.send_message(message)
    print("Email sent to "+recipent)
try:
    print("Starting Email Service")
    z = smtplib.SMTP_SSL("smtp.gmail.com", 465)
except Exception:
    print("Error Occured\nCouldnt connect to GMAIL servers")
    time.sleep(3)
    quit()

with z as smtp:
    print("Connected to GMAIL servers")
    email = input("Enter email address: ").strip()
    password = input("Enter password: ").strip()
    check = login(email, password)
    loginCheck(check)
    recipent = check_recipent()
    subject = input("Enter subject: ").strip()
    body = input("Enter body of mail: ").strip()
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email
    msg["To"] = recipent
    msg.set_content(body)
    attatchments = int(input("Enter number of attatchments: ").strip())
    if attatchments != 0:
        for each in range(0,attatchments):
            path = path = input(f"Enter file path for attachment no.{each+1}: ").strip()
            with open(path, "rb") as fptr:
                data = fptr.read()
                ext = input(f"Enter file name with extension for attatchment no.{each+1}: ").strip()
                msg.add_attachment(data, maintype = "bla-bla", subtype = "bla-bla", filename = ext)
            print("\n\n\n")
    try:
        send(msg)
        forward = input("Want to forward this mail to other addresses? (y/n): ").strip()
        if forward.lower() == "y":
            recipent = check_recipent()
            while recipent != "":
                msg = EmailMessage()
                msg["To"] = recipent
                msg["Subject"] = subject
                msg["From"] = email
                msg.set_content(body)
                msg.add_attachment(data, maintype = "bla-bla", subtype = "bla-bla", filename = ext)
                send(msg)
                forward = input("Want to forward this mail to other addresses? (y/n): ").strip()
                if forward.lower() == "y":
                    recipent = check_recipent()
                else:
                    break
    except Exception as e:
        print(e)

        print("Couldn't send email")
        time.sleep(3)
        quit()

    print("bye")
    time.sleep(3)


