"""
    evaluate output file
"""

from convlab2.dst.dstc9.eval_file import extract_gt, dump_example, prepare_data, evaluate

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('subtask', type=str, choices=['multiwoz', 'crosswoz'])
    parser.add_argument('split', type=str, choices=['train', 'val', 'test', 'human_val'])
    args = parser.parse_args()
    subtask = args.subtask
    split = args.split
    dump_example(subtask, split)
    test_data = prepare_data(subtask, args.split)
    gt = extract_gt(test_data)
    evaluate('example', subtask, gt)
