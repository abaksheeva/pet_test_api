# pet_test_api
Pet project demonstrates automation testing of REST API using Python (3.12). 
It uses:
- _pytest_ for writing tests
- _requests_ for sending REST API requests
- _pydantic_ for json schemas creation and validation
- _allure-pytests_ for generating reports
- _pytest-xdist_ for running tests in parallel

It also contains examples of:
- running tests in a Docker container
- running tests in GitHub Actions (reports can be found on 
Actions tab -> Workflows -> pages-build-deployment. 
Open the last job and job _deploy_ will contain the link to Allure report)

Service under the test: https://petstore.swagger.io/#/

# Environment preparation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

# Run tests (local)

### Run tests
```bash
pytest tests
```

### View the report
```bash
allure serve allure-results
```

# Run tests in Docker 
Running tests in a Docker container has been implemented for the Github Actions

### In order to run tests in Docker
```bash
docker build -t pet-tests-api .
docker run pet-tests-api
```

### To copy test result from Docker
```bash
docker cp $(docker ps -a -q | head -1):./api-tests/allure-results .
```

### View the copied report from Docker
```bash
allure serve allure-results
```
