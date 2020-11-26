## ConvLab-2
ConvLab-2 is an open-source toolkit that enables researchers to build task-oriented dialogue systems with state-of-the-art models, perform an end-to-end evaluation, and diagnose the weakness of systems. As the successor of [ConvLab](https://github.com/ConvLab/ConvLab/), ConvLab-2 inherits ConvLab's framework but integrates more powerful dialogue models and supports more datasets. 

The code of ConvLab-2 has been released [here](https://github.com/thu-coai/Convlab-2). 

If you use ConvLab-2 in your research, please cite [ConvLab-2: An Open-Source Toolkit for Building, Evaluating, and Diagnosing Dialogue Systems](https://arxiv.org/abs/2002.04793).

## Participation in DSTC-9 Multi-Domain Task-Oriented Dialog Challenge II Track
### Updates
11/26/2020 -- Release public test sets in source language for cross-lingual DST task.
1. MultiWOZ: [data/multiwoz_zh/dstc9-250.zip](https://github.com/ConvLab/ConvLab-2/blob/master/data/multiwoz_zh/dstc9-250-src.json.zip)
2. CrossWOZ: [data/crosswoz_en/dstc9-250.zip](https://github.com/ConvLab/ConvLab-2/blob/master/data/crosswoz_en/dstc9-250-src.json.zip)

11/03/2020 -- Update CrossWOZ evaluation code and leaderboard. See evaluation section for details.

10/30/2020 -- Release public datasets for cross-lingual DST task.
1. MultiWOZ: [data/multiwoz_zh/dstc9-250.zip](https://github.com/ConvLab/ConvLab-2/blob/master/data/multiwoz_zh/dstc9-250.json.zip)
2. CrossWOZ: [data/crosswoz_en/dstc9-250.zip](https://github.com/ConvLab/ConvLab-2/blob/master/data/crosswoz_en/dstc9-250.json.zip)

10/19/2020 -- Evaluation results are released at https://convlab.github.io/.

10/01/2020 -- Update DST evaluation script for value normalization and CrossWOZ `name` issue.

09/29/2020 -- Paper submission dates updated. We encourage all participants to wrap up your methods as a paper and submit it to our workshop. The link for submissions is https://cmt3.research.microsoft.com/DSTC92021. You can find paper submission guidelines as in https://dstc9.dstc.community/paper-submission. 

09/28/2020 -- Ontology extracted from database for DST released. Values are extracted from database. see `ontology-db.json` in each data dir.

09/27/2020 -- Notice: The scripts [`agent.py`](https://github.com/thu-coai/ConvLab-2/blob/6684b67ac9d05d3b5452484d7445ba455a90d5fe/convlab2/dialog_agent/agent.py) and [`run_agent.py`](https://github.com/thu-coai/ConvLab-2/blob/6684b67ac9d05d3b5452484d7445ba455a90d5fe/convlab2/human_eval/run_agent.py) are updated to enable a better interface encapsulation for stateless bot services. However, you do not need to change anything if your current human evaluation script already works well.

09/25/2020 -- Notice: In End-to-end Multi-domain Task Completion Dialog task, DB grounded information is considered for task success in evaluation. Please check evaluation scripts in ConvLab-2 for details.

09/24/2020 -- Notice: For participants in End-to-end Multi-domain Task Completion Dialog task, please ensure that in your human evaluation script `human.py`, your bot/agent service is set up stateless (similar as in `run_agent.py`). 

09/24/2020 -- Ontology for DST released. Values are extracted from all data (include all test data). see `ontology-data.json` in each data dir. Add explanation of labeling criteria for Cross-lingual DST task in the task description.

09/22/2020 -- Test submission open. If you want to validate whether your submission is errorless before the final submission, you can submit a test submission in CodaLab. Note that CodaLab does not generate reports on the dashboard. We will manually validate your submission and email you about the results. Please do not hesitate to contact us if you have any questions.

09/21/2020 -- Test data released for cross-lingual multi-domain dialog state tracking task
1. MultiWOZ: [data/multiwoz_zh/dstc9-test-250.zip](https://github.com/ConvLab/ConvLab-2/blob/master/data/multiwoz_zh/dstc9-test-250.zip)
2. CrossWOZ: [data/crosswoz_en/dstc9-test-250.zip](https://github.com/ConvLab/ConvLab-2/blob/master/data/crosswoz_en/dstc9-test-250.zip)

Evaluation script: `eval_file.py` and `eval_model.py` on https://github.com/thu-coai/ConvLab-2/tree/master/convlab2/dst/dstc9.

07/15/2020 -- A cleaned version of MultiWOZ 2.1 train/val/test dataset is added to `data/multiwoz/MultiWOZ2.1_Cleaned.zip`

### Task Description
**[Task Proposal](https://drive.google.com/file/d/0Bx4CHsnRHDmJcHQxMmtJRUUyYVBJQnI5SUs5cWlfSGdQbVhj/view)**

As part of the Ninth Dialog System Technology Challenge (DSTC9),  Microsoft Research and Tsinghua University are hosting Multi-domain Task-oriented Dialog Challenge II, aiming to solve two tasks in the multi-domain task completion setting:

**End-to-end Multi-domain Task Completion Dialog** — In recent years there has been an increasing interest in building complex task completion bots that span over multiple domains. In this task, participants will develop an end-to-end dialog system that receives natural language as an input and generates natural language as an output in the travel planning setting. There is no restriction on the modeling approaches, and all resources/datasets/pre-trained models in the community can be used for model training. The system will be evaluated in MultiWOZ 2.1 dataset setting with ConvLab-2.

**Cross-lingual Multi-domain Dialog State Tracking** — Building a dialog system that handles multiple languages becomes increasingly important with the rapid process of globalization. To advance state-of-the-art technologies in handling cross-lingual multi-domain dialogs, we offer the task of building cross-lingual dialog state trackers with a training set in resource-rich language, and dev/test set in a resource-poor language. In particular, this task consists of two sub-tasks. One uses English as the resource-rich language and Chinese as the resource-poor language on the MultiWOZ dataset, and the other one uses Chinese as the resource-rich language and English as the resource-poor language on the CrossWOZ dataset.

labeling criteria:
1. Please consult the original papers first ([MultiWOZ](https://arxiv.org/abs/1810.00278), [MultiWOZ 2.1](https://arxiv.org/abs/1907.01669), [CrossWOZ](https://arxiv.org/abs/2002.11893)). And provided ontology based on data `ontology-data.json`.
2. There are some noisy and confusing annotations in dataset, such as `when to annotate the name of the restaurant/hotel/attraction?`, we open an issue #7 to share the thoughts.

### Timeline
<table>
<tr>
<td><b> Jun 15, 2020</b></td>  <td> Competition Starts </td>
</tr>
<tr>
<td><b> Sep 21, 2020</b></td>  <td> Test data is released </td>
</tr><tr>
<td><b> Oct 5, 2020</b></td>  <td>Entry submission deadline </td>
</tr><tr>
<td><b> Oct 19,2020</b></td>  <td> Results announced </td>
</tr><tr>
<td><b> Nov 17, 2020</b></td>  <td> Paper submission deadline </td>
</tr><tr>
 <td><b> Nov 18, 2020 - Nov 30, 2020 </b></td>  <td> Review period </td>
</tr><tr>
<td><b> Dec 3, 2020</b></td>  <td> Paper acceptance notification </td>
</tr><tr>
<td><b> Dec 18, 2020</b></td>  <td> Camera-ready submission deadline </td>
</tr>
</table>

### Evaluation
#### Multi-domain End-to-end Dialog Challenge Task
1. Automatic end2end Evaluation: The submitted system (code) will be evaluated using the user-simulator setting `bertnlu + AgendaPolicy + templateNLG` as in [ConvLab-2](https://github.com/thu-coai/Convlab-2). We will use the evaluator MultiWozEvaluator in `convlab2/evaluator/multiwoz_eval.py` to report metrics, including success rate, complete rate, book rate, number of turns, inform precision/recall/F1. The success rate is considered as the key metric in the automatic evaluation.
Note: The reference number (`Ref`) represents the index of the booked entity in the database (see [dbquery](https://github.com/thu-coai/ConvLab-2/blob/master/convlab2/util/multiwoz/dbquery.py) for details), which will be checked in the automatic evaluation.
2. Human Evaluation: The submitted system will be evaluated in Amazon Mechanic Turk. Crowd-workers will communicate with your summited system, and provide a rating based on the whole experience (language understanding, appropriateness, etc.)

For participants interested in the ConvLab-2 baseline model performance, please check [test scripts](https://github.com/thu-coai/ConvLab-2/tree/master/tests) in ConvLab-2.
#### Multi-domain Cross-lingual Dialog State Tracking Task
We evaluate the performance of the dialog state tracker using two metrics:
1. Joint Goal Accuracy. This metric evaluates whether the predicted dialog state is exactly equal to the ground
truth.
2. Slot Accuracy. This metric evaluates whether the predicted label for each individual slot is exactly equal to the ground
truth, averaged over all slots.

**11/03/2020 update:**

During the evaluation, we found that there is a gap between collected CrossWOZ data and our assumption. Specifically, as mentioned in Issue #7(https://github.com/ConvLab/ConvLab-2/issues/7), we think that the agent should log down the names of attraction/hotel/restaurant when the user accepts them. However, the collected data miss a number of the name labels in this situation. Therefore, we utilize the candidate lists from selectedResults to correct name labels. We’ve updated our evaluation code (https://github.com/thu-coai/ConvLab-2/blob/master/convlab2/dst/dstc9/utils.py#L13-L68) with an additional argument to reflect this change(set correct_name_label=True). We also provide an additional leaderboard for CrossWOZ at https://convlab.github.io. This change is considered as applying two different evaluation approaches, and both of the original and new leaderboards are valid.

### Registration and Participation
1. Submit the participation form [here](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7x1M3FOeqhCttKwx4jvle9UNUVTQVRaT1AwUVRGUlc0WlBZVklQQ0tSWCQlQCN0PWcu). Your identities will NOT be made public.
2. Participate at https://aka.ms/dstc-mdtc (sign up if you do not have a CodaLab account). Participation is welcome from any team.

### Submission
####  Multi-domain End-to-end Dialog Challenge Task
1. Extend ConvLab-2 with your code, and submit up to 5 agents. In the main directory, please create a directory called `end2end`, and sub-directories with names `submission[1-5]`. In the sub-directory, add your runnable main python scripts for both automatic evaluation and human evaluation, respectively. For automatic evaluation, please use a similar format as `tests/test_end2end.py` in ConvLab-2 with the main script name as `automatic.py`. For human evaluation, please use a similar format as `convlab2/human_eval/run_agent.py` in ConvLab-2 with the main script name as `human.py`. Since the human evaluation service supports concurrent workers in Amazon Mechanic Turk, please ensure that **your service in human.py is stateless and compatible with `convlab2/human_eval/run.py`** (Your dialog agent should not use its existing internal state, but takes the dialog state via in_request[‘agent_state’]).
2. If your code uses external packages beyond the existing docker environment, please choose one of the following two approaches to specify your environment requirements:
    - Create your own Dockerfile with the name dev.dockerfile (preferred)
    - Add install.sh under the main directory. Running install.sh should install all required extra packages.
3. Please add a file called `model_description.txt` in the directory `end2end`, and add a brief description of your system. Based on the information you provide, we will make some summarization for our track review.
4. Zip the system and submit (Click 'Participate' in https://aka.ms/dstc-mdtc, select Test Submission or Final Submission, and fill in required information. Once you click 'Submit' in CodaLab, a window pops up for you to upload the zip file). In case that your models are too large, you can share your model checkpoints in cloud drives and add scripts to download models.

Notice: the simulator evaluation and human evaluation may not be exactly the same as `tests/test_end2end.py` and `convlab2/human_eval/` in ConvLab-2, respectively.

#### Multi-domain Cross-lingual Dialog State Tracking Task
1. Extend ConvLab-2 with your code, and submit up to 5 results and models. In the main directory, please create a directory called `multiwoz-dst` or `crosswoz-dst` or both, based on your selected task(s), and include your prediction results (for released 250 test samples) and models (to perform evaluation on 250 hidden test samples) with the name `submission[1-5]`. We will use `eval_file.py` and `eval_model.py` (both are available on https://github.com/thu-coai/ConvLab-2/tree/master/convlab2/dst/dstc9) to evaluate the results and models.
2. Please add a file called `model_description.txt` in the directory `multiwoz-dst` and/or `crosswoz-dst`, and add a brief description of your system. Based on the information you provide, we will make some summarization for our track review.
3. Zip them and submit (Click 'Participate' in https://aka.ms/dstc-mdtc, select Test Submission or Final Submission, and fill in required information. Once you click 'Submit' in CodaLab, a window pops up for you to upload the zip file).

Notice: the final score will be the average of performance on the released data and the hidden data. We will use the `sys_state_init` of CrossWOZ dataset as DST label.

**If you are participating in both tasks, you can submit one zip file with both tasks' results.** 

**Please also note that the CodaLab system/dashboard will not report evaluation results. If you want to validate whether your submission is errorless before the final submission, you can submit a test submission after September 21 and notify us via email.**


### Resources for reference
[SOLOIST: Few-shot Task-Oriented Dialog with A Single Pre-trained Auto-regressive Model](https://arxiv.org/abs/2005.05298)

[DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation](https://github.com/microsoft/DialoGPT)
### Contact Information
Please email dstc9-mdtc@service.microsoft.com if you have any questions.
For special enquiries, feel free to contact: jincli (at) microsoft (dot) com; zhu-q18 (at) mails (dot) tsinghua (dot) edu (dot) cn
