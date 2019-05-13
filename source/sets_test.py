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
    assert st.size == 4

if __name__ == '__main__':
    unittest.main()