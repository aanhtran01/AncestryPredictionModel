Ancestry Prediction Model
-------------------------
This repository contains code for a linear regression-based model to predict the ancestry of individuals based on Single Nucleotide Polymorphism (SNP) data. Please note that the datasets required for training and validation are not available in this repository. You need to obtain these datasets separately.

Dataset
-------
To use the code, you must have the following dataset files:

ancestry_train.data: An Ntrain x M matrix in a txt file storing the SNP information of the input data, used for training purposes (Ntrain represents individual numbers; M represents the available SNPs).
ancestry_train.solution: A Ntrain x K matrix in a txt file representing the proportion (range 0-1) of each individual belonging to each of the K different ancestry groups, used for training purposes.
ancestry_test.data: An Nvalid x M matrix in a txt file storing the SNP information of the input data, used for validation purposes (Ntrain represents individual numbers; M represents the available SNPs).
ancestry_label.name: The categories of the response variable y (for reference purposes only).
ancestry_feat.name: The feature name of each input feature (for reference purposes only).
Ensure that these files are available before running the code.

Requirements
------------
Make sure you have the following dependencies installed:

Python 3
NumPy
pandas
scikit-learn
You can install the required packages using:
pip install numpy pandas scikit-learn

Output Files
------------
predictions.csv: CSV file containing the predicted proportions of each individual belonging to different ancestry groups.
