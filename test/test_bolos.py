import sys
sys.path.append(".")
from src.bowling import Bolos

def test_Bolos():
    assert 60 == Bolos("12345123451234512345").score()
    assert 90 == Bolos("9-9-9-9-9-9-9-9-9-9-").score()
    assert 82 == Bolos("9-3561368153258-7181").score()
    assert 121 == Bolos("9-3/613/815/-/8-7/8-").score()
    assert 100 == Bolos("X9-9-9-9-9-9-9-9-9-").score()
    assert 110 == Bolos("X9-X9-9-9-9-9-9-9-").score()
    assert 120 == Bolos("XX9-9-9-9-9-9-9-9-").score()
    assert 141 == Bolos("XXX9-9-9-9-9-9-9-").score()
    assert 131 == Bolos("9-3/613/815/-/8-7/8/8").score()
    assert 150 == Bolos("5/5/5/5/5/5/5/5/5/5/5").score()
    assert 111 == Bolos("9-9-9-9-9-9-9-9-9-XXX").score()
    assert 149 == Bolos("8/549-XX5/53639/9/X").score()
    assert 175 == Bolos("X5/X5/XX5/--5/X5/").score()
    assert 300 == Bolos("XXXXXXXXXXXX").score()

  