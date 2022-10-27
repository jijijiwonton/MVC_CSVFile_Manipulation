import pytest
from controller import Controller
from model import Model
from view import View

'''A test to assert whether the new record is inserted expectedly.'''
def test_addNewRecord():
    model = Model("source", "latin", "english", "french", "year", "month", "number")
    view = View()
    
    controller = Controller(model, view)
    controller.runCreateNewRecord(Model("newSource", "newLatin", "newEnglish", "newFrench", "newYear", "newMonth", "newNumber"))
    
    '''The reason it should be 101 is because I initialize 100 records to display and save it in-memory data structure.'''
    assert 101 == len(controller.inMemoryData)