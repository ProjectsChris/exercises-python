import unittest
import challenges.challenges


class TestShiftToRight(unittest.TestCase):
    num_vector = [[80, 3], [-24, 2], [-5, 1], [38, 0], [192, 4], [4666, 6], [3777, 6], [1024, 5], [-512, 10]]
    res_vector = [10, -6, -3, 38, 12, 72, 59, 32, -1]

    def test_shift_to_right(self):
        index = 0

        for i in range(len(self.num_vector)):
            self.assertEqual(challenges.challenges.shift_to_right(self.num_vector[index][0], self.num_vector[index][1]), self.res_vector[index])
            index += 1