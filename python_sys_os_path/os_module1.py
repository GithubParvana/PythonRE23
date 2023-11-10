import os

print('current directory', os.getcwd())

# os.mkdir('newfolder')




if not os.path.isdir('newfolder'):
    print('Folder movcud deyil, folder yaradilir...')
    os.mkdir('newfolder')
else:
    print('Folder movcuddur, folder adi deyisdirilir...')

    try:
        os.rename('newfolder', 'changed_folder')
    except FileExistsError:
        print('The name you wanted to change is already exist. Changing new name ...')
        if os.path.isdir('changed_folder'):
            print('changed_folder artiq movcuddur, yeni adla evez olunur...')
            os.rename('changed_folder', 'folder4')
    
    


print(os.listdir())
