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
```pytest -v```             - return more verbose output.
```pytest -vv```            - return max verbose output.
```pytest -s```             - allows to show print statements in the console.
```pytest --capture=no```   - allows to show print statements in the console.
```pytest --tb=no```        - hide traceback.
```pytest --tb=short```     - shorter traceback format.
```pytest --setup-show```   - shows us an order of operations of tests and fixtures.
```pytest --markers```      - print to console the list of markers.


# Pytest commands
```pytest ch1```                        - run all tests in 'ch1' directory.  
```pytest test_one.py test_two.py```    - run tests from two test files.  
```pytest test_one.py::test_passing```  - run test 'test_passing' function from 'test_one.py' file.  
```pytest test_one.py::TestEqiality::test_equality```  - run test 'test_equality' method from 'TestEqiality' class from 'test_one.py' file.  

```pytest -k pattern```                 - run all tests that contain the pattern.  
```pytest -k "equality and not equality_fail```        - run all tests that contain 'equality' and not contain 'equality_fail'.
```pytest -k "(dict or ids) and not TestEquality```    - run all tests with 'dict' or 'ids' in name, but not ones in TestEquality class.     

```pytest -m marker_name```             - run all tests whith specific marker.  
```pytest -m "marker_name1 and/or/not marker_name2..."```             - run all tests whith specific marker. 

```pytest --fixtures -v```              - return all fixtures info from current directory where we run a command (show us fixture name, scope, filename where fixture is located). Also we can add filename if we want to know the info about fixtures used in this file.  
```pytest --fixtures-per-test test_count.py::test_empty``` - return fixtures that used in 'test_empty' test in 'test_count.py' file.  

```pytest -s test_autouse.py```         - flag '-s' enables output capture.

```pytest -v "test_func_param.py::test_finish[write a book-done]"```    - run test "test_finish" with parameters ("write a book", "done") from "test_func_param.py" file.  

```pytest -v -ra```                     - flag '-ra' displayes the reason of a skiped tests after tests run.  



# Pytest markers
```@pytest.mark.skip(reason=None)```    - skip run of the test, can add a reason string.  
```@pytest.mark.skipif(condition, ..., *, reason)```    - skip run of the test if some condition is True.  
```@pytest.mark.xfail(condition, ..., *, reason, run=True, raises=None, strict=xfail_strict)```     - marked the test that should fail as expected.  
```@pytest.mark.parametrize(argnames, argvalues, indirect, ids, scope)```   - calls a test function multiple times , passing in different arguments in turn.  
```@pytest.mark.usefixtures(fixturename1, fixturename2, ...)```     - marks tests as needing all the specified fixtures.    


# Pytest fixture scope
```@pytest.fixture(scope="function")```     - default scope, fixture runs before/after each test function.  
```@pytest.fixture(scope="module")```       - fixture runs before/after each module (file with tests). Need to be in a 'conftest.py' file.  
```@pytest.fixture(scope="class")```        - fixture runs before/after each class (class with tests).   
```@pytest.fixture(scope="package")```      - fixture runs before/after each package (directory with test files). Need to be in a 'conftest.py' file.  
```@pytest.fixture(scope="session")```      - fixture runs before/after the session. Need to be in a 'conftest.py' file.  


# Pytest buildin fixtures
```tmp_path```              - returns a temp directory path. tmp_path is function scope  
```
file = tmp_path / "file.txt"
```

```tmp_path_factory```      - returns a temp path factory object. To create a new directory we should use mktemp method. tmp_path_factory is session scope  
```
path = tmp_path_factory.mktemp("sub")
file = path / "file.txt"
```

```capsys```                - fixture enables the capturing of writes to stdout and stderr
```
# save the output of the function in 'output' variable
output = capsys.readouterr().out.rstrip()
```
```
# this code will always be displayed in console, even without the -s flag 
with capsys.disabled():
    print("\ncapsys disabled print")
```