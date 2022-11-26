import unittest

from translator import englishToFrench, frenchToEnglish

class TestMyFunc(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(None),None)
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish(None),'Soup')


       
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(None),None)
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(englishToFrench('sunrise'),'Lever du soleil')
        self.assertEqual(englishToFrench('sunrise'),'Lever du soleil')
        
if __name__ == '__main__':
    unittest.main()