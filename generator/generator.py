import os
import random

from data.data import Person
from faker import Faker

faker = Faker('en_GB')
Faker.seed()


def generated_person():
    yield Person(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        full_name=faker.first_name() + " " + faker.last_name(),
        age=random.randint(18, 80),
        salary=random.randint(100, 320),
        department=faker.job(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address(),
        mobile=faker.msisdn(),
    )


def generated_file():

    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Construct the relative path to the file
    file_name = f'filetest{random.randint(0,228)}.txt'
    path = os.path.join(current_directory, file_name)
    file = open(path, 'w+')
    file.write(f'Hi There{random.randint(1, 100)}')
    file.close()
    return file.name, path
