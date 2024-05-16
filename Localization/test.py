import unittest
import localization

class TestLocalization(unittest.TestCase):
    def assertAlmostEqualList(self, list1, list2, tol=0.001):
        self.assertEqual(len(list1), len(list2))
        for i in range(len(list1)):
            for j in range(len(list1[i])):
                self.assertAlmostEqual(list1[i][j], list2[i][j], delta=tol)

    def test_case1(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'G'],
                  ['G', 'G', 'G']]
        measurements = ['R']
        motions = [[0,0]]
        sensor_right = 1.0
        p_move = 1.0
        p = localization.localize(colors, measurements, motions, sensor_right, p_move, 0)
        self.assertEqual(p, [[0.0, 0.0, 0.0],
                             [0.0, 1.0, 0.0],
                             [0.0, 0.0, 0.0]])

    def test_case2(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R']
        motions = [[0,0]]
        sensor_right = 1.0
        p_move = 1.0
        p = localization.localize(colors, measurements, motions, sensor_right, p_move, 0)
        self.assertEqual(p, [[0.0, 0.0, 0.0],
                             [0.0, 0.5, 0.5],
                             [0.0, 0.0, 0.0]])
    def test_case3(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R', 'R']
        motions = [[0,0], [0,1]]
        sensor_right = 0.8
        p_move = 1.0
        p = localization.localize(colors, measurements, motions, sensor_right, p_move, 0)
        self.assertAlmostEqualList(p, [[0.03333333333, 0.03333333333, 0.03333333333],
                             [0.13333333333, 0.13333333333, 0.53333333333],
                             [0.03333333333, 0.03333333333, 0.03333333333]])

    def test_case4(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R', 'R']
        motions = [[0,0], [0,1]]
        sensor_right = 1.0
        p_move = 1.0
        p = localization.localize(colors, measurements, motions, sensor_right, p_move, 0)
        self.assertAlmostEqualList(p, [[0.0, 0.0, 0.0],
                             [0.0, 0.0, 1.0],
                             [0.0, 0.0, 0.0]])

    def test_case5(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R', 'R']
        motions = [[0,0], [0,1]]
        sensor_right = 0.8
        p_move = 0.5
        p = localization.localize(colors, measurements, motions, sensor_right, p_move, 0)
        self.assertAlmostEqualList(p, [[0.0289855072, 0.0289855072, 0.0289855072],
                             [0.0724637681, 0.2898550724, 0.4637681159],
                             [0.0289855072, 0.0289855072, 0.0289855072]])

    def test_case6(self):
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        measurements = ['R', 'R']
        motions = [[0,0], [0,1]]
        sensor_right = 1.0
        p_move = 0.5
        p = localization.localize(colors, measurements, motions, sensor_right, p_move, 0)
        self.assertAlmostEqualList(p, [[0.0, 0.0, 0.0],
                             [0.0, 0.33333333, 0.66666666],
                             [0.0, 0.0, 0.0]])

    def test_case7(self):
        colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
        measurements = ['R']
        motions = [[0,0]]
        sensor_right = 0.8
        p_move = 1.0
        p = localization.localize(colors, measurements, motions, sensor_right, p_move, 0)
        self.assertAlmostEqualList(p, [[0.06666666666, 0.06666666666, 0.06666666666],
     [0.06666666666, 0.26666666666, 0.26666666666],
     [0.06666666666, 0.06666666666, 0.06666666666]])

    def test_case8(self):
        colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
        measurements = ['G','G','G','G','G']
        motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
        sensor_right = 0.7
        p_move = 0.8
        p = localization.localize(colors, measurements, motions, sensor_right, p_move, 0)
        self.assertAlmostEqualList(p, [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
 [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
 [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
 [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]])

if __name__ == '__main__':
    unittest.main()
