import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# 邮箱发信地址（SMTP服务器） - SMTP server host/domain name of sender
EMAIL_HOST = 'smtp.163.com'
# 邮箱发信端口（SMTP服务器端口） - SMTP server port of sender
EMAIL_PORT = 25
# 邮箱账号 - email of sender
EMAIL_USER = '***@163.com'
# 邮箱密码或授权码（作为第三方登录） - email password or authentication code
EMAIL_PASSWORD = '***'
# 收信人地址 - email of receiver
EMAIL_RECEIVER = "***@qq.com"


def send_email(html_message):
    # set up the SMTP server
    s = smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT)
    s.starttls()
    s.login(EMAIL_USER, EMAIL_PASSWORD)
    msg = MIMEMultipart() # create a message
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject']="Notice"
    msg.attach(MIMEText(html_message, 'html'))
    s.send_message(msg)
    del msg
    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == "__main__":
    send_email('<strong>Hey,</strong><br>&nbsp;&nbsp;Your program has started!')
