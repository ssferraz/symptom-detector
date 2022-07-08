from lib.interface import *
from lib.arquivo import *
from time import sleep
from typing import List
import sys

arq = 'users.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menuInicial(['Logar', 'Cadastrar Usuário', 'Sair do sistema'])

    if resposta == 1:
        cabecalho('LOGIN')
        usuario = str(input('Usuário: '))
        senha = str(input('Senha: '))
        logado = logar(arq, usuario, senha)
        if logado:
            while True:
                resposta = menuPrincipal(['Detectar Sintomas', 'Como se prevenir da COVID-19', 'Deslogar', 'Sair do sistema'])
                if resposta == 1:
                    cabecalho('DETECTAÇÃO DE SINTOMAS')
                    detectarSintomas()
                elif resposta == 2:
                    cabecalho('INFORMAÇÕES DE PREVENÇÃO COVID-19')
                    infos: List[str] = [
                        'lavar as mãos frequentemente com água e sabonete por pelo menos 20 segundos',
                        'evitar tocar nos olhos, nariz e boca com as mãos não lavadas',
                        'evitar contato próximo de pessoas doentes (1 metro de distância)',
                        'ficar em casa quando estiver doente',
                        'cobrir boca e nariz com um lenço de papel, ao tossir ou espirrar. Após, jogar no lixo e higienizar as mãos;',
                        'evitar o compartilhamento de copos, pratos ou outros objetos de uso pessoal',
                        'limpar e desinfetar objetos e superfícies que sejam tocadas com freqüência por várias pessoas',
                        'procurar atendimento médico de imediato, caso possua sintomas E contato com pessoas infectadas.'
                    ]
                    print(infoCovid(infos))
                elif resposta == 3:
                    break
                elif resposta == 4:
                    cabecalho('Saindo do sistema... Até logo!')
                    sys.exit(0)
                else:
                    print('ERRO! Digite uma opção válida!')
            sleep(2)
        else:
            print('Login inválido. Tente novamente!')

    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        usuario = str(input('Usuário: '))
        senha = str(input('Senha: '))  # getpass.getpass(prompt='Digite sua Senha: ', stream=None)
        cadastrarUsuario(arq, nome, usuario, senha)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)
