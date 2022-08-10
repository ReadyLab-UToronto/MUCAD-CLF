# The Multi-User Computer-Aided Design Collaborative Learning Framework (MUCAD-CLF) 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5504306.svg)](https://doi.org/10.5281/zenodo.5504306)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1N2NPF4MIhPmCR7keZnVtfhdxBfkYBUWF?usp=sharing)

Code available in this repository aims to provide an efficient tool to visualize and compare users' 
audit trail data from [Onshape Enterprise Analytics](https://www.onshape.com/en/features/analytics).
The MUCAD-CLF was first published in [this journal paper](https://doi.org/10.1016/j.aei.2021.101446). 
If you are using codes in this repository for research, please cite our paper for reference.

> Deng Y, Mueller M, Rogers C, Olechowski A. The Multi-User Computer-Aided Design Collaborative Learning Framework. _Adv Eng Informatics_. 2022;51:101446. doi:10.1016/j.aei.2021.101446

## Table of contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Maintainers](#maintainers)
* [Contributing](#contributing) 

## General Info 
As Onshape Analytics provides a rich but enormous dataset -- logging all user actions in an Onshape document -- 
it can be challenging to efficiently visualize and compare the data of different users. 
We first adapted and developed two action classification methods in this framework to organize and 
count the recorded action data in several meaningful categories. Then, we generated script for 
creatively plotting the counts for visaulization and comparison. 

Design Space Classification 
<p align="center">
<img src="https://drive.google.com/uc?id=1JMz5HH1T0ELfCtZg7x-3Tb5I4kekn9NR" width="600">
</p>

Action Type Classification 
<p align="center">
<img src="https://drive.google.com/uc?id=196B9Y1uIy1OdlBS9psyHSQ4fIW-6clsy" width="600">
</p>

This open-sourced repository provides two options for the public to replicate our research method 
and apply to new data for analysis: 
1. Use the interactive Jupyter notebook version shared in Google Colaboratory through 
[this link](https://colab.research.google.com/drive/1N2NPF4MIhPmCR7keZnVtfhdxBfkYBUWF?usp=sharing). 
**(Recommended for users with no/little programming experience)**
2. The Jupyter notebook mentioned in Option 1 is also available for download, named `MUCAD_CLF.ipynb` in this repository.  
3. Download or clone this repository to a local Python IDE for more flexible use and edits.   

Structure of this repository: 
* `action_classification` contains the two action classification methods that each organize actions in six different categories. 
* `action_counting` takes in an audit trail file in CSV format and count the actions using the two action classification methods. 
* `action_count_plotting` provides a few plotting functions for the visualization and comparison of the data. 
* `sample_audit_trails` contains two anonymized sample audit trails generated by us for demonstration in both single-user (one audit trail per user) and multi-user (one audit trail per file) format. 
* `sample_outputs` contains the sample plots generated by the testing script with data from the sample audit trails. 
* `test.py` provides a demonstrating script on the usage of this project. 
* `MUCAD_CLF.ipynb` is an alternative format of the repository in Jupyter notebook. 

## Technologies
Project is created with:
* Python 3.6
	
## Setup
If using the online version, please follow these steps:  
1. Click the [shared link](https://colab.research.google.com/drive/1N2NPF4MIhPmCR7keZnVtfhdxBfkYBUWF?usp=sharing) 
to access the view-only shared code.
2. Make a copy and save it in your own Google Drive to allow editing. 
3. Follow instructions in the file to upload and analyze your data.   

If cloning the entire project, please follow these steps: 
1. Download or clone this repository as you would for any other GitHub project. 
2. Download all relevant audit trails for analysis from your Onshape Enterprise account in CSV format, 
following steps shown in the image below. (Plots to be generated will compare data 
between each audit trail analyzed. It is recommended to download audit trails separately for each 
Onshape document and/or user to be analyzed.)
3. Rename the CSV files if necessary (file names will be used to format output). 
4. Place all unzipped audit trial files into the `sample_audit_trails` folder. 
5. Read, modify, and run `test.py` for a quick demonstration in any Python IDE of your choice.  
6. Aggregate actions count will be recorded in `Counts.csv` in the `sample_outputs` folder, and 
generated plots will be saved in the directory location specified. 

<p align="center">
<img src="https://drive.google.com/uc?id=1gY79D68QT0DgM8IhsncjPrkBGajQD00l" width="500">
</p>  

## Maintainers
* Yuanzhe (Felix) Deng - yuanzhe.deng@mail.utoronto.ca 
* Alison Olechowski - olechowski@mie.utoronto.ca 

Supporting organization: 
* Ready Lab, University of Toronto - https://readylab.mie.utoronto.ca 

## Contributing 
We welcome and appreciate future contributions to the framework from the Onshape users, educators, 
and researchers community, especially in the following categories: 
* New action classification methods 
* New plots/methods to visualize the data and compare data between users 
* Other useful data to be collected from the users, uncaptured by Onshape Analytics  

To contribute, please provide the code for the new method/idea along with a testing script. Then, contact the maintainers and submit a pull request.  
