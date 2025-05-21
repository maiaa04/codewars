import itertools
import unittest


def permutations(string):
    result = []
    p = itertools.permutations(string)
    for x in list(p):
        result.append(''.join(x))
    return set(result)


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(sorted(permutations('a')), ['a'])
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        self.assertEqual(sorted(permutations('aabb')), [
                         'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])


if __name__ == '__main__':
    unittest.main()
