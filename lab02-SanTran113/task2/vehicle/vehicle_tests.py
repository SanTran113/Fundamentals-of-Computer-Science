#San Tran
import unittest
import vehicle

class VehicleTests(unittest.TestCase):
   def test_vehicle(self):
      result = vehicle.Vehicle(4.0, 6.0, 4, True)
      self.assertEqual(result.wheels, 4.0)
      self.assertEqual(result.fuel, 6.0)
      self.assertEqual(result.doors, 4)
      self.assertTrue(result.roof, True)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

