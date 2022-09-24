﻿import unittest
from unittest.mock import Mock, patch
from mlbstatsapi.mlb import *


class TestPerson(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_player_instance_type_error(self): 
         with self.assertRaises(TypeError):
            player = Person()

    def test_player_instance_position_arguments(self):        
        player = Person(664034, "Ty France", "/api/v1/people/664034")
        self.assertEqual(player.id, 664034)
        self.assertIsInstance(player, Person)
        self.assertEqual(player.full_name, "Ty France")
        self.assertEqual(player.link, "/api/v1/people/664034")

    def test_player_base_class(self):
        player = Person(664034, "Ty France", "/api/v1/people/664034")
        self.assertIsInstance(player, MlbObject)

    def test_player_base_class_attributes(self):
        player = Person(664034, "Ty France", "/api/v1/people/664034")
        self.assertTrue(hasattr(player, "_load_stats"))

    def test_player_generate_stats(self):
        player = Person(664034, "Ty France", "/api/v1/people/664034")
        self.assertTrue(hasattr(player, "_load_stats"))
        player.generate_stats()
        self.assertTrue(hasattr(player, "stats"))
        self.assertIsInstance(player.stats, List)
        self.assertIsInstance(player.stats[0], Stats)
    

    # def test_player_preload_instance(self):
    #     player = Person(664034, "Ty France", "/api/v1/people/664034", preload=True)
    #     self.assertIsInstance(player.stats[0], Stats)