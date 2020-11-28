answer = 's'
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 410+10',
        'respostas': {'a': '420', 'b': '250', 'c': '153', 'd': '419', },
        'resposta_certa': 'a',
    },
    'Pergunta 2': {
        'pergunta': 'Complete o nome Stephen ...',
        'respostas': {'a': 'Joe', 'b': 'Jack', 'c': 'King', 'd': 'Reaper', },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quem foi "Jack, The Reaper" ',
        'respostas': {'a': 'Um historiador', 'b': 'Um cantor', 'c': 'Um escritor', 'd': 'Um serial Killer', },
        'resposta_certa': 'd',
    },
    'Pergunta 4': {
        'pergunta': 'Qual o sobrenome do casal que protagonizam os filmes "Invocação do mal" ',
        'respostas': {'a': 'Hill', 'b': 'Bill', 'c': 'Warren', 'd': 'Bing', },
        'resposta_certa': 'c',
    },
    'Pergunta 5': {
        'pergunta': 'A Terra é plana? ?',
        'respostas': {'a': 'Sim', 'b': 'Não', 'c': 'Gente?', 'd': 'Não sei', },
        'resposta_certa': 'b',
    },
}
print()

while answer != 'n':

    respostas_certas = 0
    for pk,pv in perguntas.items():
        print (f'{pk}: {pv["pergunta"]}')

        print('Escolha a opção correta: ')
        for rk,rv in pv['respostas'].items():
            print(f'[{rk}]: {rv}')

        resposta_usuario = input('Sua resposta: ')

        if resposta_usuario == pv['resposta_certa']:
            respostas_certas += 1
        else:
            respostas_certas += 0

        print()

    qtde_perguntas = len(perguntas)
    porcentagem_acerto =  respostas_certas / qtde_perguntas * 100

    print(f'Você acertou {respostas_certas} respostas.')
    print(f'Sua porcertagem de acerto foi de {porcentagem_acerto}%')
    print()

    answer = input ('Você quer fazer de novo ? (s/n)')
    print()

