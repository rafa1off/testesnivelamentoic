create table if not exists empresas (
    registro_ans integer PRIMARY KEY,
    cnpj bigint UNIQUE NOT NULL,
    razao_social varchar(255) NOT NULL,
    nome_fantasia varchar(255),
    modalidade varchar(255) NOT NULL,
    logradouro varchar(255) NOT NULL,
    numero varchar(255) NOT NULL,
    complemento varchar(255),
    bairro varchar(255) NOT NULL,
    cidade varchar(255) NOT NULL,
    uf varchar(255) NOT NULL,
    cep integer NOT NULL,
    ddd integer,
    telefone varchar(255),
    fax varchar(255),
    endereco_eletronico varchar(255),
    representante varchar(255),
    cargo_representante varchar(255),
    regiao_de_comercializacao integer,
    data_registro_ans date
);

create table if not exists contas (
    data date,
    registro_ans integer references empresas,
    cd_conta_contabil integer,
    descricao varchar(1024),
    vl_saldo_inicial money,
    vl_saldo_final money
);
