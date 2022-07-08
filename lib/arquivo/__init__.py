from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('USUÁRIOS CADASTRADOS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'Nome: {dado[0]} Usuário: {dado[1]} Senha: {dado[2]}')
    finally:
        a.close()


def logar(arq, usuario, senha):
    try:
        a = open(arq, 'r')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            if dado[1] == usuario and validaSenha(senha, dado[2]):
                print(f'Login realizado com sucesso! Bem-vindo {dado[0]}!')
                return True
        return False


def cadastrarUsuario(arq, nome='desconhecido', usuario='desconhecido', senha='desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{usuario};{encriptaSenha(senha)}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
