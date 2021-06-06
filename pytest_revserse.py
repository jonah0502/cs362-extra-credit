import reverse_sentence

class TestClass:
    def test_empty(self):
        assert reverse_sentence.reverseSentence("") == ""

    def test_example(self):
        assert reverse_sentence.reverseSentence("My name is V Tadimeti") =="Tadimeti V is name My"
        
    def test_mytest(self):
        assert reverse_sentence.reverseSentence("hi my name is jonah") =="jonah is name my hi"