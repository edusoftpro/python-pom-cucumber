from hamcrest import assert_that, equal_to, instance_of, is_, is_not
import unittest


class Biscuit:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def print_name(self):
        print(self.name)


class BiscuitTest(unittest.TestCase):
    def testEquals(self):
        the_biscuit = Biscuit("Ginger")
        my_biscuit = Biscuit("Ginger")
        assert_that(the_biscuit, is_not(equal_to(my_biscuit)))
        assert_that(the_biscuit, instance_of(Biscuit))
        assert_that(the_biscuit, is_(instance_of(Biscuit)))
        assert_that(the_biscuit, is_(Biscuit))


if __name__ == '__main__':
    from behave import __main__ as behave_executable
    behave_executable.main(None)
