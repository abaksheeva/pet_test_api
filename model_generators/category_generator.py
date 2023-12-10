from faker import Faker


class CategoryGenerator:

    @staticmethod
    def generate_new_category():
        fake = Faker()
        return {
            'id': fake.random_number(),
            'name': fake.name()
        }
