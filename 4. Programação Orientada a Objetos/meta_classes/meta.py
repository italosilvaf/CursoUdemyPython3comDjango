"""
EM PYTHON TUDO É UM OBJETO: incluindo classes.
Metaclasses são as "classes" que criam classes.
type é uma metaclasses (!!!???)
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo')
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'Valor A'


class B(A):
    attr_classe = 'Valor B'


class C(B):
    attr_classe = 'Valor C'


b = B()
print(b.attr_classe)

print('-' * 100)


class ClasseMEnsagemPai:
    nome = 'Teste'


A = type(
    'ClasseMensagemFilha',
    (ClasseMEnsagemPai,),
    {'mensagem': 'Olá, tudo bem? '}
)

a = A()
print(a.mensagem)
print(type(a))
