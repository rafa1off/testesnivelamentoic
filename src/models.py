from sqlmodel import SQLModel, Field


class Resultado(SQLModel, table=True):
    registro_ans: int = Field(primary_key=True)
    total_despesa: str
