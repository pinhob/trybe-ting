from queue import Queue


def search_for_word_in_lines(word, instance):
    search_result = {"file_name": "", "lines_with_word": [], "lines": []}

    for item in instance.queue:
        for line in item["linhas_do_arquivo"]:
            if str.lower(word) in str.lower(line):
                # num da linha: item["linhas_do_arquivo"].index(line)
                search_result["file_name"] = item["nome_do_arquivo"]

                search_result["lines_with_word"].append(
                    (item["linhas_do_arquivo"].index(line)) + 1
                )

                search_result["lines"].append(line)

    return search_result


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    file_has_word = search_for_word_in_lines(word, instance)

    if len(file_has_word["lines_with_word"]) > 0:
        search_result = [
            {
                "palavra": word,
                "arquivo": file_has_word["file_name"],
                "ocorrencias": [],
            }
        ]

        for number in file_has_word["lines_with_word"]:
            search_result[0]["ocorrencias"].append({"linha": number})

        print(file_has_word["lines"])

        return search_result
    else:
        return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    file_has_word = search_for_word_in_lines(word, instance)

    if len(file_has_word["lines_with_word"]) > 0:
        search_result = [
            {
                "palavra": word,
                "arquivo": file_has_word["file_name"],
                "ocorrencias": [],
            }
        ]

        for index, number in enumerate(file_has_word["lines_with_word"]):
            conteudo = file_has_word["lines"][index]

            search_result[0]["ocorrencias"].append({
                "linha": number,
                "conteudo": conteudo
            })

        return search_result
    else:
        return []


if __name__ == "__main__":
    project = Queue()
    print(exists_word("pedro", project))
