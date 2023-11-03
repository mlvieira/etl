
class TransacaoDDL(object):

    ddl_stg = '''
        CREATE TABLE IF NOT EXISTS stg.associados_frequentes (
            nom_arquivo varchar(255),
	        num_ano_mes varchar(6),
            num_cpf_cnpj varchar(14),
	        cod_cooperativa varchar(5),
	        cod_agencia varchar(3),
            cod_conta varchar(5),
            num_plastico varchar(5),
            dat_transacao timestamp,
            vlr_transacao numeric(18,2),
            nom_modalidade varchar(7),
            nom_cidade_estabelecimento varchar(255)
        );
    '''
    table_name = 'associados_frequentes'

    insert_prd = '''
        INSERT INTO prd.associados_frequentes (
            num_ano_mes, nom_arquivo, oid_transacao, 
            num_cpf_cnpj, cod_cooperativa, cod_agencia,
            cod_conta, num_plastico, dat_transacao,
            vlr_transacao, nom_modalidade, nom_cidade_estabelecimento
        )
        select
            to_char(dat_transacao, 'YYYYMM'), nom_arquivo, oid_transacao,
            num_cpf_cnpj, cod_cooperativa, cod_agencia,
            cod_conta, num_plastico, dat_transacao,
            vlr_transacao, nom_modalidade, nom_cidade_estabelecimento
        from
            prd.transacoes
        where
            dat_transacao >= current_date - interval '3' month
            and not exists(select 1 from prd.associados_frequentes af where af.oid_transacao = oid_transacao)

    '''

    purge_old_reg = '''
        DELETE FROM prd.associados_frequentes as prd
        WHERE
            dat_transacao < current_date - interval '3' month
    '''