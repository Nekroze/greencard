========
Usage
========

In order to use greencard we first need to create our tests.

In a directory called tests every ``.py`` file will be loaded by the
``greencard`` test runner. For example to check for a valid code we could have
the file tests/code.py might look like this::

    import greencard

    
    @greencard.test
    def validate_code(card):
        assert 0 < card.code <= 1000

Then by calling the following::

    $ greencard mylibrary.lbr

**greencard** will look in the tests directory and load the ``validate_code``
test that will be called on each card in the library to ensure that all cards
have a code inbetween 1 and 1000.
