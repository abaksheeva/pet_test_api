import pytest
import random

from model_generators.pet_generator import PetGenerator
from models.pet import Pet, statuses
from api.pet_api import PetClient
from models.pets import Pets

from utils.response_assertions import assert_status_code, validate_schema, validate_fields


class TestPetApi:

    @pytest.mark.pet
    def test_adding_pet(self):
        """
        Verify adding a new pet to the store
        """
        pet = PetGenerator().generate_new_pet()

        status_code, response_data = PetClient.add_pet(pet)

        assert_status_code(status_code)
        validate_schema(Pet, response_data)
        validate_fields(response_data, pet)

    # TODO: look to POST vs PUT
    @pytest.mark.pet
    def test_updating_pet(self, create_pet):
        """
        Verify updating an existing pet
        """
        pet = PetGenerator().generate_new_pet()

        status_code, response_data = PetClient.update_pet(pet)

        assert_status_code(status_code)
        validate_schema(Pet, response_data)
        validate_fields(response_data, pet)

    @pytest.mark.pet
    def test_updating_pet_by_id_and_name(self, create_pet):
        """
        Verify updating an existing pet
        """
        name_to_update = 'new_name'
        create_pet['name'] = name_to_update
        status_code, response_data = PetClient.updates_pet_in_a_store(
            pet_id=create_pet['id'], name=name_to_update)

        assert_status_code(status_code)

        status_code, response_data = PetClient.find_pet_by_id(create_pet['id'])
        assert_status_code(status_code)
        validate_fields(response_data, create_pet)

    @pytest.mark.pet
    def test_updating_pet_by_id_and_status(self, create_pet):
        """
        Verify updating an existing pet
        """
        status_to_update = 'new_status'
        create_pet['status'] = status_to_update
        status_code, response_data = PetClient.updates_pet_in_a_store(
            pet_id=create_pet['id'], status=status_to_update)

        assert_status_code(status_code)

        status_code, response_data = PetClient.find_pet_by_id(create_pet['id'])
        assert_status_code(status_code)
        validate_fields(response_data, create_pet)

    @pytest.mark.pet
    def test_updating_pet_by_id_name_and_status(self, create_pet):
        """
        Verify updating an existing pet
        """
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

    @pytest.mark.pet
    def test_finding_pets_by_status(self):
        """
        Verify finding pets by statuses
        """
        status_to_find = random.choice(statuses)
        status_code, response_data = PetClient.find_pets_by_status(status_to_find)

        assert_status_code(status_code)
        validate_schema(Pets, response_data)

        for pet in response_data:
            assert pet['status'] == status_to_find, \
                f"Status should be {status_to_find} (Pet ID = {pet['id']})"

    @pytest.mark.pet
    def test_finding_pet_by_id(self, create_pet):
        """
        Verify finding pet by ID
        """
        status_code, response_data = PetClient.find_pet_by_id(create_pet['id'])

        assert_status_code(status_code)
        validate_schema(Pet, response_data)
        validate_fields(response_data, create_pet)

    @pytest.mark.pet
    def test_delete_pet(self, create_pet):
        """
        Verify deleting a pet
        """
        status_code, response_data = PetClient.delete_pet(create_pet['id'])

        assert_status_code(status_code)
        validate_fields(response_data, {
            'code': status_code,
            'type': 'unknown',
            'message': str(create_pet['id'])
        })

        # Verify the pet was removed after calling /delete/{pet_id} endpoint
        status_code, response_data = PetClient.find_pet_by_id(create_pet['id'])
        assert_status_code(status_code, expected_status_code=404)
