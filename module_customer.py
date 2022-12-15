class Customer:
    def __init__(self, surname, name, email, contact_phone_number):
        self.surname = surname
        self.name = name
        self.email = email
        self.contact_phone_number = contact_phone_number

    def __str__(self):
        return f'{self.name} {self.surname}\n{self.email}\n{self.contact_phone_number}'