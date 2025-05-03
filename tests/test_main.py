import sys
sys.path.append('../')

import unittest
from io import StringIO
from typing import List
from unittest.mock import patch
from scripts.main import IslandCounter  # Ensure to import IslandCounter from your file

class TestIslandCounter(unittest.TestCase):
    
    def setUp(self) -> None:
        """Set up any variables needed for the tests."""
        self.example_matrix_1 = [
            ["1", "1", "0", "0", "0"],
            ["0", "1", "0", "0", "1"],
            ["1", "0", "0", "1", "1"],
            ["0", "0", "0", "0", "0"],
            ["1", "0", "1", "0", "1"]
        ]
        self.example_matrix_2 = [
            ["1", "1", "1"],
            ["1", "0", "1"],
            ["1", "1", "1"]
        ]
        self.single_island = [["1"]]
        self.no_island = [["0", "0"], ["0", "0"]]
        self.invalid_characters = [["1", "0"], ["1", "x"]]
        self.empty_matrix: List[List[str]] = []

    def test_count_islands_example_1(self):
        """Test with example matrix 1 with 5 islands."""
        counter = IslandCounter(self.example_matrix_1)
        self.assertEqual(counter.count_islands(), 5)

    def test_count_islands_example_2(self):
        """Test with example matrix 2 with a single island."""
        counter = IslandCounter(self.example_matrix_2)
        self.assertEqual(counter.count_islands(), 1)

    def test_single_island(self):
        """Test with a single-cell island matrix."""
        counter = IslandCounter(self.single_island)
        self.assertEqual(counter.count_islands(), 1)

    def test_no_island(self):
        """Test with a matrix that has no islands."""
        counter = IslandCounter(self.no_island)
        self.assertEqual(counter.count_islands(), 0)

    def test_empty_matrix(self):
        """Test with an empty matrix."""
        counter = IslandCounter(self.empty_matrix)
        self.assertEqual(counter.count_islands(), 0)

    def test_invalid_characters(self):
        """Test matrix with invalid characters should raise ValueError."""
        with self.assertRaises(ValueError):
            counter = IslandCounter(self.invalid_characters)
            counter.count_islands()

    def test_from_file(self):
        """Test loading matrix from a file."""
        with open("test_input.txt", "w") as f:
            f.write("1 1 0\n0 1 1\n1 0 1")
        counter = IslandCounter.from_file("test_input.txt")
        self.assertEqual(counter.count_islands(), 1)

    def test_invalid_file_path(self):
        """Test invalid file path raises FileNotFoundError."""
        with self.assertRaises(FileNotFoundError):
            IslandCounter.from_file("invalid_file_path.doc")

    def test_main_output(self):
        """Test main function output to stdout."""
        matrix = [
            ["1", "1", "0"],
            ["0", "1", "0"],
            ["1", "0", "1"]
        ]
        counter = IslandCounter(matrix)
        expected_output = "1\n"
        with StringIO() as buf, patch('sys.stdout', buf):
            print(counter.count_islands())
            self.assertEqual(buf.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
