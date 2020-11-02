"""
    evaluate DST model
"""

import os
from argparse import ArgumentParser

from convlab2.dst.dstc9.eval_model import eval_team

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--teams', type=str, nargs='*')
    parser.add_argument('correct_name_label', action='store_true')
    args = parser.parse_args()
    if not args.teams:
        for team in os.listdir('.'):
            if not os.path.isdir(team):
                continue
            eval_team(team, args.correct_name_label)
    else:
        for team in args.teams:
            eval_team(team, args.correct_name_label)
