import os
import json
import unittest

from smartbudget.file_io_module_3.json_io import (
    save_to_json,
    load_from_json,
    append_to_json,
    clear_json
)
from smartbudget.entity.income import Income
from smartbudget.entity.expense import Expense

TEST_FILE = "test_records.json"
class TestJsonIO(unittest.TestCase):

    def setUp(self):
        """Prepare a clean test environment before each test."""
        # Ensure the files/ directory exists
        if not os.path.exists("files"):
            os.makedirs("files")

        self.test_path = os.path.join("files", TEST_FILE)

        # Remove the test file if it already exists
        if os.path.exists(self.test_path):
            os.remove(self.test_path)

    def tearDown(self):
        """Clean up the test file after each test."""
        if os.path.exists(self.test_path):
            os.remove(self.test_path)

    # Test save_to_json()
    def test_save_to_json(self):
        """Test that save_to_json correctly writes JSON output."""
        income = Income("Salary", 5000, "Job")
        save_to_json([income], filename=TEST_FILE)

        # 1. The JSON file should be created
        self.assertTrue(os.path.exists(self.test_path))

        # 2. The file contents should match the expected structure
        with open(self.test_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Salary")
        self.assertEqual(data[0]["amount"], 5000)
        self.assertEqual(data[0]["type"], "Income")

    # Test load_from_json()
    def test_load_from_json(self):
        """Test that load_from_json correctly reconstructs objects."""
        
        income = Income("Bonus", 3000, "Job")
        save_to_json([income], filename=TEST_FILE)

        # Load the JSON back into Python objects
        results = load_from_json(filename=TEST_FILE)

        # 1. Should return a list with one item
        self.assertEqual(len(results), 1)

        # 2. Should be an Income instance
        self.assertIsInstance(results[0], Income)

        # 3. Check fields
        self.assertEqual(results[0].name, "Bonus")
        self.assertEqual(results[0].amount, 3000)
        self.assertEqual(results[0].source, "job")

    # Test append_to_json()
    def test_append_to_json(self):
        """Test that append_to_json correctly appends new records."""

        income1 = Income("Salary", 5000, "Work")
        income2 = Income("Bonus", 2000, "Job")

        # 1. Save first record
        save_to_json([income1], filename=TEST_FILE)

        # 2. Append second record
        append_to_json([income2], filename=TEST_FILE)

        # 3. Load all results
        results = load_from_json(filename=TEST_FILE)

        # Expect 2 records
        self.assertEqual(len(results), 2)

        # First record should match income1
        self.assertEqual(results[0].name, "Salary")
        self.assertEqual(results[0].amount, 5000)

        # Second record should match income2
        self.assertEqual(results[1].name, "Bonus")
        self.assertEqual(results[1].amount, 2000)

    # Test clear_json()
    def test_clear_json(self):
        """Test that clear_json resets the JSON file to an empty list."""

        # Write some initial records
        income = Income("Gift", 100, "Friend")
        save_to_json([income], filename=TEST_FILE)

        # Clear the JSON file
        clear_json(filename=TEST_FILE)

        # Load results
        results = load_from_json(filename=TEST_FILE)

        # Should be completely empty
        self.assertEqual(results, [])

