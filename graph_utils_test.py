

"""Unit tests for graph_utils.py."""
import unittest

from absl.testing import absltest # type: ignore
import graph_utils as gu # type: ignore


class GraphUtilsTest(unittest.TestCase):

  def test_cross(self):
    self.assertEqual(gu.cross([], [1]), [])
    self.assertEqual(gu.cross([1], []), [])
    self.assertEqual(gu.cross([1], [2]), [(1, 2)])
    self.assertEqual(gu.cross([1], [2, 3]), [(1, 2), (1, 3)])

    e1 = [1, 2, 3]
    e2 = [4, 5]
    target = [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
    self.assertEqual(gu.cross(e1, e2), target)

  def test_comb2(self):
    self.assertEqual(gu.comb2([]), [])
    self.assertEqual(gu.comb2([1]), [])
    self.assertEqual(gu.comb2([1, 2]), [(1, 2)])
    self.assertEqual(gu.comb2([1, 2, 3]), [(1, 2), (1, 3), (2, 3)])

  def test_comb3(self):
    self.assertEqual(gu.comb3([]), [])
    self.assertEqual(gu.comb3([1]), [])
    self.assertEqual(gu.comb3([1, 2]), [])
    self.assertEqual(gu.comb3([1, 2, 3]), [(1, 2, 3)])
    self.assertEqual(
        gu.comb3([1, 2, 3, 4]), [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
    )

  def test_comb4(self):
    self.assertEqual(gu.comb4([]), [])
    self.assertEqual(gu.comb4([1]), [])
    self.assertEqual(gu.comb4([1, 2]), [])
    self.assertEqual(gu.comb4([1, 2, 3]), [])
    self.assertEqual(gu.comb4([1, 2, 3, 4]), [(1, 2, 3, 4)])
    self.assertEqual(
        gu.comb4([1, 2, 3, 4, 5]),
        [(1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 4, 5), (1, 3, 4, 5), (2, 3, 4, 5)],
    )

  def test_perm2(self):
    self.assertEqual(gu.perm2([]), [])
    self.assertEqual(gu.perm2([1]), [])
    self.assertEqual(gu.perm2([1, 2]), [(1, 2), (2, 1)])
    self.assertEqual(
        gu.perm2([1, 2, 3]), [(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)]
    )

  def test_perm3(self):
    self.assertEqual(gu.perm3([]), [])
    self.assertEqual(gu.perm3([1]), [])
    self.assertEqual(gu.perm3([1, 2]), [])
    self.assertEqual(
        gu.perm3([1, 2, 3]),
        [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)],
    )
    self.assertEqual(
        gu.perm3([1, 2, 3, 4]),
        [
            (1, 2, 3),
            (1, 2, 4),
            (1, 3, 2),
            (1, 3, 4),
            (1, 4, 2),
            (1, 4, 3),
            (2, 1, 3),
            (2, 1, 4),
            (2, 3, 1),
            (2, 3, 4),
            (2, 4, 1),
            (2, 4, 3),
            (3, 1, 2),
            (3, 1, 4),
            (3, 2, 1),
            (3, 2, 4),
            (3, 4, 1),
            (3, 4, 2),
            (4, 1, 2),
            (4, 1, 3),
            (4, 2, 1),
            (4, 2, 3),
            (4, 3, 1),
            (4, 3, 2),
        ],
    )

  def test_perm4(self):
    self.assertEqual(gu.perm3([]), [])
    self.assertEqual(gu.perm3([1]), [])
    self.assertEqual(gu.perm3([1, 2]), [])
    self.assertEqual(gu.perm4([1, 2, 3]), [])
    self.assertEqual(
        gu.perm4([1, 2, 3, 4]),
        [
            (1, 2, 3, 4),
            (1, 2, 4, 3),
            (1, 3, 2, 4),
            (1, 3, 4, 2),
            (1, 4, 2, 3),
            (1, 4, 3, 2),  # pylint: disable=line-too-long
            (2, 1, 3, 4),
            (2, 1, 4, 3),
            (2, 3, 1, 4),
            (2, 3, 4, 1),
            (2, 4, 1, 3),
            (2, 4, 3, 1),  # pylint: disable=line-too-long
            (3, 1, 2, 4),
            (3, 1, 4, 2),
            (3, 2, 1, 4),
            (3, 2, 4, 1),
            (3, 4, 1, 2),
            (3, 4, 2, 1),  # pylint: disable=line-too-long
            (4, 1, 2, 3),
            (4, 1, 3, 2),
            (4, 2, 1, 3),
            (4, 2, 3, 1),
            (4, 3, 1, 2),
            (4, 3, 2, 1),
        ],  # pylint: disable=line-too-long
    )


if __name__ == '__main__':
  absltest.main()
