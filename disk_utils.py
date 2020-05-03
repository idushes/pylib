from os import listdir, system
from os.path import join, isdir

# получить список файлов по маске
def get_file_list(dir_path, mask = ".flac", absolute=False):
    if isdir(dir_path):
        files = listdir(dir_path)
        files = filter(lambda item: mask in item, files)
        if absolute:
            def abs_path(name): return join(dir_path, name)
            map_iterator = map(abs_path, list(files))
            return list(map_iterator)
        return list(files)
    else:
        print('path is not a dir !!! -> ', dir_path)
        return []

# получить список файлов по маске включая поддириктории (один уровеньв)
def get_full_file_list(dir_path, mask = ".flac", absolute=False):
    some_files = get_file_list(dir_path, mask=mask, absolute=absolute)
    folders = get_label_list(dir_path, absolute=True)
    for folder in folders:
        some_files_in_folder = get_file_list(folder, mask=mask, absolute=absolute)
        some_files = some_files + some_files_in_folder
    return some_files

# получить список папок в дириктории
def get_label_list(dir_path, absolute=False):
    if isdir(dir_path):
        labels = []
        for label in listdir(dir_path):
            if label in ['', '.DS_Store']: continue
            if isdir(join(dir_path, label)): labels.append(label)
        if absolute:
            def abs_path(name): return join(dir_path, name)
            map_iterator = map(abs_path, labels)
            return list(map_iterator)
        return labels
    else:
        print('path is not a dir !!! -> ', dir_path)
        return []

# отчистить дирикторию
def clean_dir(dir_path):
    if isdir(dir_path):
        system(f'rm -r {dir_path} && mkdir {dir_path}')
    else:
        system(f'mkdir {dir_path}')
