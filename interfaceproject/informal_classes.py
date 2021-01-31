class MetaAnimalInterface:
    # uses an informal interface
    # does not enforce that all child classes must implement all methods

    def __init__(self, name: str):
        pass

    def get_type(self) -> str:
        "Returns type of animal."
        pass

    def pet_animal(self) -> str:
        "Returns response to petting."
        pass


class Dog(MetaAnimalInterface):
    def __init__(self, name: str):
        self.name = name
        self.animal_type = 'Dog'

    def get_type(self) -> str:
        "Returns type of animal."
        return self.animal_type

    def pet_animal(self) -> str:
        "Returns response to petting."
        return "Woof"
