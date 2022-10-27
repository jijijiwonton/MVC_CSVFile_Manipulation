from model import Model
from view import View
from controller import Controller

class Main:

    model = Model("Source", "latin", "english", "french", "year", "month", "number")
    view = View()

    '''Based on MVC architecture, controller is manipulating data for model and updating display for view.'''    
    controller = Controller(model, view)
    
    controller.executeProgram()
    