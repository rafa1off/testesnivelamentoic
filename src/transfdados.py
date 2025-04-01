import pandas
from pathlib import Path
from zipfile import ZipFile


def teste(xlsx_dir: Path, csv_dir: Path, zip_dir: Path):
    # utiliza a biblioteca pandas para retornar
    # um dataframe da planilha do anexo1 salva pelo scraping
    dataframe = pandas.read_excel(
        f"{xlsx_dir}/anexo1.xlsx", sheet_name="Anexo I_Rol de Procedimentos", header=4
    )

    # renomeia as colunas
    od = "Seg. Odontológica"
    amb = "Seg. Ambulatorial"

    renamed_df = dataframe.rename(columns={"OD": od, "AMB": amb})

    # salva em csv
    renamed_df.to_csv(path_or_buf=f"{csv_dir}/anexo1.csv")

    # compactar arquivos em zip
    try:
        with ZipFile(f"{zip_dir}/Teste_RafaelGiuriatto.zip", mode="x") as zf:
            for file in csv_dir.iterdir():
                zf.write(file)
    except FileExistsError:
        return
