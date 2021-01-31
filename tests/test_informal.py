from interfaceproject.informal_classes import Dog


def test_dog_name():
    d = Dog('James')
    assert d.get_type() == 'Dog'


def test_dog_pet():
    d = Dog('James')
    assert d.pet_animal() == 'Woof'
