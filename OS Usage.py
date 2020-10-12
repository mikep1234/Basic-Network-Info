import os

os.system('cmd /c  netsh wlan show profiles > hello.txt')

Network_List = []

for elem in (open('hello.txt', 'r')):
    if elem.startswith('    All User Profile'):
        Network_List.append(str(elem[elem.index(':') + 2: len(elem) - 1]))

Network_Dictionary = {}

for network in Network_List:
    os.system('cmd /c netsh wlan show profiles ' + network + ' key = clear > hello.txt')
    for elem in open('hello.txt', 'r'):
        if elem.startswith('    Key Content'):
            Network_Dictionary[network] = str(elem[elem.index(':') + 1: len(elem) - 1])

for network, password in Network_Dictionary.items():
    print("=" * 30)
    print(network + ": " + password)