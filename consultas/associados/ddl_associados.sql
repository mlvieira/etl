CREATE TABLE prd.associados (
	nom_arquivo varchar(255) NULL,
	num_cpf_cnpj varchar(14) NOT NULL PRIMARY KEY,
	des_nome_associado varchar(255) NULL,
	dat_associacao date NULL,
	cod_faixa_renda int NULL,
    des_faixa_renda varchar(11) NULL
);

COMMENT ON COLUMN prd.associados.nom_arquivo IS 'Nome do arquivo carregado';
COMMENT ON COLUMN prd.associados.num_cpf_cnpj IS 'Número único que identifica uma pessoa ou empresa';
COMMENT ON COLUMN prd.associados.des_nome_associado IS 'Nome do associado';
COMMENT ON COLUMN prd.associados.dat_associacao IS 'Data em que ocorreu a associação (mesmo que abertura da conta)';
COMMENT ON COLUMN prd.associados.cod_faixa_renda IS 'Código que identifica a faixa de renda';
COMMENT ON COLUMN prd.associados.des_faixa_renda IS 'Descrição da faixa de renda';
COMMENT ON TABLE prd.associados IS 'Tabela contendo informações sobre associados';
