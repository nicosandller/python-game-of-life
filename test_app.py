import unittest
from board import Board

game = Board(10)


class TestStringMethods(unittest.TestCase):

    def test_pos_to_analize(self):
        #We need to test that neither of the positions in the set that results from  pos_to_analize is outside dimensions
        xmax = game.dim
        ymax = game.dim
        #add a cell on the dimension limit (pos_to_analize should not return a pos outside dimensions)
        game.add_cell(pos=(game.dim ,game.dim))
        #test that cells being returned are inside dimensions
        for pos in game.pos_to_analize():
            self.assertTrue(pos[0] <= xmax and pos[1] <= ymax)


if __name__ == '__main__':
    unittest.main()
