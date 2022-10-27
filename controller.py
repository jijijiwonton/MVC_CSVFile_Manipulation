class Controller:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.inMemoryData = self.model.reloadData()
    
    '''A method to reload the data from the dataset, replacing the in-memory data.'''
    def runReloadData(self):
        self.view.displayReloadData(self.inMemoryData)
        
    '''A method to persist the data from memory to the disk as a comma-separated file, writing to a new file.'''
    def createNewFile(self):
        newFileCreated = self.model.writeNewFileWithCommaSeparated("new_file.csv")
        self.view.confirmCreateNewFile(newFileCreated)
    
    '''A method to select and display either one record, or display multiple records from the in-memory data.'''
    def runOneRecord(self, indexNumber):
        self.view.displayOneView(indexNumber, self.inMemoryData)

    '''A method to create a new record and store it in the simple data structure in memory.'''
    def runCreateNewRecord(self, newRecord):
        self.model.createNewRecord(self.inMemoryData, newRecord)
    
    '''A method to select and edit a record held in the simple data structure in memory.'''
    def runEditRecord(self, indexNumber, values=[]):
        self.model.editRecord(indexNumber, self.inMemoryData, values)
        
    '''A method to select and delete a record from the simple data structure in memory.'''    
    def runDeleteRecord(self, indexNumber):
        self.model.deleteOneRecord(indexNumber, self.inMemoryData)
    
    '''A method to execute the program.'''    
    def executeProgram(self):
        self.view.displayMenu(self.model, self.view)
        
        