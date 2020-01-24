# OBJECTIVES:
#
# 1) make sure that we can initialize / instantiate our Team class
#
# 2) make sure that the Team class' .full_name property behaves as desired
#
import unittest

from app.team import Team
from app.team import BaseballTeam

class TestTeams(unittest.TestCase):

    def test_full_name(self):
        team = Team("New York", "Giants", [], "Derek Jeter")
        self.assertEqual(team.full_name, "New York Giants")

    def test_hr(self):
        #assignment 4 test
        baseball_team = BaseballTeam("New York", "Yankees", [], "Derek Jeter", "Clayton Kershaw")
        #self.assertEqual(baseball_team.homerun, "Derek Jeter hit a homerun off of starting pitcher Clayton Kershaw")
        self.assertEqual(baseball_team.homerun(), "Derek Jeter HIT A HOMERUN OFF OF Clayton Kershaw")

if __name__ == "__main__": # only run if this script is invoked from the command-line:
    unittest.main()