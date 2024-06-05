from faker.providers import BaseProvider

class MedicineProvider(BaseProvider):
    def medicine(self):
        medicines = [
            'Paracetamol', 'Ibuprofen', 'Amoxicillin', 'Ciprofloxacin',
            'Metformin', 'Amlodipine', 'Atorvastatin', 'Omeprazole'
        ]
        return self.random_element(medicines)
