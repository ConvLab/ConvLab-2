import os
import json
import zipfile
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--subtask', type=str, choices=['multiwoz', 'crosswoz'], required=True)
args = parser.parse_args()
subtask = args.subtask


def extract_gt(data):
    gt = {}
    if subtask == 'multiwoz':
        for dialog_id, dialog in data.items():
            states = []
            turns = dialog['log']
            for i in range(0, len(turns), 2):
                usr_turn, sys_turn = turns[i:i + 2]
                state = {}
                for domain_name, domain in sys_turn['metadata'].items():
                    if domain_name in ['警察机关', '医院']:
                        continue
                    domain_state = {}
                    for slots in domain.values():
                        for slot_name, value in slots.items():
                            domain_state[slot_name] = value
                    state[domain_name] = domain_state
                states.append(state)
            gt[dialog_id] = states
    else:
        for dialog_id, dialog in data.items():
            states = []
            turns = dialog['messages']
            for i in range(0, len(turns), 2):
                usr_turn, sys_turn = turns[i:i + 2]
                state = {}
                for domain_name, domain in sys_turn['sys_state_init']:
                    domain_state = {}
                    for slot_name, value in domain.items():
                        if slot_name == 'selectedResults':
                            continue
                        domain_state['slot_name'] = value
                    state[domain_name] = domain_state
                states.append(state)
            gt[dialog_id] = states

    return gt


def evaluate(gt, pred):
    def exception(description, **kargs):
        ret = {
            'status': 'exception',
            'description': description,
        }
        for k, v in kargs.items():
            ret[k] = v
        return ret

    joint_acc, joint_tot = 0
    slot_acc, slot_tot = 0, 0
    tp, fp, fn = 0, 0, 0
    for dialog_id, gt_states in gt.items():
        if dialog_id not in pred:
            return exception('some dialog not found', dialog_id=dialog_id)

        pred_states = pred[dialog_id]
        if len(gt_states) != len(pred_states):
            return exception(f'turns number incorrect, {len(gt_states)} expected, {len(pred_states)} found', dialog_id=dialog_id)

        for turn_id, (gt_state, pred_state) in enumerate(zip(gt_states, pred_states)):
            joint_tot += 1
            turn_result = True
            for domain_name, gt_domain in gt_state.items():
                if domain_name not in pred_state:
                    return exception('domain missing', dialog_id=dialog_id, turn_id=turn_id, domain=domain_name)

                pred_domain = pred_state[domain_name]
                for slot_name, gt_value in gt_domain.items():
                    if slot_name not in pred_state:
                        return exception('slot missing', dialog_id=dialog_id, turn_id=turn_id, domain=domain_name, slot=slot_name)
                    pred_value = pred_domain[slot_name]
                    slot_tot += 1
                    if gt_value == pred_value:
                        slot_acc += 1
                        tp += 1
                    else:
                        turn_result = False
                        # for class of gt_value
                        fn += 1
                        # for class of pred_value
                        fp += 1
            joint_acc += turn_result

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * tp / (2 * tp + fp + fn)
    return {
        'status': 'ok',
        'joint accuracy': joint_acc / joint_tot,
        'slot': {
            'accuracy': slot_acc / slot_tot,
            'precision': precision,
            'recall': recall,
            'f1': f1,
        }
    }


if __name__ == '__main__':
    data_dir = os.path.join('../data/', 'multiwoz_zh' if subtask == 'multiwoz' else 'crosswoz_en')
    gt = extract_gt(json.load(zipfile.ZipFile(os.path.join(data_dir, 'human_val_data.zip')).open('human_val.json')))
    json.dump(gt, open('gt-multiwoz.json', 'w'), ensure_ascii=False, indent=4)

    # results = {}
    # for i in range(1, 6):
    #     filename = f'submission{i}.json'
    #     if not os.path.exists(filename):
    #         continue
    #     pred = json.load(open(filename))
    #     results[filename] = evaluate(gt, pred)
