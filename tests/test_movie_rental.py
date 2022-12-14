import pytest

from app.customer import Customer
from app.movie import Movie
from app.rental import Rental


class TestVideoRental:

    def test_video_rental(self):
        pass

    def test_single_new_release_statement(self):
        customer = Customer('Fred')
        customer.add_rental(Rental(Movie('The Cell', Movie.NEW_RELEASE), 3))
        expected = 'Rental Record for Fred\n\tThe Cell\t9\nYou owed 9\nYou earned 2 frequent renter points\n'
        assert expected == customer.statement()

    def test_dual_new_release_statement(self):
        customer = Customer('Fred')
        customer.add_rental(Rental(Movie('The Cell', Movie.NEW_RELEASE), 3))
        customer.add_rental(Rental(Movie('The Tigger Movie', Movie.NEW_RELEASE), 3))
        expected = 'Rental Record for Fred\n\tThe Cell\t9\n\tThe Tigger Movie\t9\nYou owed 18\nYou earned 4 frequent ' \
                   'renter points\n'
        assert expected == customer.statement()

    def test_single_childrens_statement(self):
        customer = Customer('Fred')
        customer.add_rental(Rental(Movie('The Tigger Movie', Movie.CHILDRENS), 3))
        expected = 'Rental Record for Fred\n\tThe Tigger Movie\t1.5\nYou owed 1.5\nYou earned 1 frequent renter ' \
                   'points\n'
        assert expected == customer.statement()

    def test_multiple_regular_statement(self):
        customer = Customer('Fred')
        customer.add_rental(Rental(Movie('Plan 9 from Outer Space', Movie.REGULAR), 1))
        customer.add_rental(Rental(Movie('8 1/2', Movie.REGULAR), 2))
        customer.add_rental(Rental(Movie('Eraserhead', Movie.REGULAR), 3))

        expected = 'Rental Record for Fred\n\tPlan 9 from Outer Space\t2\n\t8 1/2\t2\n\tEraserhead\t3.5\nYou owed ' \
                   '7.5\nYou earned 3 frequent renter points\n'
        assert expected == customer.statement()

    def tests_complex_type_statement(self):
        customer = Customer("Bob")
        customer.add_rental(Rental(Movie("Jaws", Movie.REGULAR), 2))
        customer.add_rental(Rental(Movie("Golden Eye", Movie.REGULAR), 3))
        customer.add_rental(Rental(Movie("Short New", Movie.NEW_RELEASE), 1))
        customer.add_rental(Rental(Movie("Long New", Movie.NEW_RELEASE), 2))
        customer.add_rental(Rental(Movie("Bambi", Movie.CHILDRENS), 3))
        customer.add_rental(Rental(Movie("Toy Story", Movie.CHILDRENS), 4))

        expected = "Rental Record for Bob\n\tJaws\t2\n\tGolden Eye\t3.5\n\tShort New\t3\n\tLong " \
                   "New\t6\n\tBambi\t1.5\n\tToy Story\t3.0\nYou owed 19.0\nYou earned 7 frequent renter points\n"

        assert expected == customer.statement()

