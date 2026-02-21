# AI Alphabet Learning Board

### Voice-Based Interactive Learning System using Raspberry Pi

---

## Project Overview

The AI Alphabet Learning Board is an embedded voice-based educational system designed to assist children in learning English alphabets through interactive visual and auditory feedback.

This system integrates speech recognition with Raspberry Pi-based hardware to create a multi-mode learning environment where users can interact with alphabets using physical input and voice commands.

The objective of the system is to improve early learning through interactive training using Artificial Intelligence and Embedded System integration.

---

## System Description

The system consists of the following modules:

* Alphabet Board Interface
* Raspberry Pi Processing Unit
* Speech Recognition Module
* Machine Learning-Based Classification Model
* Audio Feedback System
* GPIO-based Hardware Interaction

The user interacts with the system using physical alphabet selection and spoken voice input.

---

## Implemented Learning Modes

| Mode   | Description       |
| ------ | ----------------- |
| Mode 1 | Know the Alphabet |
| Mode 2 | Find the Alphabet |
| Mode 3 | Learn a Word      |
| Mode 4 | Speak an Alphabet |

Each learning mode provides a different level of interaction between the user and the system through visual and audio feedback.

---

## Software Implementation

The system is implemented using Python and integrates:

* SpeechRecognition library for voice input
* pyttsx3 for text-to-speech output
* RPi.GPIO for hardware interaction
* Librosa for audio feature extraction
* Scikit-learn for alphabet classification

---

## Machine Learning Model

Voice samples of English alphabets (A–Z) were collected to train the classification model.

Feature Extraction Technique:

* MFCC (Mel-Frequency Cepstral Coefficients)

Classification Algorithms Used:

* Naive Bayes
* Random Forest
* Gradient Boosting
* Support Vector Machine (SVM)

Model training and evaluation is performed using:

training/alphabet_model_training.ipynb

---

## Project Directory Structure

```
AI-Alphabet-Learning-Board/
│
├── src/
├── dataset/
├── training/
├── models/
├── graphs/
├── literature_review/
├── documents/
├── flowchart/
├── design/
└── README.md
```

---

## Dataset

The dataset contains recorded voice samples of individual alphabets used for training the classification model.

Each class corresponds to one alphabet (A–Z).

---

## Training Results

Model performance is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Evaluation graphs are available in:

graphs/

---

## Literature Review

Related research papers and reference materials used during system development are available in:

literature_review/

---

## Documentation

Project report, presentation slides and other relevant documents are available in:

documents/

---

## System Flowchart

System operational flow is provided in:

flowchart/

---

## Physical Board Design

Physical layout and board design are provided in:

design/

---

## How to Run the System

Install required Python libraries:

```
pip install SpeechRecognition pyttsx3 librosa scikit-learn RPi.GPIO
```

Run the Raspberry Pi control script from the src folder.

---

## Application

This system can be used as:

* Educational Training Aid
* Interactive Learning Device
* Embedded AI-based Teaching Tool

---

## Developed By

Asif Mahmud

---
