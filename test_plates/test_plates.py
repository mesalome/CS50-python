import plates

def main():
    test_right_length()
    test_wrong_length()
    test_number_place()
    test_nofirst_zeros()
    test_first_zeros()
    test_capital_letters()
    test_only_numbers()
    test_wrong_number_placement()
    test_non_alphanumeric_char()



def test_right_length():
    assert plates.is_valid("sa") == True
    assert plates.is_valid("sal") == True
    assert plates.is_valid("salo") == True
    assert plates.is_valid("salom") == True
    assert plates.is_valid("salome") == True

def test_wrong_length():
    assert plates.is_valid("salomee") == False


def test_number_place():

    assert plates.is_valid("ww1") == True
    assert plates.is_valid("ww12") == True
    assert plates.is_valid("www5") == True
    assert plates.is_valid("www99") == True
    assert plates.is_valid("wwww6") == True
    assert plates.is_valid("wwwww3") == True

def test_nofirst_zeros():
    assert plates.is_valid("www90") == True
    assert plates.is_valid("ww60") == True
    assert plates.is_valid("wwww30") == True

def test_first_zeros():
    assert plates.is_valid("www09") == False
    assert plates.is_valid("ww006") == False
    assert plates.is_valid("wwww00") == False

def test_capital_letters():
    assert plates.is_valid("SA") == True
    assert plates.is_valid("SA90") == True
    assert plates.is_valid("SAL99") == True
    assert plates.is_valid("SAKK99") == True
    assert plates.is_valid("SALOME") == True

def test_only_numbers():
    assert plates.is_valid("5") == False
    assert plates.is_valid("59") == False
    assert plates.is_valid("77777") == False
    assert plates.is_valid("999999") == False

def test_wrong_number_placement():
    assert plates.is_valid("5mmmm") == False
    assert plates.is_valid("59nnn") == False
    assert plates.is_valid("m5mmm") == False
    assert plates.is_valid("mm55mm") == False

def test_non_alphanumeric_char():
    assert plates.is_valid("mmm+") == False
    assert plates.is_valid("$$$") == False
    assert plates.is_valid("..") == False

if __name__ == "__main__":
    main()