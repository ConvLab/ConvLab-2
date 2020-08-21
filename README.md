## ConvLab-2
ConvLab-2 is an open-source toolkit that enables researchers to build task-oriented dialogue systems with state-of-the-art models, perform an end-to-end evaluation, and diagnose the weakness of systems. As the successor of [ConvLab](https://github.com/ConvLab/ConvLab/), ConvLab-2 inherits ConvLab's framework but integrates more powerful dialogue models and supports more datasets. 

The code of ConvLab-2 has been released [here](https://github.com/thu-coai/Convlab-2). 

If you use ConvLab-2 in your research, please cite [ConvLab-2: An Open-Source Toolkit for Building, Evaluating, and Diagnosing Dialogue Systems](https://arxiv.org/abs/2002.04793).

## Participation in DSTC-9 Multi-Domain Task-Oriented Dialog Challenge II Track
### Updates
07/15/2020 -- A cleaned version of MultiWOZ 2.1 train/val/test dataset is added to `data/multiwoz/MultiWOZ2.1_Cleaned.zip`

### Task Description
**[Task Proposal](https://drive.google.com/file/d/0Bx4CHsnRHDmJcHQxMmtJRUUyYVBJQnI5SUs5cWlfSGdQbVhj/view)**

As part of the Ninth Dialog System Technology Challenge (DSTC9),  Microsoft Research and Tsinghua University are hosting Multi-domain Task-oriented Dialog Challenge II, aiming to solve two tasks in the multi-domain task completion setting:

**End-to-end Multi-domain Task Completion Dialog** — In recent years there has been an increasing interest in building complex task completion bots that span over multiple domains. In this task, participants will develop an end-to-end dialog system that receives natural language as an input and generates natural language as an output in the travel planning setting. There is no restriction on the modeling approaches, and all resources/datasets/pre-trained models in the community can be used for model training. The system will be evaluated in MultiWOZ 2.1 dataset setting with ConvLab-2.

**Cross-lingual Multi-domain Dialog State Tracking** — Building a dialog system that handles multiple languages becomes increasingly important with the rapid process of globalization. To advance state-of-the-art technologies in handling cross-lingual multi-domain dialogs, we offer the task of building cross-lingual dialog state trackers with a training set in resource-rich language, and dev/test set in a resource-poor language. In particular, this task consists of two sub-tasks. One uses English as the resource-rich language and Chinese as the resource-poor language on the MultiWOZ dataset, and the other one uses Chinese as the resource-rich language and English as the resource-poor language on the CrossWOZ dataset.

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
<td><b> Nov 2020</b></td>  <td> Paper submission deadline </td>
</tr>
</table>

### Evaluation
#### Multi-domain End-to-end Dialog Challenge Task
1. Automatic end2end Evaluation: The submitted system (code) will be evaluated using the user-simulator setting `bertnlu + AgendaPolicy + templateNLG` as in [ConvLab-2](https://github.com/thu-coai/Convlab-2). We will use the evaluator MultiWozEvaluator in `convlab2/evaluator/multiwoz_eval.py` to report metrics including success rate, average reward, number of turms, precision, recall, and F1 score. (Note: The reference number (`Ref`) represents the index of the booked entity in the database (see [dbquery](https://github.com/thu-coai/ConvLab-2/blob/master/convlab2/util/multiwoz/dbquery.py) for details), which will be checked in automatic evaluation)
2. Human Evaluation: The submitted system will be evaluated in Amazon Mechanic Turk. Crowd-workers will communicate with your summited system, and provide a rating based on the whole experience (language understanding, appropriateness, etc.)
#### Multi-domain Cross-lingual Dialog State Tracking Task
We evaluate the performance of the dialog state tracker using two metrics:
1. Joint Goal Accuracy. This metric evaluates whether the predicted dialog state is exactly equal to the ground
truth.
2. Slot Precision/Recall/F1. These metrics evaluate whether the predicted labels for individual slots in dialog
state are equal to the ground truth, microaveraged over all slots.

### Registration and Participation
1. Submit the participation form [here](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7x1M3FOeqhCttKwx4jvle9UNUVTQVRaT1AwUVRGUlc0WlBZVklQQ0tSWCQlQCN0PWcu). Your identities will NOT be made public.
2. Participate at https://aka.ms/dstc-mdtc (sign up if you do not have a CodaLab account). Participation is welcome from any team.

### Submission (Tentative)
####  Multi-domain End-to-end Dialog Challenge Task
1. Extend ConvLab-2 with your code, and submit up to 5 agents. In the main directory, please create a directory called `end2end`, and sub-directories with names `submission[1-5]`. In the sub-directory, add your runnable main python scripts for both automatic evaluation and human evaluation, respectively. For automatic evaluation, please use a similar format as `tests/test_end2end.py` in ConvLab-2 with the main script name as `automatic.py`. For human evaluation, please use a similar format as `convlab2/human_eval/run_agent.py` in ConvLab-2 with the main script name as `human.py`. Human evaluation is executed in Amazon Mechanic Turk. Please make sure that your agent is compatible with `convlab2/human_eval/run.py` for evaluation on Amazon Mechanic Turk.
2. If your code uses external packages beyond the existing docker environment, please choose one of the following two approaches to specify your environment requirements:
    - Add install.sh under the main directory. Running install.sh should install all required extra packages.
    - Create your own Dockerfile with the name dev.dockerfile
3. Zip the system and submit.

#### Multi-domain Cross-lingual Dialog State Tracking Task
1. Extend ConvLab-2 with your code, and submit up to 5 results.  In the main directory, please create a directory called `multiwoz-dst` or `crosswoz-dst` or both, based on your selected task(s), and include your prediction results with the name `submission[1-5]`. 
2. Zip them and submit.

**If you are participating both tasks, you can submit one zip file with the results of both tasks together**.


### Resources for reference
[SOLOIST: Few-shot Task-Oriented Dialog with A Single Pre-trained Auto-regressive Model](https://arxiv.org/abs/2005.05298)

[DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation](https://github.com/microsoft/DialoGPT)
### Contact Information
Please email dstc9-mdtc@service.microsoft.com if you have any questions.
For special enquiries, feel free to contact: jincli (at) microsoft (dot) com; zhu-q18 (at) mails (dot) tsinghua (dot) edu (dot) cn
