import faker

def get_registration_data():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    return name, email




