"""
Perguntas e respostas
"""

print('\nQuestionario:\n')

questionario = {
    'Pergunta 1': {
        'pergunta': 'Qual o nome dessa linguagem de programação?',
        'opcoes_resposta': {
            'a': 'Java.',
            'b': 'Python.',
            'c': 'JavaScript.'
        },
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Qual o nome desse editor de código?',
        'opcoes_resposta': {
            'a': 'PyCharm.',
            'b': 'NetBeans.',
            'c': 'VS Code.'
        },
        'resposta_certa': 'a'
    },
    'Pergunta 3': {
        'pergunta': 'Qual versão do Python utilizada?',
        'opcoes_resposta': {
            'a': 'Python 1.',
            'b': 'Python 2.',
            'c': 'Python 3.'
        },
        'resposta_certa': 'c'
    },
    'Pergunta 4': {
        'pergunta': 'Qual o sistema operacional usado?',
        'opcoes_resposta': {
            'a': 'Windows.',
            'b': 'Linux.',
            'c': 'macOS.'
        },
        'resposta_certa': 'a'
    },
    'Pergunta 5': {
        'pergunta': 'É utilizado Git e GitHub?',
        'opcoes_resposta': {
            'a': 'Apenas o Git.',
            'b': 'Apenas o GitHub.',
            'c': 'Ambos são utilizados.'
        },
        'resposta_certa': 'c'
    },
}

nota = 0
for chave_perguntas, valor_perguntas in questionario.items():
    print(f'{chave_perguntas}: {valor_perguntas["pergunta"]}')

    print('\nOpções de resposta:')
    for chave_respostas, valor_respostas in valor_perguntas['opcoes_resposta'].items():
        print(f'{chave_respostas}) : {valor_respostas}')

    resposta_usuario = input('\nSua resposta: ')

    if resposta_usuario == valor_perguntas['resposta_certa']:
        print('Resposta correta\n')
        nota += 1
    else:
        print('Resposta errada\n')

quantidade_perguntas = len(questionario)
porcentagem_nota = nota / quantidade_perguntas * 100

print(f'Você acertou {nota} resostas.')
print(f'Sua porcentagem de acerto de {porcentagem_nota}%.')
