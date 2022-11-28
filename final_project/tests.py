import unittest

#from translator import english_to_french, french_to_english
from machinetranslation.translator import english_to_french, french_to_english

class TestMyFunc(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english(None),None)
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        
        self.assertNotEqual(french_to_english('Bonjour'),'Potato')

    def test_english_to_french(self):
        self.assertEqual(english_to_french(None),None)
        self.assertEqual(english_to_french('Hello'),'Bonjour')

        self.assertNotEqual(english_to_french('Hello'),'Potato')
        
if __name__ == '__main__':
    unittest.main()