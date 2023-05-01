import twttr

def main():
    test_ommit_vowels()
    test_ommit_Capital_vowels()


def test_ommit_vowels():
    assert twttr.shorten("salome") == "slm"
    assert twttr.shorten("What's your name?") == "Wht's yr nm?"
    assert twttr.shorten("CS50") == "CS50"

def test_ommit_Capital_vowels():
    assert twttr.shorten("SALOME") == "SLM"
    assert twttr.shorten("WHO ARE YOU?") == "WH R Y?"


if __name__ == "__main__":
    main()