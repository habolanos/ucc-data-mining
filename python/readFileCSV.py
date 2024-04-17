# Python3 program to read CSV file using DictReader

# Import necessary packages
import csv

# Open file
with open('samplecsv.csv') as file_obj:
	# Create reader object by passing the file
	# object to DictReader method
	reader_obj = csv.DictReader(file_obj)
	# Iterate over each row in the csv file
	# using reader object
	for row in reader_obj:
		print(row)
