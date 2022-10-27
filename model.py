'''Due date: 2022/10/14
 Student name: Jiwon Hwang
 Student number: 040991933
 Description: Create MVC architecture and manipulate data from in-memory data structure based on MVC structure.'''

'''Import csv library'''
import csv

class Model:
    
    '''Define a constructor'''
    def __init__(self, source, latin_name, english_name, french_name, year, month, number):
        self.source = source
        self.latin_name = latin_name
        self.english_name = english_name
        self.french_name = french_name
        self.year = year
        self.month = month
        self.number = number
    
    '''Encapsulation accessors and mutators'''
    def get_source(self):
        return self.source
    
    def set_source(self, source):
        self.source = source
        
    def get_latin_name(self):
        return self.latin_name
    
    def set_latin_name(self, latin_name):
        self.latin_name = latin_name
        
    def get_english_name(self):
        return self.english_name
    
    def set_english_name(self, english_name):
        self.english_name = english_name
    
    def get_french_name(self):
        return self.french_name
    
    def set_french_name(self, french_name):
        self.french_name = french_name
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year 
        
    def get_month(self):
        return self.month
    
    def set_month(self, month):
        self.month = month
        
    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number
        
    '''Reload the data from the dataset, replacing the in-memory data.'''
    def reloadData(self):
        fileName = 'NAFO-4TVN-Atlantic-Cod-otoliths.csv'
        records = []
        inMemoryData = []
        
        try:
            with open(fileName, 'r') as csvfile:
                reader = csv.reader(csvfile)
                
                next(reader)
                for data in reader:
                    dataSet = Model(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        
                    records.append(dataSet)
                
                for count, r in enumerate(records):
                    
                    if(count < 100):
                        inMemoryData.append(r)
                    else:
                        break      

            return inMemoryData
                    
        except FileNotFoundError:
            print(f"${fileName} file doesn't exist")
            
    '''Persist the data from memory to the disk as a comma-separated file, writing to a new file.'''
    def writeNewFileWithCommaSeparated(self, newFileName):

        with open('NAFO-4TVN-Atlantic-Cod-otoliths.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            with open(newFileName, 'w') as new_csv_file:
                csv_writer = csv.writer(new_csv_file, delimiter=',')
                
                for record in csv_reader:
                    csv_writer.writerow(record)
                
        return newFileName
   
    '''Create a new record and store it in the simple data structure in memory'''
    def createNewRecord(self, inMemoryData, newRecord):

        inMemoryData.append(newRecord)
        return inMemoryData
            
    '''Select and edit a record held in the simple data structure in memory'''
    def editRecord(self, indexNumber, inMemoryData, values=[]):
       
        inMemoryData[indexNumber].set_source(values[0])
        inMemoryData[indexNumber].set_latin_name(values[1])
        inMemoryData[indexNumber].set_english_name(values[2])
        inMemoryData[indexNumber].set_french_name(values[3])
        inMemoryData[indexNumber].set_year(values[4])
        inMemoryData[indexNumber].set_month(values[5])
        inMemoryData[indexNumber].set_number(values[6])
        
        return values
        
    '''Select and delete a record from the simple data structure in memory'''
    def deleteOneRecord(self, indexNumber, inMemoryData):
        del inMemoryData[indexNumber]
        

                    

    