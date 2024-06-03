from faker.providers import BaseProvider

class IndianPhoneNumberProvider(BaseProvider):
    def indian_phone_number(self):
        return "+91 " + "".join([str(self.generator.random.randint(0, 9)) for _ in range(10)])
