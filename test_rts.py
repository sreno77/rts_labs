from RtsLabs import RtsLabs
import pytest

@pytest.fixture(scope='session')
def rts():
    return RtsLabs()

def test_all_above(rts):
    results_dict = rts.aboveBelow(
        [9, 8, 7, 10],
        6
    )
    assert results_dict.get('above') == 4

def test_all_below(rts):
    results_dict = rts.aboveBelow(
        [9, 8, 7, 6],
        10
    )
    assert results_dict.get('below') == 4

def test_above_and_below(rts):
    results_dict = rts.aboveBelow(
         [1, 5, 2, 1, 10],
         6
    )
    assert results_dict.get('above') == 1
    assert results_dict.get('below') == 4

def test_above_below_and_same(rts):
    results_dict = rts.aboveBelow(
         [1, 0, 2, 1, 14, 6],
         6
    )
    assert results_dict.get('above') == 1
    assert results_dict.get('below') == 4

def test_string_rotate_error_on_str(rts):
    with pytest.raises(RuntimeError) as excep:
        rts.stringRotation('Scott Reno', 'abc')

    assert 'is not an integer' in str(excep.value)

def test_string_rotate_error_on_float(rts):
    with pytest.raises(RuntimeError) as excep:
        rts.stringRotation('Scott Reno', 2.4)

    assert 'is not an integer' in str(excep.value)

def test_string_rotate_error_on_zero(rts):
    with pytest.raises(RuntimeError) as excep:
        rts.stringRotation('Scott Reno', 0)

    assert 'is not positive' in str(excep.value)

def test_string_rotate_error_on_negative(rts):
    with pytest.raises(RuntimeError) as excep:
        rts.stringRotation('Scott Reno', -1)

    assert 'is not positive' in str(excep.value)

def test_string_rotate1(rts):
    results = rts.stringRotation('Scott Reno', 4)
    assert results == 'RenoScott '

def test_string_rotate2(rts):
    results = rts.stringRotation('MyString', 2)
    assert results == 'ngMyStri'