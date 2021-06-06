import reverse_sentence
import unittest



class sentenceTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse_sentence.reverseSentence(""),"")
    def test_example(self):
        self.assertEqual(reverse_sentence.reverseSentence("My name is V Tadimeti"),"Tadimeti V is name My")
    def test_mytest(self):
        self.assertEqual(reverse_sentence.reverseSentence("hi I'm Jacob"),"Jacob I'm hi")
    
if __name__ == "__main__":
    unittest.main()