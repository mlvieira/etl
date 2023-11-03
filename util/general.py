def parse_ddl(ddl, comment = True):
    parsed = {}
    for k in ddl.keys():
        parsed[k] = ddl[k]['comment' if comment else 'type']

    return parsed