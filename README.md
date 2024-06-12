# pytest_book_discussion
Here I follow guides in a book to learn more about pytest and it's features


# Project setup
1. Create a folder on GIT service.
2. Clone repo.
3. Create a virtual environment for a project.
```
python -m venv venv
```
4. Activate virt env (powershell).
```
.\venv\Scripts\activate.ps1
```  
Deactivate virt env.
```
deactivate
```
5. Install a project code if we paste it into a project folder (cards_proj).
```
pip install ./cards_proj/
```
6. Install pytest.
```
pip install pytest
```
7. Create some tests.
8. Run tests.


# Pytest flags
```pytest -v```         - return more verbose output
```pytest -vv```        - return max verbose output
```pytest -s```         - allows to show print statements in the console
```pytest --tb=no```    - hide traceback.
```pytest --tb=short``` - shorter traceback format.


# Pytest commands
```pytest ch1```                        - run all tests in 'ch1' directory.  
```pytest test_one.py test_two.py```    - run tests from two test files.  
```pytest test_one.py::test_passing```  - run test 'test_passing' function from 'test_one.py' file.  
```pytest test_one.py::TestEqiality::test_equality```  - run test 'test_equality' method from 'TestEqiality' class from 'test_one.py' file.  
```pytest -k pattern```                 - run all tests that contain the pattern.  
```pytest -k "equality and not equality_fail```        - run all tests that contain 'equality' and not contain 'equality_fail'.
```pytest -k "(dict or ids) and not TestEquality```    - run all tests with 'dict' or 'ids' in name, but not ones in TestEquality class.     
```pytest -m marker_name```             - run all tests whith specific marker.   


# Pytest markers
```@pytest.mark.skip()```   - skip run of the test.
```@pytest.mark.skipif()``` - skip run of the test if some condition is True.
```@pytest.mark.xfail()```  - marked the test that should fail as expected.