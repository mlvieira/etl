CREATE TABLE prd.transacoes (
	        nom_arquivo varchar(255) NULL,
			oid_transacao varchar(255) NOT NULL PRIMARY KEY,
            num_cpf_cnpj varchar(14) NULL,
	        cod_cooperativa varchar(5) NULL,
	        cod_agencia varchar(3) NULL,
            cod_conta varchar(5) NULL,
            num_plastico varchar(5) NULL,
            dat_transacao date null,
            vlr_transacao numeric(18,2) NULL,
            nom_modalidade varchar(7) NULL,
            nom_cidade_estabelecimento varchar(255) NULL
);
COMMENT ON COLUMN prd.transacoes.nom_arquivo IS 'Nome do arquivo carregado';
COMMENT ON COLUMN prd.transacoes.oid_transacao IS 'OID da transacao';
COMMENT ON COLUMN prd.transacoes.num_cpf_cnpj IS 'Número do CPF/CNPJ do associado';
COMMENT ON COLUMN prd.transacoes.cod_cooperativa IS 'Número que identifica uma cooperativa';
COMMENT ON COLUMN prd.transacoes.cod_agencia IS 'Número que identifica uma agência de uma cooperativa';
COMMENT ON COLUMN prd.transacoes.cod_conta IS 'Número de uma conta corrente';
COMMENT ON COLUMN prd.transacoes.num_plastico IS 'Número único que identifica um cartão de crédito';
COMMENT ON COLUMN prd.transacoes.dat_transacao IS 'Data, hora e minuto em que a transação descrita ocorreu';
COMMENT ON COLUMN prd.transacoes.vlr_transacao IS 'Valor da transação realizada no cartão';
COMMENT ON COLUMN prd.transacoes.nom_modalidade IS 'Modalidade da transação, ou crédito ou débito';
COMMENT ON COLUMN prd.transacoes.nom_cidade_estabelecimento IS 'Cidade do estabelecimento em que ocorreu a transação';
COMMENT ON TABLE prd.transacoes IS 'Tabela contendo informações de transações de cartões de débito e crédito.';
