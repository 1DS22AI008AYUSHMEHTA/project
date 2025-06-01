import re

email_condition = r"^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+\.\w{2,3}$"
user_email = input("Enter your E-mail - ")

if re.match(email_condition, user_email):
    print("Right E-mail")
else:
    print("Wrong E-mail")
