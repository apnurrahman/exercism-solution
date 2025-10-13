"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    
    seat = ['A', 'B', 'C', 'D']
    for num in range(0, number):
        yield seat[num % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    letter_gen = generate_seat_letters(number)
    seat_number = 1
    for counter in range(0, number):
        # if seat_number == 12 and counter % 4 == 3:
        #     seat_number += 2
        #     continue
        seat_letter = next(letter_gen)
        yield f"{seat_number}{seat_letter}"
        if seat_number == 12 and counter % 4 == 3:
            seat_number += 2
        elif counter % 4 == 3 and counter != 0:
            seat_number += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seats = generate_seats(len(passengers))
    names_and_seats = {}
    for passenger in passengers:
        individual_seat = next(seats)
        names_and_seats.setdefault(passenger, individual_seat)

    return names_and_seats

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    #using ljust (left adjust) to fill zeros
    zeros = ""
    for counter in range(0, len(seat_numbers)):
        seat_and_flight = seat_numbers[counter] + flight_id
        ticket_id = seat_and_flight.ljust(12, '0')
        yield ticket_id
