import bank

def main():
    test_greeting_fine_Hello()
    test_greeting_fine_starts_with_h()
    test_greeting_fine_no_h()

def test_greeting_fine_Hello():
    assert bank.value("Hello") == 0
    assert bank.value("hello, dear customer") == 0

def test_greeting_fine_starts_with_h():
    assert bank.value("hi there") == 20
    assert bank.value("How can I help you?") == 20
    assert bank.value("hope you feel amazing") == 20

def test_greeting_fine_no_h():
    assert bank.value("good morning") == 100
    assert bank.value("Great to see you") == 100


if __name__ == "__main__":
    main()