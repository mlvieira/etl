import pandas as pd
import csv
import os
import glob

def import_csv_to_dataframe(path: str, encode='utf-8', separator=';') -> pd.DataFrame:

    if path_exists(path):

        with open(path, newline='', encoding=encode, errors='ignore') as csvfile:
            reader = csv.reader(csvfile, delimiter=separator, dialect='excel')

            info_csv = []
            for i in reader:
                info_csv.append(i)

            return pd.DataFrame(info_csv)

def path_exists(path: str) -> bool:

    if not os.path.exists(path):
        return False
    
    return True

def glob_to_list(path: str, depth = '../') -> list:

    lst_files = []

    if '.' not in path:
        path = depth + path

    for arq in glob.glob(path):
        lst_files.append([os.path.basename(arq), arq])

    return lst_files
        