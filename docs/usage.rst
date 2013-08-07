========
Usage
========

A good way to use **greencard** to test your card library is to use the
``GreenCard`` decorator on your unittests to provide them with each and every
card in the library::

    from unittest import TestCase
    from greencard.decorator import GreenCard

    class CardTests(TestCase):
        @GreenCard('mylibrary.lbr')
        def execute(self, card):
            self.assertTrue(0 < card.code <= 1000)

The above will test each and every card in the database stored at
``mylibrary.lbr`` and ensure that their code is higher then 0 but no higher
then 1000.
