
<h1 align="center">Bar Code ISBN Scanner</h1>

![QR Code Scanner](https://github.com/salmanpython06/ISBN_BARCODE_READER/blob/main/1.png)


## Introduction
This Github project is for capturing video from a camera in real-time and scans for QR codes. If a QR code with an ISBN number is found, it queries the Google Books API to fetch book information such as title, authors, publish date, and description. It then stores this information in a CSV file, avoiding duplicates based on ISBN numbers. The script runs until the user decides to stop it and gracefully closes the camera and windows afterwards. The main purpose of the script is to create a system for scanning QR codes from books, retrieving their details from an online database, and storing the information in a CSV file



## Installation
To run the Bar code ISBN Scanner, follow these steps:

1. Clone the repository to your local machine using the following command:
    - git clone https://github.com/salmanpython06/ISBN_BARCODE_READER.git

2. create a virtual environment:
    - cd ISBN_BARCODE_READER
    - pip install virtualenv
    - python -m venv myenv
3. install all modules:
    - pip install -r requirements.txt
4. run the code:
    - python main.py

Happy Scanning!
