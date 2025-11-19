import unittest
import re

TIME_PATTERN = r"\b(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d\b"
TIME_REGEX = re.compile(TIME_PATTERN)


class TestTimeRegex(unittest.TestCase):

    def test_valid_times(self):
        valid = ["00:00:00", "01:23:45", "09:05:03", "12:34:56", "23:59:59"]
        for t in valid:
            with self.subTest(time=t):
                self.assertTrue(TIME_REGEX.fullmatch(t))

    def test_invalid_times(self):
        invalid = ["24:00:00", "12:60:00", "12:34:61", "9:30:45", "09:5:03"]
        for t in invalid:
            with self.subTest(time=t):
                self.assertIsNone(TIME_REGEX.fullmatch(t))

    def test_find_in_text(self):
        text = "08:15:30 и 23:59:59 — корректно."
        self.assertEqual(TIME_REGEX.findall(text), ["08:15:30", "23:59:59"])

    def test_no_false_positives(self):
        text = "192.168.001.001 содержит 001, но не время."
        self.assertEqual(TIME_REGEX.findall(text), [])

    def test_edge_cases_hours(self):
        self.assertTrue(TIME_REGEX.fullmatch("00:00:00"))
        self.assertTrue(TIME_REGEX.fullmatch("23:59:59"))
        self.assertIsNone(TIME_REGEX.fullmatch("24:00:00"))

    def test_leading_zero_requirement(self):
        self.assertIsNone(TIME_REGEX.fullmatch("9:05:03"))
        self.assertIsNone(TIME_REGEX.fullmatch("09:5:03"))
        self.assertIsNone(TIME_REGEX.fullmatch("09:05:3"))
