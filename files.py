import os
import collections
print('cwd-',os.getcwd())
extlst = open("extlist.txt").readlines()
extlst = [x.strip() for x in extlst]


def extract(name,lst=[]):#достает все файлы из папки(в том числе и из дочерних папок, и из их дочерних папок тоже и т.д)
    for i in range(len(name)-2):
        if name[i]!='/' and name[i+1]=='/' and name[i+2]!='/':
            name  = name.replace('/','//')
            break
    files = os.listdir(name)
    for x in files:
        os.chdir(name)
        f = x.split('.')
        if len(f)>1 and '.'+f[-1] in extlst:
            lst+=[os.path.abspath(x)]
        else:
            try:lst+=extract(os.path.abspath(x),lst)
            except:lst+=[os.path.abspath(x)]
    return [x for x in set(lst) if '.' in x.split('\\')[-1]]


def extdict(lst):#создает словарь, где ключами являются расширения файлов
    ext_dict = collections.defaultdict(set)
    for file in lst:ext_dict['.'+file.split('.')[-1]]|={file}
    return dict(ext_dict)


def cout_extdict(exst,curr_ext = None):#красиво вывести словарь extdict
    if type(exst) != dict:
        print('Error:Not a dict type')
        return 0

    if curr_ext == None:
        for key, val in exst.items():
                print(key + f' {len(val)} files') if len(val) > 1 else key + f'{len(val)} file'
                for x in val: print('    ' + x)
    else:
        key = '.' + curr_ext.replace('.', '')
        val = exst[key]

        if key not in exst:
            print('Nothing there')
            return 0

        print(key + f' {len(val)} files') if len(val) > 1 else key + f'{len(val)} file'
        for x in val: print('    ' + x)


def search(name, folder):#искать что-то в папке
    lst = []
    if type(folder) == str:
        folder = extract(folder)
    for x in folder:
        if name in x:
            lst += [x]

    if len(lst)==0:return None
    if len(lst)==1:return lst[0]
    return lst









