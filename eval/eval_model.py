"""
    evaluate DST model
"""

import os

from convlab2.dst.dstc9.eval_model import evaluate
from convlab2.dst.dstc9.utils import prepare_data, extract_gt


def eval_team(team):
    for subtask in ['multiwoz', 'crosswoz']:
        test_data = prepare_data(subtask, 'dstc9')
        gt = extract_gt(test_data)
        for i in range(1, 6):
            model_dir = os.path.join(team, f'{subtask}-dst', f'submission{i}')
            if not os.path.exists(model_dir):
                continue
            print(model_dir)
            evaluate(model_dir, subtask, test_data, gt)

if __name__ == '__main__':
    for team in os.listdir('.'):
        if not os.path.isdir(team):
            continue
        eval_team(team)
