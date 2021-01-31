from abc import ABCMeta, abstractmethod


class MetaAnimalInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_type(self) -> str:
        "Returns type of animal."
        pass

    @abstractmethod
    def pet_animal(self) -> str:
        "Returns response to petting."
        pass


class NotFullyImplementedDog(MetaAnimalInterface):
    def __init__(self, name: str):
        self.name = name
        self.animal_type = 'Dog'

    # def get_type(self) -> str:
    #     "Returns type of animal."
    #     return self.animal_type

    def pet_animal(self) -> str:
        "Returns response to petting."
        return "Woof"


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
