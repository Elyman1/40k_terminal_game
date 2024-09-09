import pytest
import logging
from unittest.mock import patch

from classes.epic_hero import EpicHero
from classes.attack import Attack
from classes.exceptions import CustomException
from classes.strategem import Strategem


@pytest.fixture
def voidscythe():
    return Attack("Voidscythe", "Melee", 3, 7, 4)

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


def effect(target):
    target.strength += 1

@pytest.fixture
def buff_strength(oltyx):
    return Strategem(oltyx, "Buff Strength", "Increases target strength by 1",
                     effect, 1)

