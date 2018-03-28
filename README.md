# Android Malware Detection

Android Malware detection using Deep Learning Hybrid Model, an implementation of [A Hybrid Malicious Code Detection Method based on Deep Learning](https://pdfs.semanticscholar.org/45ba/f042f5184d856b04040f14dd8e04aa7c11f6.pdf) carried out as a project for Information Assurance and Security course.

## File Descriptions.

train_and_test.py - Contains the main code which has the hybrid model. To train the model we change the LOAD_MODEL variable to False and then run train.py to train the model, else if the model is already trained it will classify the APKs which are in the path TEST_DATASET_PATH mentioned in imports.py file(change this accordingly to test all the APKs which you want) 

imports.py - All the constants are defined here (Change these accordingly).Contains all the neccessary imports. Also set the dataset path to where the dataset is present to run the software from end-to-end.

util.py - Contains the class PreProcess() that is responsible for extracting features out of the APKs and storing them in a CSV file.


---

## Folder Descriptions.

csv/ - Contains benign and malign feature set of all the APKs for training.

testAPKs/ - Contains 1 Test case of 2 APKs (benign and malign)

screenshots/ - Contains all relevant screenshots of the code execution.

androguard/ and dbn/ - external libraries which are used.

pickled/ - contains all the necessary info for extracting the features. The main model after training is also stored here. 

We trained the Autoencoder for 5 epochs with batch size of 5.
The final training loss was found to be 170.5314 and the validation loss was found to be 171.6650.

We trained the RBM for 20 epochs with batch size 10 and learning rate of 0.06.
The final training RBM Reconstruction error was found to be 0.028728. 

### NOTE:

The dataset mentioned in the paper is for Network intrusion detection, but we are using APKs in our dataset to classify them.
As the size of the Dataset is huge, it is not included here. The directory already contains the extraced features in the form of benign.csv and malign.csv.If you want to extract features from scratch then download the genome APK dataset from [here](http://www.malgenomeproject.org/).
