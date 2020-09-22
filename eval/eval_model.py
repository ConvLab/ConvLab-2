"""
    evaluate DST model
"""

from convlab2.dst.dstc9.eval_model import evaluate

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('subtask', type=str, choices=['multiwoz', 'crosswoz'])
    args = parser.parse_args()
    evaluate('example', args.subtask)
