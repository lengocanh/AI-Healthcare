### Table of Contents

1. [Pneumonia Detection](#Pneumonia)
2. [Hippocampal Volume Quantification](#HippocampalVolume)
3. [Diabetes Drug Testing](#DiabetesDrug)
4. [Pulse Rate Est](#PulseRate)

#### Pneumonia Detection <a name="Pneumonia"></a>
In this project, I analyze data from the 2D NIH Chest X-ray Dataset and train a CNN to classify a given chest x-ray for the presence or absence of pneumonia. This project culminate in a model that can predict the presence of pneumonia with human radiologist-level accuracy that can be prepared for submission to the FDA for 510(k) clearance as software as a medical device. As part of the submission preparation, I formally describe my model, the data that it was trained on, and a validation plan that meets FDA criteria.<br>

Datas ource for training: https://www.kaggle.com/datasets/nih-chest-xrays/data

#### Hippocampal Volume Quantification <a name="HippocampalVolume"></a>
In this project I build an end-to-end AI system which features a machine learning algorithm that integrates into a clinical-grade viewer and automatically measures hippocampal volumes of new patients, as their studies are committed to the clinical imaging archive.<br>

Udacity (fictional) radiology department runs a HippoCrop tool which cuts out a rectangular portion of a brain scan from every image series, making my job a bit easier, and our committed radiologists have collected and annotated a dataset of relevant volumes, and even converted them to NIFTI format!<br>

I use the dataset that contains the segmentations of the right hippocampus and I use the U-Net architecture to build the segmentation model.<br>

After that, I will proceed to integrate the model into a working clinical PACS such that it runs on every incoming study and produces a report with volume measurements.
#### Diabetes Drug Testing <a name="DiabetesDrug"></a>
EHR data is becoming a key source of real-world evidence (RWE) for the pharmaceutical industry and regulators to make decisions on clinical trials(opens in a new tab). You are a data scientist for an exciting unicorn healthcare startup that has created a groundbreaking diabetes drug that is ready for clinical trial testing. It is a very unique and sensitive drug that requires administering the drug over at least 5-7 days of time in the hospital(X number of days based off of distribution that I will see in data and cutoff point) with frequent monitoring/testing and patient medication adherence training(opens in a new tab) with a mobile application.<br>
In order to achieve your goal you must first build a regression model that can predict the estimated hospitalization time for a patient and also provide an uncertainty estimate range for that prediction so that you can rank the predictions based off of the uncertainty range.
#### Pulse Rate Est <a name="PulseRate"></a>
In this project, I build an algorithm that:<br>

- estimates pulse rate from the PPG signal and a 3-axis accelerometer.
- assumes pulse rate will be restricted between 40BPM (beats per minute) and 240BPM
- produces an estimation confidence. A higher confidence value means that this estimate should be more accurate than an estimate with a lower confidence value.
- produces an output at least every 2 seconds.

