import unittest
from password_generator import (
    generate_password,
    validate_password,
    rule_has_upper,
    rule_has_lower,
    rule_has_digit,
    rule_has_symbol,
)


class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        password = generate_password(10, True, False, False, False)
        self.assertEqual(len(password), 10)

    def test_digits_only(self):
        password = generate_password(8, False, False, True, False)
        self.assertTrue(password.isdigit())

    def test_multiple_rules(self):
        password = generate_password(20, True, True, True, True)
        rules = [rule_has_upper, rule_has_lower, rule_has_digit, rule_has_symbol]
        self.assertTrue(validate_password(password, rules))

    def test_no_types_selected(self):
        password = generate_password(8, False, False, False, False)
        self.assertIsNone(password)


if __name__ == "__main__":
    unittest.main()