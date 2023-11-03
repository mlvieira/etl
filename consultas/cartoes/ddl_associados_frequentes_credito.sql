CREATE TABLE prd.associados_frequentes_credito (
	        num_ano_mes varchar(6),
            nom_arquivo varchar(255),
			oid_transacao varchar(255) NOT NULL PRIMARY KEY,
            num_cpf_cnpj varchar(14),
	        cod_cooperativa varchar(5),
	        cod_agencia varchar(3),
            cod_conta varchar(5),
            num_plastico varchar(5),
            dat_transacao date,
            vlr_transacao numeric(18,2),
            nom_modalidade varchar(7) NULL,
            nom_cidade_estabelecimento varchar(255)
);
COMMENT ON COLUMN prd.associados_frequentes_credito.num_ano_mes IS 'Ano e mês da data da transação YYYYMM';
COMMENT ON COLUMN prd.associados_frequentes_credito.nom_arquivo IS 'Nome do arquivo carregado';
COMMENT ON COLUMN prd.associados_frequentes_credito.oid_transacao IS 'OID da transacao';
COMMENT ON COLUMN prd.associados_frequentes_credito.num_cpf_cnpj IS 'Número do CPF/CNPJ do associado';
COMMENT ON COLUMN prd.associados_frequentes_credito.cod_cooperativa IS 'Número que identifica uma cooperativa';
COMMENT ON COLUMN prd.associados_frequentes_credito.cod_agencia IS 'Número que identifica uma agência de uma cooperativa';
COMMENT ON COLUMN prd.associados_frequentes_credito.cod_conta IS 'Número de uma conta corrente';
COMMENT ON COLUMN prd.associados_frequentes_credito.num_plastico IS 'Número único que identifica um cartão de crédito';
COMMENT ON COLUMN prd.associados_frequentes_credito.dat_transacao IS 'Data, hora e minuto em que a transação descrita ocorreu';
COMMENT ON COLUMN prd.associados_frequentes_credito.vlr_transacao IS 'Valor da transação realizada no cartão';
COMMENT ON COLUMN prd.associados_frequentes_credito.nom_modalidade IS 'Modalidade da transação. Essa base só apresenta crédito';
COMMENT ON COLUMN prd.associados_frequentes_credito.nom_cidade_estabelecimento IS 'Cidade do estabelecimento em que ocorreu a transação';
COMMENT ON TABLE prd.associados_frequentes_credito IS 'Tabela contendo informações de transações de cartões de crédito nos últimos 3 meses.';
