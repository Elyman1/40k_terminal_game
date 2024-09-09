import pytest
import logging
from unittest.mock import patch

from classes.epic_hero import EpicHero
from classes.attack import Attack
from classes.exceptions import CustomException
from classes.strategem import Strategem

from fixtures.fixtures import (
    oltyx, autarch, grot, tachyon_arrow, voidscythe, deathspinner, stubber, buff_strength
    )


class TestEpicHeroAttributes:
    def test_hero_initialised_with_correct_attributes(self, oltyx):
        assert oltyx.name == "Oltyx"
        assert oltyx.faction == "Necrons"
        assert oltyx.wounds == 10
        assert oltyx.toughness == 6
        assert oltyx.strategems == ["Resurrection Orb"]
        assert oltyx.invulnerable_save == 4
        assert oltyx.cp == 0

    def test_wrong_types_cant_be_used_in_attributes(self):
        with pytest.raises(TypeError):
            oltyx = EpicHero([["Oltyx"], ["Necrons"],
            {["Tachyon Arrow", "Voidscythe"]}, '10', '5', '6',{["Resurrection Orb"]}, '0'])

class TestTakeDamage:
    def test_hero_can_take_damage(self, oltyx):
        oltyx.take_damage(1)
        assert oltyx.wounds < 10

class TestUseAttack:
    def test_use_attack_lowers_opponents_health(self, oltyx, autarch, voidscythe):
        oltyx.use_attack(voidscythe, autarch)
        assert autarch.wounds < 7

class TestIsAlive:
    def test_is_alive_returns_true_when_alive(self, oltyx):
        assert oltyx.is_alive() == True

    def test_is_alive_returns_false_when_dead(self, oltyx):
        oltyx.take_damage(10)
        assert oltyx.is_alive() == False

class TestGainCP:
    def test_incraments_cp(self, oltyx):
        oltyx.gain_cp()
        assert oltyx.cp > 0

    def test_cp_cant_go_above_6(self, oltyx):
        oltyx.cp = 6
        oltyx.gain_cp()
        assert oltyx.cp == 6
        
class TestDetermineHitNeeded:
    def test_strength_double_toughness(self, oltyx, grot, voidscythe):
        assert oltyx.determine_hit_roll_needed(grot, voidscythe) == 2

    def test_strength_higher_than_toughness(self, oltyx, autarch, voidscythe):
        assert oltyx.determine_hit_roll_needed(autarch, voidscythe) == 3

    def test_strength_equal_to_toughness(self, oltyx, autarch, tachyon_arrow):
        assert oltyx.determine_hit_roll_needed(autarch, tachyon_arrow) == 4

    def test_strength_lower_than_toughness(self, grot, autarch, stubber):
        assert grot.determine_hit_roll_needed(autarch, stubber) == 5

    def test_strength_half_toughness(self, grot, oltyx, stubber):
        assert grot.determine_hit_roll_needed(oltyx, stubber) == 6

class TestRollDice:
    def test_returns_a_list(self, oltyx):
        assert type(oltyx.roll_dice(1)) == list

import unittest
from io import StringIO
from unittest.mock import patch

class TestExceptionHandling:
    def test_wrong_argument_type_in_determine_hit_roll_attack(
            self, grot, oltyx, stubber
            ):
        with patch('logging.error') as mock_log_error:
            oltyx.determine_hit_roll_needed(grot.name, stubber)
            mock_log_error.assert_called_once_with(
                "Wrong argument type given to 'determine_hit_roll_' function"
                )

    def test_wrong_argument_type_in_determine_hit_roll_target(
            self, grot, oltyx, stubber
            ):
        with patch('logging.error') as mock_log_error:
            oltyx.determine_hit_roll_needed(grot, stubber.name)
            mock_log_error.assert_called_once_with(
                "Wrong argument type given to 'determine_hit_roll_' function"
                )
            
    