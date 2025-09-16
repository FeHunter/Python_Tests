import csv
import os

file_name = "Tennis_High_Score.csv"
current_dir = os.path.dirname(__file__)

def WriteHighScore(high_score):
    global current_dir, file_name
    file = os.path.isfile(current_dir)
    with open(file_name , mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([high_score])

def ReadHighScore():
    global current_dir, file_name
    if not os.path.isfile(file_name):
        return 0
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(int(row[0]))
            return int(row[0])