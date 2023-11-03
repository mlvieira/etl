
class EntidadeDDL(object):

    ddl_stg = '''
        CREATE TABLE IF NOT EXISTS stg.entidades (
	        nom_arquivo varchar(255) NULL,
	        cod_cooperativa varchar(5) NULL,
	        des_nome_cooperativa varchar(255) NULL,
	        cod_agencia varchar(3) NULL,
	        des_nome_agencia varchar(255) NULL
        );
    '''
    table_name = 'entidades'

    insert_prd = '''
        INSERT INTO prd.entidades (
            nom_arquivo, cod_coop_agencia,
            cod_cooperativa, des_nome_cooperativa,
            cod_agencia, des_nome_agencia
        )
        SELECT
            nom_arquivo
            , lpad(cod_cooperativa, 4, '0') || cod_agencia as cod_coop_agencia 
            , lpad(cod_cooperativa, 4, '0') as cod_cooperativa
            , des_nome_cooperativa
            , cod_agencia
            , replace(des_nome_agencia, 'AGNCIA', 'AGENCIA') as des_nome_agencia
        FROM
            stg.entidades
        WHERE
            nom_arquivo = '@NOM_ARQUIVO'
    '''

    delete_prd_exists_stg = '''
        DELETE FROM prd.entidades as prd
        WHERE
            EXISTS(
                SELECT
                    1
                FROM
                    stg.entidades stg
                WHERE
                    stg.nom_arquivo = prd.nom_arquivo
            )
    '''

    select_stg_arquivos = '''
        SELECT
            DISTINCT nom_arquivo
        FROM stg.entidades
    '''