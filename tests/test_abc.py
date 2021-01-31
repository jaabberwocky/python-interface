from interfaceproject.abc_classes import MetaAnimalInterface
from interfaceproject.abc_classes import NotFullyImplementedDog, Dog
import pytest


def test_not_implemented_base():
    with pytest.raises(TypeError):
        m = MetaAnimalInterface() # noqa


def test_not_implemented_dog():
    with pytest.raises(TypeError):
        d = NotFullyImplementedDog('James') # noqa


def test_get_type():
    d = Dog('James')
    assert d.get_type() == 'Dog'


def test_pet():
    d = Dog('James')
    assert d.pet_animal() == 'Woof'
