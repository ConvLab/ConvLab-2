# ConvLab-2
ConvLab-2 is an open-source toolkit that enables researchers to build task-oriented dialogue systems with state-of-the-art models, perform an end-to-end evaluation, and diagnose the weakness of systems. As the successor of ConvLab (https://github.com/ConvLab/ConvLab/), ConvLab-2 inherits ConvLab's framework but integrates more powerful dialogue models and supports more datasets. The code of ConvLab-2 has been released here https://github.com/thu-coai/Convlab-2. If you use ConvLab-2 in your research, please cite [ConvLab-2: An Open-Source Toolkit for Building, Evaluating, and Diagnosing Dialogue Systems](https://arxiv.org/abs/2002.04793).

## Participation in DSTC-9
1. Extend ConvLab with your code, and include submission.json under the convlab/spec directory.
2. In submission.json, specify up to 5 specs with the name submission[1-5].
2. Make sure the code with the config is runnable in the docker environment.
3. If your code uses external packages beyond the existing docker environment, please choose one of the following two approaches to specify your environment requirements:
    - Add install.sh under the convlab directory. install.sh should include all required extra packages.
    - Create your own Dockerfile with the name dev.dockerfile
4. Zip the system and submit.
### Evaluation
1. Automatic end2end Evaluation: The submitted system will be evaluated using the user-simulator setting in spec `milu_rule_rule_template` in `convlab/spec/baseline.json`. We will use the evaluator MultiWozEvaluator in `convlab/evaluator/multiwoz` to report metrics including success rate, average reward, number of turms, precision, recall, and F1 score.
2. Human Evaluation: The submitted system will be evaluated in Amazon Mechanic Turk. Crowd-workers will communicate with your summited system, and provide a rating based on the whole experience (language understanding, appropriateness, etc.)
