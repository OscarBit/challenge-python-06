def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    return lambda x: x / n


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):
        def test_closure_make_division_by(self):
            self.assertEqual(6, make_division_by(3)(18))
            self.assertEqual(20, make_division_by(5)(100))
            self.assertEqual(3, make_division_by(18)(54))
    
    unittest.main()
    
    run()
