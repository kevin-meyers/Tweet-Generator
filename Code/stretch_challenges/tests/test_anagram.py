from .lib import anagram

def test_make_anagram():
    assert anagram.make_anagram('please work') in ['work please', 'please work']
    assert anagram.make_anagram('hey') in ['hey', 'ehy', 'yeh', 'yhe', 'eyh', 'hye']


test_make_anagram()
