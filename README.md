# Advanced-NLP-Take-Home-Exam
The code was carried out by Yeshan Wang during the course ‘Advanced NLP' taught by Luis Morgado da Costa and Jose Angel Daza at VU Amsterdam.

**All code and notebooks should be run in the following order:**

## Create_ChallengeSet.ipynb
The notebook is used to create challenge datasets for 5 capabilities and save as corresponding json files in the data directory:
- data/causative_alternation.json
- data/long_distance_dependencies.json
- data/location_modifiers.json
- data/voice.json
- data/robustness.json

## main.ipynb
The notebook is used for running two SRL models (BiLSTM/BERT) over the Challenge Dataset. The evaluation results (failure rate) of each model in each test (with example failure cases) can be seen in the notebook. The text-based output of each model in each test is saved as corresponding json files in the output directory:
- output/causative alternation/BiLSTM.json & BERT.json
- output/long distance dependencies/BiLSTM.json & BERT.json
- output/location modifiers/BiLSTM.json & BERT.json
- output/voice/BiLSTM.json & BERT.json
- output/robustness/BiLSTM.json & BERT.json

The requirements.txt file includes all necessary libraries for code running.
The utils.py file contains all helper functions needed to run the the notebook main.ipynb

