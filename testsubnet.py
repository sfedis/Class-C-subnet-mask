import unittest
import subnets

class TestSubnets(unittest.TestCase):

    def test_isMask(self):
        testString = "255.255.255."
        
        for i in range(256, 5000, 1):
            self.assertFalse(subnets.isMask(testString + f"{i}"))

        for i in range(-5000, -1, 1):
            self.assertFalse(subnets.isMask(testString + f"{i}"))

        for i in range(-3000, 25, 1):
            self.assertFalse(subnets.isMask(testString + f"{i}"))

        for i in range(3000, 30, 1):
            self.assertFalse(subnets.isMask(testString + f"{i}"))

if __name__ == '__main__':
    unittest.main()