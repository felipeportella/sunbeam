import unittest
import sunbeam

class TestState(unittest.TestCase):

    spe3 = None

    def setUp(self):
        if self.spe3 is None:
            self.spe3 = sunbeam.parse('spe3/SPE3CASE1.DATA')
        self.state = self.spe3

    def test_repr_title(self):
        self.assertTrue('EclipseState' in repr(self.state))
        self.assertEqual('SPE 3 - CASE 1', self.state.title)

    def test_state_nnc(self):
        self.assertFalse(self.state.has_input_nnc())

    def test_grid(self):
        self.assertEqual(9, self.state.getNX())
        self.assertEqual(9, self.state.getNY())
        self.assertEqual(4, self.state.getNZ())
        self.assertEqual(9*9*4, self.state.nactive())
        self.assertEqual(9*9*4, self.state.cartesianSize())
        g,i,j,k = 295,7,5,3
        self.assertEqual(g, self.state.globalIndex(i,j,k))
        self.assertEqual((i,j,k), self.state.getIJK(g))
