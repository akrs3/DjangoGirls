print('Hello, Django Girls!')

estagiarios = ['Anne', 'Rubson', 'Mateus']
print(estagiarios)

design = {'nome' : 'Raira', 'idade': '22'}
len(design)

design.pop('idade')
design['sobrenome'] = 'Izabel'
print(design)

name = 'Kelly'

if name == 'Anne':
    print('3 é maior que 2')
elif name == 'Kelly':
    print('Hello Kelly')
else:
    print('Onde está Kelly')

def hi(name):
    if name == 'Anne':
        print('Tudo apaixonada')
    elif name == 'Kelly':
        print('É o Amor')
    else:
        print('I love you')

hi("Raira")

def ho(name):
    print('Hi ' + name + '!')

ho("Lidiane")

devs = ['Lidi', 'Raira', 'Anne', 'Esdras', 'Rubson', 'Mateus']

for name in devs:
    ho(name)
    print('Next dev')

for i in range(1,6):
    print(i)
