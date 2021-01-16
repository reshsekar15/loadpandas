
'''
Author: Reshma Sekar
Date: 01.16.2021
Function name: clean_string 
Function description: Function takes in a value, converts this to a string and removes any leading or trailing spaces
'''

def clean_string(value):
    value = str(value).lstrip()
    value = str(value).rstrip()
    return value


'''
Author: Reshma Sekar
Date: 01.16.2021
Function name: find_header 
Function description: Function takes in column names, dataframe and matches each row against columns to find the header row
If no header exists, the function could be slow as it is reading every row till the end of file to look for a match.
Function returns -1 if the header has already been read. 
Function returns the header row as integer if it is found
Function returns -1 if no header is found in file
'''
def find_header(cols, data):
    existing_cols = data.columns
    for each_col in existing_cols:
        each_col = clean_string(each_col)
        if(each_col in cols):
            return 0
    for each_row in range(0, len(data.index)):
        row = data.iloc[each_row]
        row = row.str.strip()
        row_is_header = True
        for each_col in cols: 
            if(each_col in row.values) == False:
                row_is_header = False
        if(row_is_header == True):
            return each_row+1
    return -1

'''
Author: Reshma Sekar
Date: 01.16.2021
Function name: find_header 
Function description: Function takes in column names, dataframe, and a threshold value. The function reads only the threshold number 
of rows(threshold value * number of rows, eg; 0.01 reads 1% of the rows in file) to find the header.
Function returns -1 if the header has already been read. 
Function returns the header row as integer if it is found
Function returns -1 if no header is found in file
'''
def find_header_limited(cols, data, row_limit):
    existing_cols = data.columns
    for each_col in existing_cols:
        each_col = clean_string(each_col)
        if(each_col in cols):
            return 0
    for each_row in range(0, len(data.index)*row_limit):
        row = data.iloc[each_row]
        row = row.str.strip()
        row_is_header = True
        for each_col in cols: 
            if(each_col in row.values) == False:
                row_is_header = False
        if(row_is_header == True):
            return each_row+1
    return -1
