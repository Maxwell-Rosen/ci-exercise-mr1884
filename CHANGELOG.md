## WIP


## Version 0.1: start of assignment

* First code.
trim trailing whitespace.................................................Failed
- hook id: trailing-whitespace
- exit code: 1
- files were modified by this hook

Fixing src/unc/__init__.py

black....................................................................Failed
- hook id: black
- files were modified by this hook

reformatted noxfile.py
reformatted tests/test_stdunc.py
reformatted tests/test_labunc.py
reformatted src/unc/__init__.py

All done! ✨ 🍰 ✨
4 files reformatted.

ruff.....................................................................Failed
- hook id: ruff
- exit code: 1
- files were modified by this hook

src/unc/__init__.py:15:89: E501 Line too long (91 > 88 characters)
Found 6 errors (5 fixed, 1 remaining).

trim trailing whitespace.................................................Passed
black....................................................................Passed
ruff.....................................................................Failed
- hook id: ruff
- exit code: 1

src/unc/__init__.py:15:89: E501 Line too long (91 > 88 characters)
Found 1 error

in __init__.py, I changed some spacing on line 15


⋊> ~/D/H/ci-exercise-mr1884 on main ⨯ nox -s tests                                                     (base) 12:20:17
nox > Running session tests
nox > Creating virtual environment (virtualenv) using python in .nox/tests
nox > python -m pip install -e .
nox > python -m pip install pytest uncertainties
nox > pytest
================================================ test session starts =================================================
platform darwin -- Python 3.11.3, pytest-7.4.2, pluggy-1.3.0
rootdir: /Users/mhrosen/Documents/Homework Scientific Computing/ci-exercise-mr1884
collected 85 items

tests/test_labunc.py .....                                                                                     [  5%]
tests/test_stdunc.py ................................................................................          [100%]

================================================= 85 passed in 0.16s =================================================
nox > Session tests was successful.
⋊> ~/D/H/ci-exercise-mr1884 on main ⨯
