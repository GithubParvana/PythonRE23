import os

print('current directory', os.getcwd())

if not os.path.isdir('newfolder'):
    print('Folder is not available, it is creating ...')
    os.mkdir('newfolder')


os.chdir('newfolder')

print('current directory', os.getcwd())

open('run.py', 'a').close()

# print(os.listdir())

os.system('python run.py')

# os.system('git init')