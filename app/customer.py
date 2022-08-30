from app.movie import Movie


class Customer(object):

    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, rental):
        self._rentals.append(rental)

    def get_name(self):
        return self._name

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        rentals = self._rentals
        result = 'Rental Record for ' + self._name + '\n'

        for rental in rentals:
            this_amount = 0

            # determines the amount for each line
            if rental.get_movie().get_price_code() == Movie.REGULAR:
                this_amount += 2
                if rental.days_rented > 2:
                    this_amount += (rental.get_days_rented() - 2) * 1.5
            elif rental.get_movie().get_price_code() == Movie.NEW_RELEASE:
                this_amount += rental.get_days_rented() * 3
            elif rental.get_movie().get_price_code() == Movie.CHILDRENS:
                this_amount += 1.5
                if rental.get_days_rented() > 3:
                    this_amount += (rental.get_days_rented() - 3) * 1.5

            # add frequent renter points
            frequent_renter_points += 1

            # add bonus for two day new release rental
            if rental.get_movie().get_price_code() == Movie.NEW_RELEASE and rental.get_days_rented() > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += '\t' + rental.get_movie().get_title() + '\t' + str(this_amount) + '\n'
            total_amount += this_amount

        # add footer lines
        result += 'You owed ' + str(total_amount) + '\n'
        result += 'You earned ' + str(frequent_renter_points) + ' frequent ' \
                  'renter points\n'

        return result
