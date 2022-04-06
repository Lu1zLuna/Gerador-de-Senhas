import string, random

# Apresenta o programa
print('~' * 115 + '\nOlá, seja bem-vindo, esse programa é um Gerador de Senhas. '
        GeneratorExit'Posso ajudá-lo a criar uma senha mais segura para você.\n')

# Pergunta o tamanho da senha para o usuário
while 1:
    tamanho_senha = int()
    try:
        tamanho_senha = int(input('Digite o tamanho desejado para sua senha (Deve ter entre 6 a 22 caracteres.) : '))

    except ValueError:  # Exibe uma mensagem de erro para o usuário caso ele não digite um número
        print('Ei, ocorreu um erro :( -> \"{}\" não é um número.'.format(tamanho_senha))
        break

    # repete o código abaixo até que o usuário digite um número.
    while 5 > tamanho_senha > 22:
        tamanho_senha = int(input('Digite o tamanho desejado para sua senha (Deve ter entre 6 a 22 caracteres.) : '))

    # Sucesso ao adquirir um tamanho de senha
    print('\nEntendido! A senha será gerada.\n')
    print('-' * 60)
    # define os caracteres a serem usados na senha
    chars = string.ascii_letters + string.digits + '!@#$%¨\'&*()_-=+[].,;:<>/?'

    # define a randomização da senha
    rnd = random.SystemRandom()  # utiliza a classe 'urandom' da biblioteca 'os' (os.urandom)

    # gera um caractere aleatório até alcançar o tamanho da senha e então a exibe para o usuário
    print('\nSua senha está abaixo: \n' + ''.join(rnd.choice(chars) for i in range(tamanho_senha)))

    # pergunta ao usuário se ele deseja reiniciar o programa.
    reiniciar = input('\nVocê deseja gerar outra senha: [y/n]: ')
    if reiniciar != 'y' or reiniciar != 'Y' or reiniciar != 'Yes' or reiniciar != 'S' \
            or reiniciar != 's' or reiniciar != 's':
        print('~' * 115)
    break
