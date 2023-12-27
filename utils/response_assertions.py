import json
import allure

from jsonschema import validate


def assert_status_code(status_code: int, expected_status_code: int = 200):
    with (allure.step(f"Assert that response status code is {expected_status_code}")):
        assert status_code == expected_status_code, (f"Response status code should be "
                                                     f"{expected_status_code} but got {status_code}")


def validate_json_schema(json_object, schema):
    with allure.step(f"Validate json schema:"):
        allure.attach(json.dumps(json_object), "actual_json", allure.attachment_type.JSON)
        allure.attach(json.dumps(schema), "schema", allure.attachment_type.JSON)

        validate(json_object, schema)


def validate_schema(model, json_object):
    with allure.step(f"Validate json schema:"):
        allure.attach(json.dumps(json_object), "actual_json", allure.attachment_type.JSON)
        allure.attach(json.dumps(model.model_json_schema()), "expected", allure.attachment_type.JSON)

        model.model_validate(json_object, strict=True)


def validate_fields(actual, expected):
    with allure.step(f"Validate fields:"):
        allure.attach(json.dumps(actual), "actual_json", allure.attachment_type.JSON)
        allure.attach(json.dumps(expected), "expected", allure.attachment_type.JSON)

        assert actual == expected, "Data from response should equals to expected"
