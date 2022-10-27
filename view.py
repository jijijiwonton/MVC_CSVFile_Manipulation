from model import Model
from controller import Controller

class View:
    
    '''A view method to display loaded data from in-memory data structure'''
    def displayReloadData(self,inMemoryData):
        for count, r in enumerate(inMemoryData):
            if((count+1) % 10 == 0):
                print("Practical Project2 by Jiwon Hwang")
            print(f"{count+1} item(s) displayed")
            print(f"source       | " + r.get_source())
            print(f"latin_name   | " + r.get_latin_name())
            print(f"english_name | " + r.get_english_name())
            print(f"french_name  | " + r.get_french_name())
            print(f"year         | " + r.get_year())
            print(f"month        | " + r.get_month())
            print(f"number       | " + r.get_number())
            print()
            
    '''A view method to display a confirmation message to create a new file'''        
    def confirmCreateNewFile(self, newFileName):
        
        print(f'{newFileName} is created successfully with records.\n')
    
    '''A view method to display one record based on index number'''    
    def displayOneView(self, indexNumber, inMemory):
        print("Practical Project2 by Jiwon Hwang")
        print(f"** Index {indexNumber} record is displayed...")    
        print(f"source       | " + inMemory[indexNumber].get_source())
        print(f"latin_name   | " + inMemory[indexNumber].get_latin_name())
        print(f"english_name | " + inMemory[indexNumber].get_english_name())
        print(f"french_name  | " + inMemory[indexNumber].get_french_name())
        print(f"year         | " + inMemory[indexNumber].get_year())
        print(f"month        | " + inMemory[indexNumber].get_month())
        print(f"number       | " + inMemory[indexNumber].get_number())
        print()
    
    '''A view method to display menu based on while loop to execute the program until the user wants to quit'''        
    def displayMenu(self, model, view):
        
        QUIT_THE_PROGRAM = "0";
        RELOAD_IN_MEMORY_STRUCTURE = "1";
        CREATE_NEW_COMMA_SEPARATED_FILE = "2";
        DISPLAY_ONE_RECORD_IN_MEMORY_STRUCTURE = "3";
        CREATE_NEW_RECORD_IN_MEMORY_STRUCTURE = "4";
        EDIT_NEW_RECORD_IN_MEMORY_STRUCTURE = "5";
        DELETE_ONE_RECORD_FROM_MEMORY_STRUCTURE = "6";
    
        controller = Controller(model, view)
    
        userInput = 1
    
        while(userInput != 0):
            print(RELOAD_IN_MEMORY_STRUCTURE + ": Reload the data from the dataset, replacing the in-memory data.")
            print(CREATE_NEW_COMMA_SEPARATED_FILE + ": Persist the data from memory to the disk as a comma-separated file, writing to a new file.")
            print(DISPLAY_ONE_RECORD_IN_MEMORY_STRUCTURE + ": Select and display either one record, or display multiple records from the in-memory data.")
            print(CREATE_NEW_RECORD_IN_MEMORY_STRUCTURE + ": Create a new record and store it in the simple data structure in memory.")            
            print(EDIT_NEW_RECORD_IN_MEMORY_STRUCTURE + ": Select and edit a record held in the simple data structure in memory.")
            print(DELETE_ONE_RECORD_FROM_MEMORY_STRUCTURE + ": Select and delete a record from the simple data structure in memory.")
            
            '''It acts like a scanner class in Java'''
            userInput = input("Choose an option you want to execute: ")
            print("Practical Project2 by Jiwon Hwang")
            print(userInput)
            
            if userInput == RELOAD_IN_MEMORY_STRUCTURE:
                controller.runReloadData()
                print()
            elif userInput == CREATE_NEW_COMMA_SEPARATED_FILE:
                controller.createNewFile()
                print()
            elif userInput == DISPLAY_ONE_RECORD_IN_MEMORY_STRUCTURE:
                controller.runOneRecord(0)
                print()
            elif userInput == CREATE_NEW_RECORD_IN_MEMORY_STRUCTURE:
                controller.runCreateNewRecord(Model("newSource", "newLatin", "newEnglish", "newFrench", "newYear", "newMonth", "newNumber"))
                print()
            elif userInput == EDIT_NEW_RECORD_IN_MEMORY_STRUCTURE:
                controller.runEditRecord(0, ["editSource", "editLatin", "editEnglish", "editFrench", "editYear", "editMonth", "editNumber"])
                print()
                controller.runOneRecord(0)
                print()
            elif userInput == DELETE_ONE_RECORD_FROM_MEMORY_STRUCTURE:
                controller.runDeleteRecord(1)
                controller.runReloadData()
                print()
            elif userInput == QUIT_THE_PROGRAM:
                print("Thanks for using Jiwon Hwang program!")
                break