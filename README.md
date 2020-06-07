# Transcity 🚗🚄🚲
CSV file filtering/extraction tool for Trevor Hyman's Transcity MID thesis project.

### Instructions 📝
1. [Download Python 3](https://www.python.org/downloads/)
2. Download or clone the project
3. Open the project folder and pop all the files you want to work with in the `files` folder. Make sure there are no sub folders in the `files` folder. 

### How to Filter 🔥
If you open up the `transcity.py` file, you'll see I included 4 variables at the top of the main function:
```
INPUT_FILE = "December2.csv"

OUTPUT_FILE = "test.csv"

COLUMNS = ["street_address", "city", "postal_code"]

ZIPCODES = ["90036", "90035"]
```
You need to edit these values so that they point to the right files and filter the right data. I left some comments in the code, but here's a description of each variable:
- INPUT_FILE    --> the name of the file you want to extract data from
- OUTPUT_FILE   --> the name of the new file that will be created from the extraction
- COLUMNS       --> a list of all the columns you want from the input file
- ZIPCODES      --> a list of all the zipcodes you want to filter the dataset by

INPUT_FILE and OUTPUT_FILE are just for reading the right file and naming the new file that will be generated. COLUMNS and ZIPCODES are what you use to filter the data. Make sure all of these values are __exact__ matches.

### How to Export 💯
Once you have the 4 variables configured, you're ready to export:
1. Open "Terminal" on your Mac
2. Type `cd Downloads/Transcity` and hit enter; you are now inside of the folder you just downloaded
3. Type `python transcity.py` and hit enter; the file is now being processed

When the file is finished processing, it should appear in the `export` folder with the name you assigned to the OUTPUT_FILE variable.