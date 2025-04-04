import scraping
import transfdados
from pathlib import Path
from fastapi import FastAPI, Depends
from sqlmodel import create_engine, Session, text
from typing import Annotated
from models import Resultado


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


app = FastAPI()

engine = create_engine(
    "postgresql://postgres:postgres@postgres:5432/testenivelamentoic"
)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/")
async def root():
    return {"message": "Olá!"}


@app.get("/api/despesas-trimestre")
async def trimestre(session: SessionDep) -> list[Resultado]:
    sql = text("""
with despesas_trimestre as (
    select
        registro_ans,
        SUM(vl_saldo_final) as total_despesa
    from contas
    where descricao='EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
      and data >= DATE_TRUNC('quarter', CURRENT_DATE) - INTERVAL '1 year'
    group by registro_ans
)
select
    registro_ans,
    total_despesa
from despesas_trimestre
order by total_despesa desc
limit 10
    """)
    empresas = session.exec(sql).fetchall()
    return empresas


@app.get("/api/despesas-ano")
async def ano(session: SessionDep) -> list[Resultado]:
    sql = text("""
with despesas_ano as (
    select
        registro_ans,
        SUM(vl_saldo_final) as total_despesa
    from contas
    where descricao='EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
      and data >= CURRENT_DATE - INTERVAL '1 year'
    group by registro_ans
)
select
    registro_ans,
    total_despesa
from despesas_ano
order by total_despesa desc
limit 10;
    """)
    empresas = session.exec(sql).fetchall()
    return empresas


if __name__ == "__main__":
    main()
