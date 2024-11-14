# Custom Dataset Capture Tool for Trash Detection

This repository contains scripts for capturing images to create a custom dataset for trash detection. The scripts provide functionality to capture images using either a laptop's built-in webcam or a mobile camera connected via USB/WiFi.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Laptop Camera Capture](#laptop-camera-capture)
- [Mobile Camera Capture](#mobile-camera-capture)
- [Configuration](#configuration)
- [Contributing](#contributing)


## Introduction

The purpose of this project is to capture images to build a custom dataset for detecting different classes of trash or objects. The tool provides a user-friendly way to define object classes, capture images for each class, and manage datasets efficiently.

## Features

- Capture images using a laptop's webcam (`capture_with_laptop.py`) or a mobile camera (`capture_with_mobile.py`).
- Define new object classes dynamically.
- Automatic image saving with class-based naming conventions.
- Real-time user interface with options to start/stop image capture.
- Easy integration with image classification and object detection training pipelines.

## Installation

### Prerequisites

- Python 3.9 or above (preferably python 3.9)
- OpenCV library
- USB/WiFi connectivity for mobile camera usage (if applicable)

### Setup

1. Clone this repository:
    
    git clone <repository_url>
    cd <repository_directory>
    
2. Create a virtual environment (recommended):
    
     python -m venv myenv
     myenv\Scripts\activate`
    
3. Install dependencies:
    
     pip install -r requirements.txt
    

## Usage

### Laptop Camera Capture

To use the laptop's webcam for capturing images:

1. Run the `capture_with_laptop.py` script:
    
     python capture_with_laptop.py
    
2. When prompted, enter a class name for the object (e.g., `wrapper`, `specs`).
3. If the class already exists, you can choose to add new images to it or change the class name.
4. Start capturing images:
    Press `c` to capture an image.
    Press `q` to stop capturing and exit.

Captured images will be saved in the `./images/<class_name>` directory.

### Mobile Camera Capture

To use a mobile camera for capturing images (via USB/WiFi):

1. Run the `capture_with_mobile.py` script:
    
     python capture_with_mobile.py
    
2. Follow the same prompts and steps as for laptop capture.

## Configuration

- The default save directory for images is `./images/<class_name>`.
- Image capture keys:
  `c` - Capture an image
  `q` - Quit and exit the capture window

## Contributing

Contributions are welcome! If you have suggestions or encounter issues, please open an issue or submit a pull request.
