import json

from models.pet import Pet
from tests.conftest import get_project_root_dir
from utils.response_assertions import validate_json_schema


class TestValidation:
    """
    Test created for testing purposes just to verify
    that pydantic can validate schema and catch errors
    like jsonschema.validate
    """

    json_file_path = f'{get_project_root_dir()}/data/pet.json'

    def test_jsonschema_validate(self):
        with open(self.json_file_path) as f:
            text = json.load(f)

        # validate json schema using jsonschema.validate
        validate_json_schema(text, Pet.model_json_schema())

    def test_pydantic_validate(self):
        with open(self.json_file_path) as f:
            text = f.read()

        # validate json schema using pydantic
        Pet.model_validate_json(text.strip(), strict=False)
        Pet.model_validate_json(text.strip(), strict=True)
