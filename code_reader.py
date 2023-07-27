"""
        Code by: SalmanMallah
        gmail: pythonsalman06@gmail.com
"""
import cv2 # opencv
import requests
import numpy as np
import pandas as pd
import pyzbar.pyzbar as pyzbar

isbn = ''
cam = cv2.VideoCapture(0)

global a
a=0

def datasave(a,isbn):
    isbn = str(isbn)
    isbn = isbn[2:-1]

    # fetching the data using isbnlin
    print(f"========={isbn}===========")
    URL = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(isbn)
    print(URL)
    r = requests.get(url=URL)
    data = r.json()
    try:
        book_info = data["items"][0]["volumeInfo"]

        title = book_info.get("title")
        authors = book_info.get("authors")
        publish_date = book_info.get("publishedDate")
        isbn = book_info.get("industryIdentifiers")[1]["identifier"]
        description = book_info.get("description")
        print("\n\n\n")
        table = {"title": title, "authors": authors, "isbn": isbn, "publish_date": publish_date, "description": description}
        # print(table)

        df = pd.DataFrame(table)
        df.iloc[a:]=df
        print(df.iloc[a:])
        print(a)
        df.to_csv('data.csv', mode='a', header=False, index=False)
    except KeyError:
        print("Invalid ISBN\nPlease Try again!")
 

while True:
    _, frame = cam.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        isbn = obj.data
        a=a+1
        datasave(a,isbn)
    cv2.imshow("Scan QR code Prehss ESC to quite.", frame)
    key = cv2.waitKey(1)

    if key == 27:
        print("You Quite the Screen")
        break


cam.release()
cv2.destroyAllWindows()
