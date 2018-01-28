#!/usr/bin/python3
# /etc/init.d/send_mail_ip.py
### BEGIN INIT INFO
# Provides:          send_mail_ip.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO
#
"""
    @author: MinhHT3
    @brief : urllib
"""
import smtplib
import json
from urllib.request import urlopen, Request
import os
import datetime, time


ip = 'https://ipinfo.io/json'

def get(uri):
    req = Request(uri)
    req.add_header('user-agent', 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36')
    return urlopen(req)

ipres_json = ""
ipres = ""

try:
    ipres_json = json.loads(get(ip).read().decode())
    ipres = get(ip).read().decode()
    print(ipres)
except:
    pass

curr_ip = ""
pre_ip = ""
if (ipres_json != ""):
    curr_ip = ipres_json['ip']

file_name = "./ip_address"

if os.path.exists(file_name):
    with open(file_name, "r") as f:
        pre_ip = f.read()
        f.close()
else:
    with open(file_name, "w") as f:
        if (curr_ip != ""):
            f.write(curr_ip)
        f.close()
print("curr_ip: ", curr_ip)
print("pre_ip: ", pre_ip)

def send_mail(message):
    try:
        ## mail
        sender = 'htm.doc01@gmail.com'
        to = ['hoangtrongminh304@gmail.com']
        subject = 'Test IP'
        body = "test IP"

        email_text = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (sender, ", ".join(to), subject, message)

        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpObj.ehlo()
        smtpObj.login(sender, 'Htmdoc01')
        smtpObj.sendmail(sender, to, email_text)
        smtpObj.close()
        print("Successfully sent email")
    except:
        print("sent email fail")
        pass

# send_mail(ipres)

count = 0
set_time_duration = 60

while 1:
    count += 1
    print("===== hehe.ping ", count)

    try:
        ipres_json = json.loads(get(ip).read().decode())
        curr_ip = ipres_json['ip']
        print(curr_ip)

        if (curr_ip != pre_ip):
            pre_ip = curr_ip
            print("changes ip")
            with open(file_name, "w") as f:
                f.write(curr_ip)
                f.close()
            send_mail("IP address: " + curr_ip)
        else:
            print("same ip")
    except:
        pass

    print("===== Wait %s =====" % set_time_duration)
    time.sleep(set_time_duration)
