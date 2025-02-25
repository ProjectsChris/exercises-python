import random
import unittest

from challenges import challenges


class TestShiftToRight(unittest.TestCase):
    num_vector = [[80, 3], [-24, 2], [-5, 1], [38, 0], [192, 4], [4666, 6], [3777, 6], [1024, 5], [-512, 10]]
    res_vector = [10, -6, -3, 38, 12, 72, 59, 32, -1]

    def test_shift_to_right(self):
        for i in range(len(self.num_vector)):
            self.assertEqual(challenges.shift_to_right(self.num_vector[i][0], self.num_vector[i][1]), self.res_vector[i])


class TestNumberLength(unittest.TestCase):
    numbers = [10, 5000, 0, 4039182, 9999999999999999, 1, 777777777777777777777777777777]
    length = [2, 4, 1, 7, 16, 1, 30]

    def test_number_length(self):
        for i in range(len(self.numbers)):
            self.assertEqual(challenges.number_length(self.numbers[i]), self.length[i])

class TestFindingAdjacentNodes(unittest.TestCase):
    matrix = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]

    def test_finding_adjacent_nodes(self):
        self.assertEqual(challenges.finding_adjacent_nodes(self.matrix, 0, 1), True)
        self.assertEqual(challenges.finding_adjacent_nodes(self.matrix, 0, 2), False)
        self.assertEqual(challenges.finding_adjacent_nodes(self.matrix, 2, 1), True)