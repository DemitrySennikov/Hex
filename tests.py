import unittest


from team import Team as T
from field import Field
from moves import move


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.field = Field(5, T.AI)
    
    def test_empty(self):
        self.assertFalse(self.field.is_team_win(T.player))
        self.assertFalse(self.field.is_team_win(T.AI))
    
    def test_after_move(self):
        self.field.try_move(T.player, 3, 1)
        self.assertFalse(self.field.is_team_win(T.player))
        self.assertFalse(self.field.is_team_win(T.AI))
        self.field.try_move(T.AI, 3, 3)
        self.assertFalse(self.field.is_team_win(T.player))
        self.assertFalse(self.field.is_team_win(T.AI))

    def test_win(self):
        self.field.try_move(T.player, 1, 1)
        self.field.try_move(T.player, 2, 1)
        self.field.try_move(T.player, 3, 1)
        self.field.try_move(T.player, 4, 1)
        self.field.try_move(T.player, 5, 1)
        self.assertTrue(self.field.is_team_win(T.player))

    def test_move_to_owned(self):
        self.assertTrue(self.field.try_move(T.AI, 3, 3))
        self.assertFalse(self.field.try_move(T.AI, 3, 3))
        self.assertFalse(self.field.try_move(T.player, 3, 3))
        
    def test_move_out_of_field(self):
        self.assertFalse(self.field.try_move(T.AI, 0, 3))
        self.assertFalse(self.field.try_move(T.AI, 6, 3))
        self.assertFalse(self.field.try_move(T.AI, 3, 0))
        self.assertFalse(self.field.try_move(T.AI, 3, 6))

    def test_clever_AI(self):
        self.field.try_move(T.player, 1, 3)
        self.field.try_move(T.player, 1, 4)
        self.field.try_move(T.player, 2, 4)
        self.field.try_move(T.player, 3, 4)
        self.field.try_move(T.player, 5, 2)
        self.field.try_move(T.AI, 2, 1)
        self.field.try_move(T.AI, 2, 2)
        self.field.try_move(T.AI, 3, 2)
        self.field.try_move(T.AI, 4, 4)
        self.field.try_move(T.AI, 4, 5)
        hex, _, _, _ = move(T.AI, self.field, None)
        if hex is None:
            self.fail()
        self.field.try_move(T.AI, hex.x, hex.y)
        self.assertTrue(self.field.is_team_win(T.AI))
