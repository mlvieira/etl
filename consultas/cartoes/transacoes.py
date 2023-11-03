
class TransacaoDDL(object):

    ddl_stg = '''
        CREATE TABLE IF NOT EXISTS stg.transacoes (
	        nom_arquivo varchar(255),
            num_cpf_cnpj varchar(14),
	        cod_cooperativa varchar(5),
	        cod_agencia varchar(3),
            cod_conta varchar(5),
            num_plastico varchar(5),
            dat_transacao timestamp,
            vlr_transacao numeric(18,2),
            nom_modalidade varchar(7) NULL,
            nom_cidade_estabelecimento varchar(255)
        );
    '''
    table_name = 'transacoes'

    insert_prd = '''
        INSERT INTO prd.transacoes (
            nom_arquivo, oid_transacao, num_cpf_cnpj,
	        cod_cooperativa, cod_agencia, cod_conta,
            num_plastico, dat_transacao, vlr_transacao,
            nom_modalidade, nom_cidade_estabelecimento
        )
        select
            nom_arquivo, oid_transacao, num_cpf_cnpj,
	        cod_cooperativa, cod_agencia, cod_conta,
            num_plastico, dat_transacao, vlr_transacao,
            nom_modalidade, nom_cidade_estabelecimento
        from (            
            select
                nom_arquivo
                , md5(num_cpf_cnpj || lpad(cod_cooperativa, 4, '0') || cod_agencia || cod_conta || num_plastico || cast(dat_transacao as varchar(20)) || cast(vlr_transacao as varchar(20))) as oid_transacao
                , num_cpf_cnpj
                , lpad(cod_cooperativa, 4, '0') as cod_cooperativa
                , cod_agencia
                , cod_conta
                , num_plastico
                , dat_transacao
                , vlr_transacao
                , case nom_modalidade
                    when 'CREDITO' then upper('Crédito')
                    when 'DEBITO' then upper('Débito')
                    when '0' then null
                    else upper(nom_modalidade)
                end as nom_modalidade
                , nom_cidade_estabelecimento
			    , row_number() over(partition by num_cpf_cnpj || lpad(cod_cooperativa, 4, '0') || cod_agencia || cod_conta || num_plastico || cast(dat_transacao as varchar(20)) || cast(vlr_transacao as varchar(20)) order by dat_transacao) as rn
            from
                stg.transacoes
            where
			    nom_arquivo = '@NOM_ARQUIVO'
         ) stg
        where
            rn = 1

    '''

    delete_prd_exists_stg = '''
        DELETE FROM prd.transacoes as prd
        WHERE
            EXISTS(
                SELECT
                    1
                FROM
                    stg.transacoes stg
                WHERE
                    stg.nom_arquivo = prd.nom_arquivo
            )
    '''

    select_stg_arquivos = '''
        SELECT
            DISTINCT nom_arquivo
        FROM stg.transacoes
    '''