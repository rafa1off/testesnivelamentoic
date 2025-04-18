import urllib.request as urllib
from pathlib import Path
from zipfile import ZipFile

import requests
from bs4 import BeautifulSoup


def teste(pdf_dir: Path, xlsx_dir: Path, zip_dir: Path):
    # enviar uma requisição Get para a url e retornar o conteúdo como texto
    content = requests.get(
        "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    ).content

    # transformar o texto em um objeto HTML
    soup = BeautifulSoup(content, "html.parser")

    # iterar sobre totas as tags com classe "internal-link"
    # utilizadas pelo site para definir o link de download do arquivo
    # e fazer o download
    archives_links = soup.find_all("a", class_="internal-link")
    for link in archives_links:
        if "Anexo I." in link.text:
            try:
                urllib.urlretrieve(link["href"], f"{pdf_dir}/anexo1.pdf")
            except FileExistsError:
                continue
            continue

        if "(Anexo I" in link.text:
            try:
                urllib.urlretrieve(link["href"], f"{xlsx_dir}/anexo1.xlsx")
            except FileExistsError:
                continue
            continue

        if "Anexo II" in link.text:
            try:
                urllib.urlretrieve(link["href"], f"{pdf_dir}/anexo2.pdf")
            except FileExistsError:
                continue
            continue

    # compactar arquivos em zip
    try:
        with ZipFile(f"{zip_dir}/Teste1.zip", mode="x") as zf:
            for file in pdf_dir.iterdir():
                zf.write(file)
    except FileExistsError:
        return
