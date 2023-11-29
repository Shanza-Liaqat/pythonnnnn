class Person:
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address

    # Getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_address(self):
        return self._address

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_address(self, address):
        self._address = address

def main():
    # Creating an instance of the Person class
    person = Person(name="John Doe", age=25, address="123 Main Street")

    # Getting and printing initial values
    print("Initial values:")
    print("Name:", person.get_name())
    print("Age:", person.get_age())
    print("Address:", person.get_address())

    # Changing values using setter methods
    person.set_name("Jane Doe")
    person.set_age(30)
    person.set_address("456 Oak Avenue")

    # Getting and printing updated values
    print("\nUpdated values:")
    print("Name:", person.get_name())
    print("Age:", person.get_age())
    print("Address:", person.get_address())

if __name__ == "__main__":
    main()
