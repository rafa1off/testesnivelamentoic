import pandas
from pathlib import Path
from zipfile import ZipFile


def teste():
    # prepara diretórios
    data_dir = Path("data/")
    xlsx_dir = Path(f"{data_dir}/xlsx/")
    csv_dir = Path(f"{data_dir}/csv/")
    zip_dir = Path(f"{data_dir}/zip")

    if not data_dir.exists():
        data_dir.mkdir()

    if not xlsx_dir.exists():
        xlsx_dir.mkdir()

    if not csv_dir.exists():
        csv_dir.mkdir()

    if not zip_dir.exists():
        zip_dir.mkdir()

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
