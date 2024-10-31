import time
import unittest

class TestTimeMeasurement(unittest.TestCase):
    def test_measurement(self):
        @measure_time
        def fast_function():
            return 42

        result = fast_function()
        self.assertEqual(result, 42)

if __name__ == '__main__':
    unittest.main()

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання функції {func.__name__}: {end_time - start_time:.5f} секунд")
        return result
    return wrapper