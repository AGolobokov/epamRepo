import pytest
import unittest
from homework8.tasks.task2 import TableData

import sqlite3 as sql


def test_TableData():

    exemplar = TableData(database_name="example.sqlite", table_name="presidents")

    assert len(exemplar) == 6

    assert exemplar["Yeltsin"] == ("Yeltsin", 999, "Russia")
    assert exemplar["Trump"] == ("Trump", 1337, "US")

    assert ("Yeltsin" in exemplar) == True

    test_list_name = list()
    for president in exemplar:
        test_list_name.append(president["name"])

    assert test_list_name == [
        "Yeltsin",
        "Trump",
        "Big Man Tyrone",
        "Macron",
        "Duda",
        "Mada",
    ]

    test_list_age = list()
    for president in exemplar:
        test_list_age.append(president["age"])

    assert test_list_age == [999, 1337, 101, 123, 555, 555]

    # пытался добавить запись сделать новую проверку что методы видят апдейт базы и удалить запись,но почему то не получается удалить запись :(
    # # # open connection
    # new_connection_db = sql.connect('example.sqlite')
    # new_cursor = new_connection_db.cursor()
    # new_query = "INSERT INTO presidents VALUES (?, ?, ?);"
    # new_cursor.execute(new_query, ('Mada', 555, 'Grenland'))
    #
    # new_connection_db.commit()
    #
    # assert len(exemplar) == 6
    #
    # new_name_list = list()
    # for president in exemplar:
    #     new_name_list.append(president)
    #
    # assert new_name_list == ['Yeltsin', 'Trump', 'Big Man Tyrone', 'Macron', 'Duda', 'Wada', 'Mada']
    #
    # delete_query = """DELETE from presidents where name = ?"""
    # new_cursor.execute(delete_query, ('Mada',))
    # new_connection_db.commit()
    # # # close connection
    # new_cursor.close()
    # new_connection_db.close()
