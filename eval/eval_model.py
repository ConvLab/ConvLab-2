"""
    evaluate DST model
"""

from convlab2.dst.dstc9.eval_model import evaluate
from convlab2.dst.dstc9.utils import prepare_data

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('subtask', type=str, choices=['multiwoz', 'crosswoz'])
    parser.add_argument('split', type=str, choices=['train', 'val', 'test', 'human_val'])
    args = parser.parse_args()
    subtask = args.subtask
    test_data = prepare_data(subtask, args.split)
    gt = {
        dialog_id: [state for _, _, state in turns]
        for dialog_id, turns in test_data.items()
    }
    evaluate('example', subtask, test_data, gt)
