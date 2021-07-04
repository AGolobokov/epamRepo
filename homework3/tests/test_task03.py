import pytest

from homework3.tasks.task03 import make_filter


DATA_FOR_TEST = [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]


@pytest.mark.parametrize("arg, expected", [
    ({'name': 'polly', 'type': 'bird'}, [DATA_FOR_TEST[1]]),
    ({'name': 'Bill', 'type': 'bird'}, []),
    ({'name': 'Bill', 'type': 'person'}, [DATA_FOR_TEST[0]]),
    ])
def test_positive_make_filter(arg, expected):
    assert make_filter(**arg).apply(DATA_FOR_TEST) == expected
