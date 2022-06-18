def incr(x):
    if x != 10:
        x += 1
    return x


def test_incr():
    assert incr(0) == 1
    assert incr(10) == 10 # Добавленный assert для 100% покрытия.

#pip install coverage

#coverage run -m pytest ex_3.py
#coverage report -m ex_3.py

#coverage run --branch -m pytest ex_3.py
#coverage report -m ex_3.py

#coverage html ex_3.py

#assert incr(10) == 10  # Добавленный assert для 100% покрытия.