
import csv
import sys
import os

def main():

  # Edit these variables to change what you want from the file.
  # ----------------------------------------------------------

  # Input file is the name of the file you want to read and exract data from.
  # The file name needs to match exactly.
  INPUT_FILE = "example.csv"
  
  # Output file is the name of the new file that will be created and written to. 
  # Name this whatever you want.
  OUTPUT_FILE = "export.csv"

  # This a list of all the columns you want from the dataset. 
  # Just add the ones you want separated by commas.
  COLUMNS = ["street_address", "city", "postal_code"]

  # This is a list of all the zipcodes you want to filter in the data set.
  # Just add the ones you want separated by commas.
  ZIPCODES = ["90035"]

  # This increases the maximum file size limit to handle the 2 GB file size of the CSVs.
  csv.field_size_limit(sys.maxsize)

  # This opens one file for reading and one file for writing.
  with open("./files/" + INPUT_FILE, "r") as read_file, open("./export/" + OUTPUT_FILE, "w") as write_file:
    print("\nFile processing...please wait...")
    csv_reader = csv.reader(read_file, delimiter=",")
    csv_writer = csv.writer(write_file, delimiter=",")

    # This variable lets us keep track of what row we are currently on.
    line_count = 0

    # This is map that tells python where each column is in the data set. Each column 
    # has a corresponding index/position that is required to access the data in that column.
    col_map = {}

    # This loops through the entire dataset, row by row, processing each row.
    for row in csv_reader:

      # If the dataset is on the first line, grab all the columns and their positions
      # and add them to the col_map variable. Then write the columns to the new CSV.
      if line_count == 0:
        new_row = []
        for i in range(len(row)):
          if row[i] in COLUMNS:
            col_map[row[i]] = i
            new_row.append(row[i])
        if col_map.keys():
          csv_writer.writerow(new_row)
          line_count += 1
        else:
          raise Exception("The columns you requested are not present in the input file.")

      # Else, the dataset is on a row has data, so we know it needs to be processed.
      # We loop through each row, check to see if its zipcode is in the list of 
      # ZIPCODES defined above. If it is, then grab all the data from that row,
      # and write it to the new CSV file.
      else:
        result = []
        if row[col_map["postal_code"]] in ZIPCODES:
          for key in col_map:
            col = col_map[key]
            result.append(row[col])
          csv_writer.writerow(result)
          result = []
          line_count += 1

    print("\nDone!")
    print("--------------------------------------")
    print("New File Name:\t", OUTPUT_FILE)
    print("Location:\t", "/export/" + OUTPUT_FILE)
    print("Columns:\t", COLUMNS)
    print("Zipcodes:\t", ZIPCODES)
    print("# of records:\t", line_count - 1)
    print("--------------------------------------\n")

if __name__=='__main__':
  main()