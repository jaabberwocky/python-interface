from interfaceproject.project_classes import Dog


def test_dog_name():
    d = Dog('James')
    assert d.get_type() == 'Dog'
