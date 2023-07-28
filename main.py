"""
        Code by: SalmanMallah
        gmail: pythonsalman06@gmail.com
"""
import cv2 # opencv
import requests
import numpy as np
import pandas as pd
import os 
import pyzbar.pyzbar as pyzbar
from csv import DictWriter

isbn = ''
cam = cv2.VideoCapture(0)

def datasave(isbn):
    isbn = str(isbn)
    isbn = isbn[2:-1]

    # fetching the data using isbnlin
    print(f"========={isbn}===========")
    URL = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(isbn)
    # print(URL)
    r = requests.get(url=URL)
    data = r.json()
    try:
        # parsing the isbnlin response into required variables
        book_info = data["items"][0]["volumeInfo"]

        title = book_info.get("title")
        authors = book_info.get("authors")
        publish_date = book_info.get("publishedDate")
        isbn = book_info.get("industryIdentifiers")[0]["identifier"]
        description = book_info.get("description")
        print("\n\n\n")

        table = {"title": title, "authors": authors, "isbn": isbn, "publish_date": publish_date, "description": description}

        # creating a data frame using panda
        df = pd.DataFrame(table)

        # appending book data into csv file
        with open('book_data.csv', 'a', newline="") as wf:
            dict_writer = DictWriter(wf, fieldnames=['title', 'authors', 'isbn', 'publish_date', 'description'])
           
            # checking if file has headers or not and adding the it if does not have
            if os.stat('book_data.csv').st_size == 0:
                dict_writer.writeheader()
            
            else:
                read_csv = pd.read_csv("book_data.csv", dtype={"isbn": str})
                '''By default, pandas interprets numeric columns in the CSV as numeric data types, and leading zeros in integers are ignored.
                  This behavior is consistent with how integers are usually handled in programming languages like Python.
                To preserve leading zeros in the ISBN numbers, you need to explicitly specify that the "isbn" column should be treated as a string (object) data type during the CSV read operation.
                  You can do this by setting the dtype parameter of pd.read_csv()'''
                
                check_isbn = read_csv["isbn"].tolist()
                print(check_isbn)

                # checking if isbn number is already present in our file
                if isbn in check_isbn:
                    print("Book is already registered...")
                
                # if isbn is not already present, adding it
                else:
                    print(f"this isbn: {isbn} not matched")
                    df.to_csv('book_data.csv', mode='a', header=False, index=False)
    
    except KeyError:
        print("Invalid ISBN\nPlease Try again!")
 
# scanning QR Code from Camera
while True:
    _, frame = cam.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        isbn = obj.data

        datasave(isbn)
    cv2.imshow("Scan QR code Prehss ESC to quite.", frame)
    key = cv2.waitKey(1)

    if key == 27:
        print("You Quite the Screen")
        break


cam.release()
cv2.destroyAllWindows()