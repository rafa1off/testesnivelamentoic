import scraping
import transfdados
from pathlib import Path


def main():
    # preparar diretórios
    data_dir = Path("data/")
    pdf_dir = Path(f"{data_dir}/pdf/")
    xlsx_dir = Path(f"{data_dir}/xlsx/")
    csv_dir = Path(f"{data_dir}/csv/")
    zip_dir = Path(f"{data_dir}/zip")

    if not data_dir.exists():
        data_dir.mkdir()

    if not pdf_dir.exists():
        pdf_dir.mkdir()

    if not xlsx_dir.exists():
        xlsx_dir.mkdir()

    if not csv_dir.exists():
        csv_dir.mkdir()

    if not zip_dir.exists():
        zip_dir.mkdir()

    scraping.teste(pdf_dir, xlsx_dir, zip_dir)
    transfdados.teste(xlsx_dir, csv_dir, zip_dir)


if __name__ == "__main__":
    main()
