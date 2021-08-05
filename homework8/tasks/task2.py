import sqlite3 as sql


class TableData:

    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

        self.connection_db = sql.connect(self.database_name)
        self.cursor = self.connection_db.cursor()

        counter = 0
        self.cursor.execute(f'SELECT * FROM {self.table_name}')
        for row in self.cursor:
            counter += 1
        self.start = 0
        self.stop = counter

        # создаем словарь для некст
        self.dict_next = {}
        colons = [description[0] for description in self.cursor.description]
        for elm in colons:
            if elm not in self.dict_next:
                self.dict_next.update({elm:elm})
        # print(self.dict_next)

        self.connection_db.commit()
        self.my_a = self.one_step_query_generator(self.stop)
        # self.cursor.close()
        # self.connection_db.close()

    def one_step_query_generator(self, lenght):
        self.cursor.execute(f'SELECT * FROM {self.table_name}')
        for i in range(0, lenght):
            a = self.cursor.fetchone()
            yield a

    def __getitem__(self, key):
        self.cursor.execute(f'SELECT * FROM {self.table_name}')
        for row in self.cursor:
            if key in row:
                return row
        return None

    def __len__(self):
        # var 1
        # self.cursor.execute(f'SELECT count(*) FROM {self.table_name}')
        # result = self.cursor.fetchone()
        # return result[0]

        # var 2
        counter = 0
        self.cursor.execute(f'SELECT * FROM {self.table_name}')
        for row in self.cursor:
            counter += 1
        return counter

    def __contains__(self, element):
        self.cursor.execute(f'SELECT * FROM {self.table_name}')
        for row in self.cursor:
            if element in row:
                return True
        return False

    def __iter__(self):
        return self

    def __next__(self):
        value_from_gen = next(self.my_a)
        local_count = 0
        for key in self.dict_next:
            self.dict_next[key] = value_from_gen[local_count]
            local_count += 1
        if self.start >= self.stop:
            raise StopIteration
        current = self.start
        self.start += 1
        return self.dict_next


presidents = TableData(database_name='example.sqlite', table_name='presidents')
print(len(presidents))
print(presidents['Yeltsin'])

if 'Yeltsin' in presidents:
    print("Yes")
else:
    print("No")

print()

for president in presidents:
    print(president)


