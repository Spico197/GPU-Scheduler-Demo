# GPU-Scheduler-Demo
a demo for easy and efficient GPU using

check GPU status every 30 seconds and send an email automatically
when GPU 0 (index 0) memory utilization is less than 50% and 
GPU utilization is less than 10% .

## Installation
```bash
$ python -m pip install gpustat
$ python -m pip install apscheduler
```

## Usage

1. Settings in `send_email.py`
```python
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
```

2. Start script
```bash
$ python scheduler.py
```
