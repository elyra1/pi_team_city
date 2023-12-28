import pytest
from programm import find_hypotenuse
def test_find_hypotenuse_default():
    assert(5 == find_hypotenuse(3, 4))

def test_find_hypotenuse_0_side():
    try:
        find_hypotenuse(0, 4)
        assert(False)
    except:
        assert(True)

def test_find_hypotenuse_correct():
    h = find_hypotenuse(5, 4)
    assert(h**2 - 25 == 16)
    assert(h**2 - 16 == 25)
    

if __name__ == "__main__":
    pytest.main(['--teamcity'])


