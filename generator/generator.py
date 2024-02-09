import random

from data.data import Person
from faker import Faker

faker = Faker('en_GB')
Faker.seed()


def generated_person():
    yield Person(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        full_name= faker.first_name() + " " + faker.last_name(),
        age= random.randint(18,80),
        salary=random.randint(100,320),
        department=faker.job(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address(),
    )
