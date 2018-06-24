#Kelsey Yim
#Assignment #4
#CPSC 223P

import sqlite3

class table:
    
    def __init__(self, tbl_name):
        self._name = tbl_name
        self._conn = sqlite3.connect('sqtest.db')
        
    # create a table using the attrib names and types        
    def create(self, attib_names, attrb_types):
        col_string = "("
        counter = 0
        for i in attib_names:
            if counter != (len(attib_names)-1):
              #Concatenate string to add SQL formatting {} and ()
                col_string += i       
                col_string += " {at}, ".format(at = attrb_types)
                counter += 1
            else:
                col_string += i
                col_string += " {at})".format(at = attrb_types)
        self._conn.execute('CREATE TABLE IF NOT EXISTS {tn} {at}'\
                           .format(tn = self._name, at = col_string))
    # get the list of attribute names of the table 
    def getAttribNames(self):
        c = self._conn.execute('SELECT * FROM {tn}'.format(tn = self._name))
        #Description is a list of all the column names
        attNames = [description[0] for description in c.description]
        print(attNames)

    # insert a row into the table         
    def addRow(self, attib_vals):
        row_string = "("
        counter = 0
        #Similar concatenation when creating table
        for i in attib_vals:
            if counter != len(attib_vals) - 1:
                row_string += i
                row_string += ', '
                counter += 1
            else:
                row_string += i
                row_string += ')'
                
        self._conn.execute('INSERT INTO {tn} VALUES {rs}'\
                           .format(tn = self._name, rs = row_string))
        
    # returns a cursor  
    def retrieveAll(self):
        return self._conn.cursor()
    # return a cursor pointing to the result set
    
    def performAvgGroupBY(self, avg_col, grpby_col):
        cursorObject = self._conn.cursor()
        #Create a new cursor object to point to average 
        cursorObject.execute('SELECT {gp}, AVG({at}) FROM {tn} GROUP BY {gp}'\
                   .format(gp = grpby_col, at = avg_col, tn = self._name))
        print("The average of all gpa's grouped by cwid: ")
        #Can also use fetchone() that will print out average of student with the most records
        print(cursorObject.fetchall())
        
    def commitChanges(self):
        self._conn.commit()     #Does not automatically save

#Read in the first line of text file and save into list of column names
file = open('userInput.txt',"r")  #r = read only
columnName = file.readline().rstrip('\n')
col_list = columnName.split(',')

table_name = 'Student'

#Test table class methods:
tbl = table(table_name)
tbl.create(col_list, 'TEXT')
for line in file:                 #Read until the end of the file and save
    row_vals = line.split(' ')    #into a list of row_vals
    tbl.addRow(row_vals)
tbl.getAttribNames()
tbl.performAvgGroupBY('gpa', 'cwid')
tbl.retrieveAll()
tbl.commitChanges()
file.close()
