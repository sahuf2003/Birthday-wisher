import pandas as pd
import datetime as dt
import os,random
import smtplib

my_email = "youremail@gmail.com"
password ="yourpassword"
random_file = random.choice(os.listdir("letter_templates"))
PLACEHOLDER = "[NAME]"
now = dt.datetime.now()
today = now.day
month = now.month
year = now.year
data = pd.read_csv("birthdays.csv")

birthday = data[(data['day'] == today) & (data['month'] == month)]
if birthday.empty:
    print("bruh no birthday")
else:
    namaewa = birthday['name']
    naaaame = namaewa.to_string(index=False)
    print(naaaame)

    email = birthday['email']
    eemail = email.to_string(index=False)
    print(eemail)


    with open(f"letter_templates\{random_file}") as file:
        letter = file.read()
        print(type(letter))
        new_content = letter.replace(PLACEHOLDER,naaaame)

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=eemail,msg=new_content)
