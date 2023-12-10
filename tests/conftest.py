from pathlib import Path
import pytest

from model_generators.pet_generator import PetGenerator
from api.pet_api import PetClient
from utils.response_assertions import assert_status_code


def get_project_root_dir():
    return Path(__file__).absolute().parent.parent


@pytest.fixture
def create_pet():
    pet = PetGenerator().generate_new_pet()
    status_code, response_data = PetClient.add_pet(pet)
    assert_status_code(status_code)
    yield pet

