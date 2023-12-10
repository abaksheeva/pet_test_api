import random

from faker import Faker

from model_generators.category_generator import CategoryGenerator
from model_generators.tag_generator import TagGenerator
from models.pet import statuses


class PetGenerator:

    def __init__(self):
        self.pet = dict()

    def generate_new_pet(self):
        fake = Faker()

        self.pet = dict()
        self.pet['id'] = fake.random_number()
        self.pet['category'] = CategoryGenerator.generate_new_category()
        self.pet['name'] = fake.name()
        self.pet['photoUrls'] = [fake.image_url()]
        self.pet['tags'] = [TagGenerator.generate_new_tag()]
        self.pet['status'] = random.choice(statuses)

        return self.pet
