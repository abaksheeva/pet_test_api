from faker import Faker


class TagGenerator:

    @staticmethod
    def generate_new_tag():
        fake = Faker()
        return {
            'id': fake.random_number(),
            'name': fake.word()
        }
