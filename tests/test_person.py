﻿# import unittest
# from unittest.mock import Mock, patch
# from mlbstatsapi.person import Person


# class TestPerson(unittest.TestCase):
#     # @classmethod
#     # def setUpClass(cls) -> None:
#     #     cls.mock_get_patcher = patch('src.mlb.requests.get')
#     #     cls.mock_get = cls.mock_get_patcher.start()

#     # @classmethod
#     # def tearDownClass(cls) -> None:
#     #     cls.mock_get_patcher.stop()

#     def test_player_instance_type_error(self): 
#         with self.assertRaises(TypeError):
#             player = Person()

#     def test_player_instance_id_instance_success(self):        
#         player = Person(664034)
#         self.assertEqual(player.id, 664034)
#         self.assertIsInstance(player, Person)

    