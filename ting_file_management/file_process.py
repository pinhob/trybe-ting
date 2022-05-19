from ting_file_management.file_management import txt_importer
import sys


def search_for_file(path_file, instance):
    file_is_new = True

    if len(instance.queue) >= 1:
        for item in instance.queue:
            if item["nome_do_arquivo"] == path_file:
                file_is_new = False

    return file_is_new


def process(path_file, instance):
    file_content = txt_importer(path_file)

    file_infos = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }

    file_is_new = search_for_file(path_file, instance)

    if file_is_new:
        instance.enqueue(file_infos)

    print(file_infos, file=sys.stdout)


def remove(instance):
    if instance.__len__() > 0:
        path_file = instance.queue[0]["nome_do_arquivo"]
        instance.dequeue()
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)
    else:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
