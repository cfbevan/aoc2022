from unittest import TestCase
from unittest import main

from .main import Stacks
from .main import pt1
from .main import pt2

input_diagram = '\n'.join([
    '    [D]',
    '[N] [C]',
    '[Z] [M] [P]',
    ' 1   2   3',
])

input = '\n'.join([
    input_diagram,
    '', 
    'move 1 from 2 to 1',
    'move 3 from 1 to 3',
    'move 2 from 2 to 1',
    'move 1 from 1 to 2'
])

class Testday05(TestCase):

    def test_stacks_parse_diagram(self):
        s = Stacks(input_diagram)
        self.assertEqual(s.stacks, {
            1: ['Z', 'N'],
            2: ['M', 'C', 'D'],
            3: ['P']
        })

    def test_move(self):
        s = Stacks(input_diagram)
        s.move('move 1 from 2 to 1')
        self.assertEqual(s.stacks, {
            1: ['Z', 'N', 'D'],
            2: ['M', 'C'],
            3: ['P']
        })
        s.move('move 3 from 1 to 3')
        self.assertEqual(s.stacks, {
            1: [],
            2: ['M', 'C'],
            3: ['P', 'D', 'N', 'Z']
        })
        s.move('move 2 from 2 to 1')
        self.assertEqual(s.stacks, {
            1: ['C', 'M'],
            2: [],
            3: ['P', 'D', 'N', 'Z']
        })
        s.move('move 1 from 1 to 2')
        self.assertEqual(s.stacks, {
            1: ['C'],
            2: ['M'],
            3: ['P', 'D', 'N', 'Z']
        })

    def test_move2(self):
        s = Stacks(input_diagram)
        s.move('move 1 from 2 to 1', True)
        self.assertEqual(s.stacks, {
            1: ['Z', 'N', 'D'],
            2: ['M', 'C'],
            3: ['P']
        })
        s.move('move 3 from 1 to 3', True)
        self.assertEqual(s.stacks, {
            1: [],
            2: ['M', 'C'],
            3: ['P', 'Z', 'N', 'D']
        })
        s.move('move 2 from 2 to 1', True)
        self.assertEqual(s.stacks, {
            1: ['M', 'C'],
            2: [],
            3: ['P', 'Z', 'N', 'D']
        })
        s.move('move 1 from 1 to 2', True)
        self.assertEqual(s.stacks, {
            1: ['M'],
            2: ['C'],
            3: ['P', 'Z', 'N', 'D']
        })

    def test_pt1(self):
        output = pt1(input)
        expected = 'CMZ'
        self.assertEqual(output, expected)

    def test_pt2(self):
        output = pt2(input)
        expected = 'MCD'
        self.assertEqual(output, expected)
        
if __name__ == '__main__':
    main()