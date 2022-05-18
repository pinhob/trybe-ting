import sys
from os.path import isfile


def txt_importer(path_file):
    # com ajuda do túlio na monitoria
    if not isfile(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")

    with open(path_file) as file:
        return file.read().splitlines()
