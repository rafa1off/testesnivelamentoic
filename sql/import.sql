copy empresas from '<STORAGE_DIR>/Relatorio_cadop.csv' delimiter ';' csv header encoding 'utf8' on conflict (registro_ans) do nothing;

create table if not exists temp_contas (
    data date,
    registro_ans integer,
    cd_conta_contabil integer,
    descricao varchar(255),
    vl_saldo_inicial money,
    vl_saldo_final money
);

copy temp_contas from '<STORAGE_DIR>/1T2024.csv' delimiter ';' csv header encoding 'utf8';
copy temp_contas from '<STORAGE_DIR>/2T2024.csv' delimiter ';' csv header encoding 'utf8';
copy temp_contas from '<STORAGE_DIR>/3T2024.csv' delimiter ';' csv header encoding 'utf8';
copy temp_contas from '<STORAGE_DIR>/4T2024.csv' delimiter ';' csv header encoding 'utf8';

insert into contas
select * from temp_contas where exists (select registro_ans from empresas where temp_contas.registro_ans = empresas.registro_ans);

drop table temp_contas;
