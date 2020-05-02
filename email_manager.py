import config
import smtplib


def create_email(previousRates, date, todaysRate):
    if len(previousRates) == 0:
        email_data = f"On {date} the {todaysRate[0]} exchange rate is {todaysRate[1]} to the pound."
    else:
        email_data = (f"Todays {todaysRate[0]} exchange rate is {todaysRate[1]} to the pound.\nThe maximum so far is: {float(max(previousRates))}\nThe minimum so far is: {float(min(previousRates))}")
        if float(todaysRate[1]) > float(max(previousRates)):
            email_data += "\nThis is the highest rate so far, you may want to buy today"
        elif float(todaysRate[1]) == float(max(previousRates)):
            email_data += "\nThis is the joint highest so far, you may want to buy today"
    email_subject = f"{todaysRate[0]} exchange rate - {date}"
    send_email(email_subject, email_data)


def send_email(subject, email_data):
    senders_address = ("senders address")
    receiver_address = ("recipients address")
    # create smtp object. This creates a connection to the smtp mail server. Use this to call methods to login and send emails
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    # must call this to establish connection to server. First item in tuple is 250. Success.
    smtp_obj.ehlo()
    # You are connecting to port 587. Using standard TLS encryption. So need to enable encryption. 220 = success:
    smtp_obj.starttls()
    # log in
    smtp_obj.login(config.email_address, config.password)

    # send email
    smtp_obj.sendmail(my_address, receiver_address,
                     f"Subject: {subject}\n{email_data}\nMany Thanks")
    # logout
    smtp_obj.quit()
