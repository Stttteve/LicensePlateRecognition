# LicensePlateRecognition

# License Plate Recognition System

This project implements a License Plate Recognition (LPR) system using machine learning and image processing techniques. The goal of the system is to detect and recognize characters on vehicle license plates from an image input. The system is developed using Python and utilizes libraries such as `scikit-image`, `scikit-learn`, and `numpy`.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License Plate Detection](#license-plate-detection)
- [Character Segmentation](#character-segmentation)
- [Character Recognition](#character-recognition)
- [Contributing](#contributing)
- [License](#license)

## Introduction

License Plate Recognition (LPR) systems are widely used in security systems, parking management, and traffic monitoring. This project provides a Python implementation for detecting the license plate in an image, segmenting individual characters, and recognizing them using machine learning techniques.

## Features

- Detects license plates in vehicle images.
- Segments and extracts individual characters from license plates.
- Recognizes characters using a trained machine learning model.

  
## Installation

To get started, clone the repository and install the necessary dependencies. Make sure you have Python 3.8 or higher installed.

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/LicensePlateRecognition.git
    cd LicensePlateRecognition
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv lpr
    source lpr/bin/activate  # On Windows use: lpr\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install numpy
    pip install scikit-image
    pip install matplotlib
    pip install scikit-learn
    pip install joblib
    ```

## Usage

Once you have installed the dependencies, you can start the program by running:

```bash
python char_prediction.py


Project Structure

license-plate-recognition/
│
├── char_prediction.py        # Character recognition code (main entry point)
├── lpr_image.py              # Image processing functions
├── lpr_findConnected.py      # Functions that locate the bounding box of the license plate
├── lpr_locate.py              # Draw bounding box and Segment the characthers on the Licenseplate
├── Trainingdata/             # Training dataset for character recognition
├── car.jpg                  # Sample image with License plate HNR8333
├── car4.jpg                  # Sample image with license plate INRS5103
├── README.md                 # This file
└── Char_recognition model.py  # Code to train the character recognition model

License Plate Detection
The first stage involves detecting the license plate in the input image. The steps include:

Grayscale conversion of the input image.
Binary conversion using Otsu's thresholding.
Connected Component Analysis (CCA) to label the image regions.
Bounding box detection to identify possible license plates using specific size and shape constraints.
Character Segmentation
Once the license plate is localized, character segmentation is done by:

Isolating the region of the license plate.
Dividing the region into individual characters using projection analysis and connected components.
Character Recognition
Character recognition is performed using a machine learning model trained on a labeled dataset of characters. The characters are resized to a uniform size (20x20 pixels) before feeding into a Support Vector Classifier (SVC) for classification.

Contributing
Feel free to contribute to this project by submitting a pull request or opening an issue. All contributions are welcome!

License
This project is licensed under the MIT License.
