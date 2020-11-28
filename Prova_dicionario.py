answer = 's'
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 410+10',#Esquerda fica a key, direita a value
        'respostas': {'A': '420', 'B': '250', 'C': '153', 'D': '419', },
        'resposta_certa': 'a',
    },
    'Pergunta 2': {
        'pergunta': 'Complete o nome Stephen ...',
        'respostas': {'A': 'Joe', 'B': 'Jack', 'C': 'King', 'D': 'Reaper', },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quem foi "Jack, The Reaper" ',
        'respostas': {'A': 'Um historiador', 'B': 'Um cantor', 'C': 'Um escritor', 'D': 'Um serial Killer', },
        'resposta_certa': 'd',
    },
    'Pergunta 4': {
        'pergunta': 'Qual o sobrenome do casal que protagonizam os filmes "Invocação do mal" ',
        'respostas': {'A': 'Hill', 'B': 'Bill', 'C': 'Warren', 'D': 'Bing', },
        'resposta_certa': 'c',
    },
    'Pergunta 5': {
        'pergunta': 'A Terra é plana? ?',
        'respostas': {'A': 'Sim', 'B': 'Não', 'C': 'Talvez', 'D': 'Não sei', },
        'resposta_certa': 'b',
    },
}
print()

while answer != 'n':

    respostas_certas = 0
    for pk, pv in perguntas.items():
        print(f'{pk}: {pv["pergunta"]}')

        print('Escolha a opção correta: ')
        for rk, rv in pv['respostas'].items():
            print(f'[{rk}]: {rv}')

        resposta_usuario = input('Sua resposta: ')

        if resposta_usuario == pv['resposta_certa']:
            print(f'Resposta correta')
            respostas_certas += 1
        else:
            respostas_certas += 0
            for rcv in pv['resposta_certa']:
                print(f'A opção correta é: {rcv}')

        print()

    qtde_perguntas = len(perguntas)
    porcentagem_acerto = respostas_certas / qtde_perguntas * 100

    print(f'Você acertou {respostas_certas} respostas.')
    print(f'Sua porcertagem de acerto foi de {porcentagem_acerto}%')
    print()

    answer = input('Você quer fazer de novo ? (s/n)')
    print()
