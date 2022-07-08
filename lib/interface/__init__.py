import bcrypt
from typing import List
from time import sleep

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def encriptaSenha(password):
    hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    return hash.decode()


def validaSenha(self, password):
    return bcrypt.checkpw(self.encode('utf8'), password.encode('utf8'))


def menuInicial(lista):
    cabecalho('MENU INICIAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc


def menuPrincipal(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc

def detectarSintomas():
    sintomas = []

    febre = str(input('Sente febre? [S/N] ').strip().upper()[0])
    while febre not in 'SN':
        febre = str(input('Dados inválidos. Por favor, informe se teve febre: ').strip().upper()[0])
    if febre in 'S':
        sintomas.append('febre')

    tosse = str(input('Sente tosse? [S/N] ').strip().upper()[0])
    while tosse not in 'SN':
        tosse = str(input('Dados inválidos. Por favor, informe se teve tosse: ').strip().upper()[0])
    if tosse in 'S':
        sintomas.append('tosse')

    coriza = str(input('Sente coriza? [S/N] ').strip().upper()[0])
    while coriza not in 'SN':
        coriza = str(input('Dados inválidos. Por favor, informe se teve coriza: ').strip().upper()[0])
    if coriza in 'S':
        sintomas.append('coriza')

    dorGarganta = str(input('Sente dor de gargana? [S/N] ').strip().upper()[0])
    while dorGarganta not in 'SN':
        dorGarganta = str(input('Dados inválidos. Por favor, informe se teve dor de garganta: ').strip().upper()[0])
    if dorGarganta in 'S':
        sintomas.append('dor de garganta')

    difResp = str(input('Sente dificuldade de respirar? [S/N] ').strip().upper()[0])
    while difResp not in 'SN':
        difResp = str(input('Dados inválidos. Por favor, informe se teve dificuldade de respirar: ').strip().upper()[0])
    if difResp in 'S':
        sintomas.append('dificuldade de respirar')

    contato = str(input('Teve histórico de contato próximo de caso suspeito para COVID-19 nos últimos 14 dias? [S/N] ').strip().upper()[0])
    while contato not in 'SN':
        contato = str(input('Dados inválidos. Por favor, informe se teve contato próximo de caso suspeito: ').strip().upper()[0])
    if contato in 'S':
        sintomas.append('contato')

    if len(sintomas) >= 1 and 'contato' in sintomas:
        cabecalho('É provável que você ESTEJA infectado pelo \nCOVID-19, procure um atendimento médico.')
    else:
        cabecalho('É provável que você NÃO esteja infectado \npelo COVID-19. Mantenha as condutas de precaução \ne '
                'prevenção!')


def infoCovid(infos: List[str], index: int = 0):
    if len(infos) <= index:
        return ''
    info = infos[index]
    print((index+1), info)
    sleep(5)
    index += 1
    return infoCovid(infos, index)