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
limit 10;

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
