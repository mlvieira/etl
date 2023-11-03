CREATE TABLE prd.entidades (
	nom_arquivo varchar(255) NOT NULL,
	cod_coop_agencia varchar(8) NOT null PRIMARY KEY,
	cod_cooperativa varchar(5) NULL,
	des_nome_cooperativa varchar(255) NULL,
	cod_agencia varchar(3) NULL,
	des_nome_agencia varchar(255) NULL
);

COMMENT ON COLUMN prd.entidades.nom_arquivo IS 'Nome do arquivo carregado';
COMMENT ON COLUMN prd.entidades.cod_coop_agencia IS 'Concatecação com cod_cooperativa + cod_agencia (PK)';
COMMENT ON COLUMN prd.entidades.cod_cooperativa IS 'Número que identifica uma cooperativa';
COMMENT ON COLUMN prd.entidades.des_nome_cooperativa IS 'Nome da cooperativa';
COMMENT ON COLUMN prd.entidades.cod_agencia IS 'Número que identifica uma agência de uma cooperativa';
COMMENT ON COLUMN prd.entidades.des_nome_agencia IS 'Nome da agência';
COMMENT ON TABLE prd.entidades IS 'Tabela contendo informações sobre cooperativas e agências.';
