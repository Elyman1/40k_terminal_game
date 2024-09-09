import pytest
import logging
from unittest.mock import patch

from classes.epic_hero import EpicHero
from classes.attack import Attack
from classes.exceptions import CustomException
from classes.strategem import Strategem, BuffStrength

from fixtures.fixtures import (
    oltyx, autarch, grot, tachyon_arrow, voidscythe, deathspinner, stubber, buff_strength
    )

class TestStrategemAttributes:
    def test_initialised_with_correct_attributes(self, buff_strength, oltyx):
        assert isinstance(buff_strength.target, EpicHero)
        assert buff_strength.name == "Buff Strength"
        assert buff_strength.description == "Increases target strength by 1"
        assert buff_strength.cp_cost == 1

class TestStrategemBasicFuntionality:
    def test_user_cp_decrements(self, buff_strength):
        buff_strength = BuffStrength
        buff_strength.activate(oltyx)

        

