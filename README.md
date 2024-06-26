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


# The following plugins in some way change the normal test run flow:
## Plugins That Change the Normal Test Run Flow
* pytest-order      —   Allows us to specify the order using a marker  
* pytest-randomly   —   Randomizes the order, first by file, then by class, then by test. It works itself (plugin only should be installed and then we can run tests as usual - ```pytest -v```)  
* pytest-repeat     —   Makes it easy to repeat a single test, or multiple tests, a specific number of times  
```pytest --count=10 test_parallel.py``` - run "test_parallel.py" 10 times
* pytest-rerunfailures  —   Re-runs failed tests. Helpful for flaky tests  
* pytest-xdist      —   Runs tests in parallel, either using multiple CPUs on one machine, or multiple remote machines  
```pytest -n=auto test_parallel.py```  - run "test_parallel.py" tests on as many CPU cores as possible.
## Plugins That Alter or Enhance Output
* pytest-sugar      —   Shows green checkmarks instead of dots for passing tests and has a nice progress bar. It also shows failures instantly, like pytest-instafail
## Plugins for Web Development
* pytest-selenium   —   Provides fixtures to allow for easy configuration of browser-based tests. Selenium is a popular tool for browser testing.  
* pytest-splinter   —   Built on top of Selenium as a higher level interface, this allows Splinter to be used more easily from pytest.  
* pytest-django and pytest-flask    —   Help make testing Django and Flask applica-tions easier with pytest. Django and Flask are two of the most popular web frameworks for Python.  
## Plugins for Fake Data
* Faker             —   Generates fake data for you. Provides faker fixture for use with pytest
* model-bakery      —   Generates Django model objects with fake data.
* pytest-factoryboy —   Includes fixtures for Factory Boy, a database model data generator
* pytest-mimesis    —   Generates fake data similar to Faker, but Mimesis is quite a bit faster
## Plugins That Extend pytest Functionality
* pytest-cov        —   Runs coverage while testing
* pytest-benchmark  —   Runs benchmark timing on code within tests
* pytest-timeout    —   Doesn’t let tests run too long
* pytest-asyncio    —   Tests async functions
* pytest-bdd        —   Writes behavior-driven development (BDD)–style tests with pytest
* pytest-freezegun  —   Freezes time so that any code that reads the time will get the same value during a test. You can also set a particular date or time.
* pytest-mock       —   A thin-wrapper around the unittest.mock patching API