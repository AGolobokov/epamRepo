import pytest
from homework8.tasks.task1 import KeyValueStorage


import tempfile


@pytest.fixture()
def test_file() -> str:
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/test.txt"
    with open(temp_file, "w") as f:
        f.write("name=kek\nlast_name=top\npower=9001\nsong=shadilay")
    return temp_file


def test_KeyValueStorage(test_file):

    exemplar_key_value_storage = KeyValueStorage(test_file)

    assert exemplar_key_value_storage.last_name == 'top'
    assert exemplar_key_value_storage.name == 'kek'
    assert exemplar_key_value_storage.power == 9001
    assert exemplar_key_value_storage.song == 'shadilay'
    assert exemplar_key_value_storage['name'] == 'kek'
    assert exemplar_key_value_storage['power'] == 9001
