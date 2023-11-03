def criar_insert(table_name: str, table_owner: str, columns: int):
    str_insert = f'insert into {table_owner}.{table_name} ' +\
                'values (' + ','.join('%s' for i in range(columns)) + ')'
    return str_insert