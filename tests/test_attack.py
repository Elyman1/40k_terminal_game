import pytest

from classes.epic_hero import EpicHero
from classes.attack import Attack
from classes.exceptions import CustomException


@pytest.fixture
def voidscythe():
    return Attack("Voidscythe", "Melee", 3, 12, 4)

@pytest.fixture
def tachyon_arrow():
    return Attack("Tachyon Arrow", "Ranged", 1, 4, 10)

@pytest.fixture
def deathspinner():
    return Attack("Death Spinner", "Ranged", 5, 4, 1)

@pytest.fixture
def stubber():
    return Attack("Stubber", "Ranged", 3, 3, 1)

@pytest.fixture
def oltyx():
    return EpicHero("Oltyx", "Necrons",
           ["Tachyon Arrow", "Voidscythe"], 10, 6, ["Resurrection Orb"], 4, 0)

@pytest.fixture
def autarch():
    return EpicHero("Autarch", "Aeldari",
            ["Death Spinner", "Star Glaive"], 7, 4, ["Path of Command"], 4, 0)

@pytest.fixture
def grot():
    return EpicHero("Grot", "Orks", ["Stubber"], 2, 3, ["Waagh"], 0, 0)

class TestAttackAttributes:
    def test_hero_initialised_with_correct_attributes(self, voidscythe):
        assert voidscythe.name == "Voidscythe"
        assert voidscythe.attack_type == "Melee"
        assert voidscythe.num_attacks == 3
        assert voidscythe.attack_strength == 12
        assert voidscythe.damage == 4