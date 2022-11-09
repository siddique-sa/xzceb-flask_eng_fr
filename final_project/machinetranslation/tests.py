import unittest

from translator import english_to_french, french_to_english

class TestMyTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french(""),"")
        self.assertEqual(english_to_french("Hello"),"Bonjour")

    def test_f2e(self):
        self.assertEqual(french_to_english(""),"")
        self.assertEqual(french_to_english("Bonjour"),"Hello")

unittest.main()