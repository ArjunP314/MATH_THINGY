

"""Unit testing for the trace_back code."""

import unittest

from absl.testing import absltest # type: ignore
import ddar # type: ignore
import graph as gh # type: ignore
import problem as pr # type: ignore
import trace_back as tb # type: ignore


class TracebackTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.defs = pr.Definition.from_txt_file('defs.txt', to_dict=True)
    cls.rules = pr.Theorem.from_txt_file('rules.txt', to_dict=True)

  def test_orthocenter_dependency_difference(self):
    txt = 'a b c = triangle a b c; d = on_tline d b a c, on_tline d c a b; e = on_line e a c, on_line e b d ? perp a d b c'  # pylint: disable=line-too-long
    p = pr.Problem.from_txt(txt)
    g, _ = gh.Graph.build_problem(p, TracebackTest.defs)

    ddar.solve(g, TracebackTest.rules, p)

    goal_args = g.names2nodes(p.goal.args)
    query = pr.Dependency(p.goal.name, goal_args, None, None)

    setup, aux, _, _ = tb.get_logs(query, g, merge_trivials=False)

    # Convert each predicates to its hash string:
    setup = [p.hashed() for p in setup]
    aux = [p.hashed() for p in aux]

    self.assertCountEqual(
        setup, [('perp', 'a', 'c', 'b', 'd'), ('perp', 'a', 'b', 'c', 'd')]
    )

    self.assertCountEqual(
        aux, [('coll', 'a', 'c', 'e'), ('coll', 'b', 'd', 'e')]
    )


if __name__ == '__main__':
  absltest.main()
