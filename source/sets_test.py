from sets import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class SetTest(unittest.TestCase):

  def test_init(self):
    st = Set(['A', 'B', 'C'])
    assert st.size == 3

  def test_add(self):
    st = Set(['A', 'B', 'C'])
    assert st.size == 3
    st.add('D')
    assert st.size == 4

  def test_remove(self):
    st = Set(['A', 'B', 'C'])
    assert st.size == 3
    st.remove('C')
    assert st.size == 2

  def test_contains(self):
    st = Set(['A', 'B', 'C'])
    assert st.contains('A') == True
    assert st.contains('Z') == False

  def test_union(self):
    st = Set(['A', 'B', 'C'])
    other_st = Set(['Z', 'Y', 'X'])
    new_st = st.union(other_st)
    assert new_st.contains('A') == True
    assert new_st.contains('Z') == True

  def test_difference(self):
    st = Set(['A', 'B', 'C', 'D', 'E'])
    other_st = Set(['A', 'B', 'C', 'F', 'G'])
    difference = st.difference(other_st)
    assert difference.contains('D') == True
    assert difference.contains('E') == True
    assert difference.contains('F') == True
    assert difference.contains('G') == True

  def test_is_subset(self):
    st = Set(['A', 'B', 'C', 'D', 'E'])
    other_st = Set(['B', 'C', 'D'])
    assert other_st.is_subset(st) == True
    other_st = Set(['B', 'C', 'F'])
    assert other_st.is_subset(st) == False

if __name__ == '__main__':
    unittest.main()