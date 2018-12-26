import unittest

from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
  """
  Fibonacci numbers test class.
  """

  def setUp(self):
    """ Initialise test suite - no-op. """
    pass

  def tearDown(self):
    """ Clean up test suite - no-op. """
    pass

  def test_fibonacci0(self):
    """ Test fibonacci(0). """
    self.assertEqual(0, fibonacci(0))

  def test_fibonacci1(self):
    """ Test fibonacci(1). """
    self.assertEqual(1, fibonacci(1))

  def test_fibonacci2(self):
    """ Test fibonacci(2). """
    self.assertEqual(1, fibonacci(2))

  def test_fibonacci3(self):
    """ Test fibonacci(3). """
    self.assertEqual(2, fibonacci(3))

  def test_fibonacci30(self):
    """ Test fibonacci(30). """
    self.assertEqual(832040, fibonacci(30))

if __name__ == '__main__':
  unittest.main()