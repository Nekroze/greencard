from argparse import ArgumentParser


def main(clargs=None):
    parser = ArgumentParser(
        description="A card validator for Librarian databases.")
    args = parser.parse_args(clargs)
