#! python3
# removeCsvHeader.py    - removes header from a csv file

import csv, os

# TODO - Find all files that end with .csv

os.makedirs('headerRemoved', exist_ok=True)


# TODO - open each csv file, read contents and write (w/o the first line) into
# a new csv file

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    print('Removing header from ' + csvFilename + '...')

    csvRows = []
    
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    
    csvFileObj.close()

    # Write out the CSV file

    csvFileObjWrite = open(os.path.join('headerRemoved', csvFilename), 'w',
                           newline ='')
    csvWriter = csv.writer(csvFileObjWrite)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObjWrite.close()
    
