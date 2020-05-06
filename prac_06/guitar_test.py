from prac_06.guitar import Guitar

CURRENT_YEAR = 2020


def test_guitar():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other_guitars = Guitar("Another Guitar", 2013, 2000.9)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 98,
                                                      guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other_guitars.name, 7,
                                                      other_guitars.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,
                                                         True,
                                                         guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other_guitars.name,
                                                         False,
                                                         other_guitars.is_vintage()))


if __name__ == '__main__':
    test_guitar()