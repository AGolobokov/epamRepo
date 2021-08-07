import sqlite3 as sql


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        # open connection
        self.connection_db = sql.connect(self.database_name)
        self.cursor = self.connection_db.cursor()

        # prepare for magic next
        self.start = 0
        counter = 0
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        for row in self.cursor:
            counter += 1
        self.stop = counter

        # create dict for magic next
        self.dict_next = {}
        columns = [description[0] for description in self.cursor.description]
        for elm in columns:
            if elm not in self.dict_next:
                self.dict_next.update({elm: elm})
        print(self.dict_next)

        self.connection_db.commit()
        # close connection
        self.cursor.close()
        self.connection_db.close()

    def __getitem__(self, key):
        self.connection_db = sql.connect(self.database_name)
        self.cursor = self.connection_db.cursor()
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        for row in self.cursor:
            if key in row:
                return row
        self.cursor.close()
        self.connection_db.close()
        return None

    def __len__(self):
        self.connection_db = sql.connect(self.database_name)
        self.cursor = self.connection_db.cursor()
        # var 1
        # self.cursor.execute(f'SELECT count(*) FROM {self.table_name}')
        # result = self.cursor.fetchone()
        # return result[0]

        # var 2
        counter = 0
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        for row in self.cursor:
            counter += 1
        return counter

    def __contains__(self, element):
        self.connection_db = sql.connect(self.database_name)
        self.cursor = self.connection_db.cursor()
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        for row in self.cursor:
            if element in row:
                return True
        self.cursor.close()
        self.connection_db.close()
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == 0:
            self.stop = TableData.__len__(self)
            self.connection_db = sql.connect(self.database_name)
            self.cursor = self.connection_db.cursor()
            self.cursor.execute(f"SELECT * FROM {self.table_name}")
        if self.start >= self.stop:
            self.start = 0
            raise StopIteration
        db_line = self.cursor.fetchone()
        local_count = 0
        for key in self.dict_next:
            self.dict_next[key] = db_line[local_count]
            local_count += 1
        self.start += 1
        return self.dict_next


if __name__ == "__main__":

    presidents = TableData(database_name="example.sqlite", table_name="presidents")
    print(len(presidents))
    print(presidents["Yeltsin"])

    if "Yeltsin" in presidents:
        print("Yes\n")
    else:
        print("No\n")

    for president in presidents:
        print(president["name"])

    for president in presidents:
        print(president["age"])

    # open connection
    # new_connection_db = sql.connect('example.sqlite')
    # new_cursor = new_connection_db.cursor()
    # new_query = "INSERT INTO presidents VALUES (?, ?, ?);"
    # new_cursor.execute(new_query, ('Bacron', 123, 'France'))
    #
    # new_connection_db.commit()
    # # close connection
    # new_cursor.close()
    # new_connection_db.close()
    #
    # print(len(presidents))
    #
    # for president in presidents:
    #     print(president['name'])
