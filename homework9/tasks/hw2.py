"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

# >>> with supressor(IndexError):
...    [][2]

"""
import contextlib


class SupressorClass:
    """
    This class is context manager, that suppresses passed exception
    """

    def __init__(self, error):
        self.error = error

    def __enter__(self):
        print("__enter__")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("__exit__")
        return isinstance(exc_value, self.error)


@contextlib.contextmanager
def supressor_generator(error):
    """
     This generator is context manager, that suppresses passed exception
    :param error: name of exception that we should suppress
    :return:
    """
    try:
        yield
    except error:
        print(f"Exception {error} was suppressed")


if __name__ == "__main__":
    with SupressorClass(AssertionError):
        raise AssertionError

    with supressor_generator(AssertionError):
        raise AssertionError
