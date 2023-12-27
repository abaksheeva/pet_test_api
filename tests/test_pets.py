import allure
import pytest
import random

from model_generators.message_generator import MsgGenerator
from model_generators.pet_generator import PetGenerator
from models.message import Message
from models.pet import Pet, statuses
from api.pet_api import PetClient
from models.pets import Pets

from utils.response_assertions import assert_status_code, validate_schema, validate_fields


@allure.tag("pet")
@allure.suite("Tests for pets")
class TestPetApi:

    @allure.title("Verify adding a new pet to the store")
    @pytest.mark.pet
    def test_adding_pet(self):
        pet = PetGenerator.generate_new_pet()

        status_code, response_data = PetClient.add_pet(pet)

        assert_status_code(status_code)
        validate_schema(Pet, response_data)
        validate_fields(response_data, pet)

    @allure.title("Verify updating an existing pet")
    @pytest.mark.pet
    def test_updating_pet(self, create_pet):
        pet = PetGenerator.generate_new_pet()

        status_code, response_data = PetClient.update_pet(pet)

        assert_status_code(status_code)
        validate_schema(Pet, response_data)
        validate_fields(response_data, pet)

    @allure.title("Verify updating an existing pet")
    @pytest.mark.pet
    def test_updating_pet_by_id_and_name(self, create_pet):
        name_to_update = 'new_name'
        create_pet['name'] = name_to_update
        status_code, response_data = PetClient.updates_pet_in_a_store(
            pet_id=create_pet['id'], name=name_to_update)

        assert_status_code(status_code)

        status_code, response_data = PetClient.find_pet_by_id(create_pet['id'])
        assert_status_code(status_code)
        validate_fields(response_data, create_pet)

    @allure.title("Verify updating an existing pet")
    @pytest.mark.pet
    def test_updating_pet_by_id_and_status(self, create_pet):
        status_to_update = 'new_status'
        create_pet['status'] = status_to_update
        status_code, response_data = PetClient.updates_pet_in_a_store(
            pet_id=create_pet['id'], status=status_to_update)

        assert_status_code(status_code)

        status_code, response_data = PetClient.find_pet_by_id(create_pet['id'])
        assert_status_code(status_code)
        validate_fields(response_data, create_pet)

    @allure.title("Verify updating an existing pet")
    @pytest.mark.pet
    def test_updating_pet_by_id_name_and_status(self, create_pet):
        name_to_update = 'new_name'
        status_to_update = 'new_status'

        create_pet['name'] = name_to_update
        create_pet['status'] = status_to_update
        status_code, response_data = PetClient.updates_pet_in_a_store(
            pet_id=create_pet['id'], name=name_to_update, status=status_to_update)

        assert_status_code(status_code)

        status_code, response_data = PetClient.find_pet_by_id(create_pet['id'])
        assert_status_code(status_code)
        validate_fields(response_data, create_pet)

    @allure.title("Verify finding pets by statuses")
    @pytest.mark.pet
    def test_finding_pets_by_status(self):
        status_to_find = random.choice(statuses)
        status_code, response_data = PetClient.find_pets_by_status(status_to_find)

        assert_status_code(status_code)
        validate_schema(Pets, response_data)

        for pet in response_data:
            assert pet['status'] == status_to_find, \
                f"Status should be {status_to_find} (Pet ID = {pet['id']})"

    @allure.title("Verify finding pet by ID")
    @pytest.mark.pet
    def test_finding_pet_by_id(self, create_pet):
        status_code, response_data = PetClient.find_pet_by_id(create_pet['id'])

        assert_status_code(status_code)
        validate_schema(Pet, response_data)
        validate_fields(response_data, create_pet)

    @allure.title("Verify deleting a pet")
    @pytest.mark.pet
    def test_delete_pet(self, create_pet):
        status_code, response_data = PetClient.delete_pet(create_pet['id'])

        assert_status_code(status_code)
        validate_schema(Message, response_data)
        validate_fields(response_data,
                        MsgGenerator.generate_from(code=200,
                                                   msg_type='unknown',
                                                   message=str(create_pet['id'])))

        with allure.step("Verify the pet was removed after calling /delete/{pet_id} endpoint"):
            status_code, response_data = PetClient.find_pet_by_id(create_pet['id'])
            assert_status_code(status_code, expected_status_code=404)
