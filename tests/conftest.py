import os
import platform
from pathlib import Path

import allure
import pytest

from model_generators.pet_generator import PetGenerator
from api.pet_api import PetClient
from utils.response_assertions import assert_status_code


def get_project_root_dir():
    return Path(__file__).absolute().parent.parent


@allure.title("Create a new pet for the test")
@pytest.fixture
def create_pet():
    pet = PetGenerator.generate_new_pet()
    status_code, response_data = PetClient.add_pet(pet)
    assert_status_code(status_code)
    yield pet


@pytest.fixture(scope="session", autouse=True)
def create_env_file():
    yield
    envs = [
        f"os_platform = {os.name}",
        f"\nos_release = {platform.release()}",
        f"\nos_version = {platform.version()}",
        f"\npython_version = {platform.python_version()}"
    ]
    with open("allure-results/environment.properties", mode="w") as f:
        f.writelines(envs)
