# pet_test_api
Pet project which demonstrates automation testing of REST API

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
