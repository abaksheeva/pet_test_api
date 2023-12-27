import json

import requests
import allure

from data.data import BASE_URL, HEADER_CONTENT_TYPE_JSON, HEADER_ACCEPT, HEADER_CONTENT_TYPE_FOARM_DATA


class PetClient:

    @staticmethod
    def upload_image(pet_id, filepath, filetype):
        url = f'{BASE_URL}/pet/{pet_id}/uploadImage'

        with allure.step(f"POST: Add new pet to the store (Request URL: {url}"):
            response = requests.post(url=url,
                                     headers=HEADER_ACCEPT | HEADER_CONTENT_TYPE_FOARM_DATA,
                                     params={
                                         'file': filepath,
                                         'type': filetype
                                     })

        return response.status_code, response.json()

    @staticmethod
    def add_pet(pet):
        url = f'{BASE_URL}/pet'

        with allure.step(f"POST: Add new pet to the store (Request URL: {url}, body: {json.dumps(pet)}"):
            response = requests.post(url=url,
                                     headers=HEADER_CONTENT_TYPE_JSON | HEADER_ACCEPT,
                                     data=json.dumps(pet)
                                     )
        return response.status_code, response.json()

    @staticmethod
    def update_pet(pet):
        url = f'{BASE_URL}/pet'

        with allure.step(f"PUT: Update an existing pet (Request URL: {url}, body: {json.dumps(pet)}"):
            response = requests.put(url=url,
                                    headers=HEADER_CONTENT_TYPE_JSON | HEADER_ACCEPT,
                                    data=json.dumps(pet)
                                    )

        return response.status_code, response.json()

    @staticmethod
    def find_pets_by_status(status):
        url = f'{BASE_URL}/pet/findByStatus'

        with allure.step(f"GET: Find pets by status (Request URL: {url})"):
            response = requests.get(url=url,
                                    headers=HEADER_ACCEPT,
                                    params={'status': status}
                                    )

        return response.status_code, response.json()

    @staticmethod
    def find_pet_by_id(pet_id):
        url = f'{BASE_URL}/pet/{pet_id}'

        with allure.step(f"GET: Find pet by ID (Request URL: {url})"):
            response = requests.get(url=url,
                                    headers=HEADER_ACCEPT
                                    )

        return response.status_code, response.json()

    @staticmethod
    def updates_pet_in_a_store(pet_id, name=None, status=None):
        url = f'{BASE_URL}/pet/{pet_id}'
        data = []
        if name:
            data.append(f'name={name}')
        if status:
            data.append(f'status={status}')

        with allure.step(f"POST: Updates a pet in the store with form data (Request URL: {url})"):
            response = requests.post(url=url,
                                     headers=HEADER_ACCEPT,
                                     data='&'.join(data)
                                     )

        return response.status_code, response.json()

    @staticmethod
    def delete_pet(pet_id):
        url = f'{BASE_URL}/pet/{pet_id}'

        with allure.step(f"DELETE: Delete a pet with ID = {pet_id} (Request URL: {url})"):
            response = requests.delete(url=url,
                                       headers=HEADER_ACCEPT
                                       )

        return response.status_code, response.json()
