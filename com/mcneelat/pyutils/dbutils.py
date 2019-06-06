import psycopg2


class AbstractDBUtils(object):
    def __init__(self, dbconn, schema):
        self.dbconn = dbconn
        self.cursor = self.dbconn.cursor()
        self.schema = schema

    def select(self, sql):
        results = []
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        while row is not None:
            results.append(row)
            row = self.cursor.fetchone()
        return results

    def runsql(self, sql, commit=True):
        self.cursor.execute(sql)
        if commit:
            self.dbconn.commit()

    def runsqlmulti(self, sql):
        for s in sql:
            self.runsql(s, False)
        self.dbconn.commit()

    def close(self):
        self.cursor.close()
        self.dbconn.close()


class PGUtils(AbstractDBUtils):
    def __init__(self, conf_data, schema=None):
        self.conf_data = conf_data
        dbconn = psycopg2.connect(**conf_data["DB_CONN_INFO"])
        super(PGUtils, self).__init__(dbconn, schema)
