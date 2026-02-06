# test_evmhorizon.py
"""
Tests for evmHorizon module.
"""

import unittest
from evmhorizon import evmHorizon

class TestevmHorizon(unittest.TestCase):
    """Test cases for evmHorizon class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = evmHorizon()
        self.assertIsInstance(instance, evmHorizon)
        
    def test_run_method(self):
        """Test the run method."""
        instance = evmHorizon()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
