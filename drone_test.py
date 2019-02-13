import unittest, utility

class TestStringMethods(unittest.TestCase):

    def test_extract_words_and_integers_from_string(self):
        result = utility.extract_words_and_integers_from_string("I12am34Jesse")
        expected = (["I", "am","Jesse"], [12,34])
        self.assertEqual(result,expected)

    def test_cardinal_to_2d_cartesian_coordinates(self):
        self.assertEqual(utility.cardinal_to_2d_cartesian_coordinates("N34W23"), [-23,34])

    def test_time_traveled_by_drone_in_minutes(self):
        origin = [1,3]
        destination = [4,7]
        speed = [1,1]
        result = utility.time_traveled_by_drone_in_minutes(origin,destination,speed)
        expected = 7
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()