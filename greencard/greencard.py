from functools import wraps


TESTS = []


def greencard(func):
    """
    A decorator for providing a unittesting function/method with every card in
    a librarian card library database when it is called.
    """
    @wraps(func)
    def Wrapped(*args, **kwargs):
        """Transparent wrapper."""
        return func(*args, **kwargs)
    TESTS.append(Wrapped)
    return Wrapped


def descovery(testdir):
    """Descover and load greencard tests."""
    import os
    from glob import glob
    import importlib

    for testpath in glob(os.path.join(testdir, "*.py")):
        importlib.import_module(testpath)


def main(clargs=None):
    """Command line entry point."""
    from argparse import ArgumentParser
    from librarian.library import Library

    parser = ArgumentParser(
        description="A test runner for each card in a librarian library.")
    parser.add_argument("library", help="Library database")
    parser.add_argument("-t", "--tests", default="./tests/",
                        help="Test directory")
    args = parser.parse_args(clargs)

    descovery(args.tests)

    lib = Library(args.library)
    failures = 0

    for card in library.retrieve_all():
        for test in TESTS:
            try:
                test(card)
            except AssertionError:
                print("{0} failed {1}".format(card, test.__name__))
                failures += 1
    return failure
