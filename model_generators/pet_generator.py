import random

from faker import Faker

from model_generators.category_generator import CategoryGenerator
from model_generators.tag_generator import TagGenerator
from models.pet import statuses


class PetGenerator:

    @staticmethod
    def generate_new_pet():
        fake = Faker()

        pet = dict()
        pet['id'] = fake.random_number()
        pet['category'] = CategoryGenerator.generate_new_category()
        pet['name'] = fake.name()
        pet['photoUrls'] = [fake.image_url()]
        pet['tags'] = [TagGenerator.generate_new_tag()]
        pet['status'] = random.choice(statuses)

        return pet
