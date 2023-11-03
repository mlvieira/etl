
class AssociadosDDL(object):

    ddl_stg = '''
        CREATE TABLE IF NOT EXISTS stg.associados (
	        nom_arquivo varchar(255) NULL,
	        num_cpf_cnpj varchar(14) NULL,
	        des_nome_associado varchar(255) NULL,
	        dat_associacao date NULL,
	        cod_faixa_renda int NULL,
            des_faixa_renda varchar(11) NULL
        );
    '''
    table_name = 'associados'

    insert_prd = '''
        INSERT INTO prd.associados (
          	nom_arquivo, num_cpf_cnpj,
	        des_nome_associado, dat_associacao,
	        cod_faixa_renda, des_faixa_renda  
        )
        SELECT
            nom_arquivo
            , num_cpf_cnpj 
            , des_nome_associado 
            , dat_associacao
            , cod_faixa_renda
            , replace(des_faixa_renda, 'MDIA', 'MÉDIA') as des_faixa_renda
        FROM
            stg.associados
        WHERE
            nom_arquivo = '@NOM_ARQUIVO'
    '''

    delete_prd_exists_stg = '''
        DELETE FROM prd.associados as prd
        WHERE
            EXISTS(
                SELECT
                    1
                FROM
                    stg.associados stg
                WHERE
                    stg.nom_arquivo = prd.nom_arquivo
            )
    '''

    select_stg_arquivos = '''
        SELECT
            DISTINCT nom_arquivo
        FROM stg.associados
    '''