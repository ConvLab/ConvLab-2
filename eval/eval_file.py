"""
    evaluate output file
"""

import os

from convlab2.dst.dstc9.utils import prepare_data, extract_gt
from convlab2.dst.dstc9.eval_file import evaluate

if __name__ == '__main__':
    for subtask in ['multiwoz', 'crosswoz']:
        test_data = prepare_data(subtask, 'dstc9-250')
        gt = extract_gt(test_data)
        for team in os.listdir('.'):
            for i in range(1, 6):
                model_dir = os.path.join(team, f'{subtask}-dst', f'submission{i}')
                if not os.path.exists(model_dir):
                    continue
                print(model_dir)
                evaluate(model_dir, subtask, gt)
