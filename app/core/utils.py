import os
from datetime import datetime

from core.config import clasif_folders, charts_folders, results_dir


#Using pathlib
def create_folder():
    try:
        path = results_dir / datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
        path.mkdir()
        for c in clasif_folders:
            clasif_path = path / c
            clasif_path.mkdir()
            for ch in charts_folders:
                charts_path = clasif_path / ch
                charts_path.mkdir()
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        return path

'''
def create_folder():
    #por ahora lo hago con datetime now,
    #deberia cambiarle el nombre
    xpath = '/results/' + datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
    #FOLDER_PATH = os.getcwd()
    FOLDER_PATH = '/Users/eche/Desktop/budget/'
    path = FOLDER_PATH + xpath
    try:
        os.mkdir(path)
        for f in folders:
            p = path + '/' + f
            os.mkdir(p)
            for fol in folders2:
                pp = p + '/' + fol
                os.mkdir(pp)

    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        return xpath

'''
if __name__ == '__main__':
    create_folder()
