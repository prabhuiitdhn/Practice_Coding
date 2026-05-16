'''
https://stackoverflow.com/questions/419163/what-does-if-name-main-do
https://stackabuse.com/what-does-if-__name__-__main__-do-in-python/
'''

'''
__name__ is the special variable that defines the name of the variable, current module, or the scripts which it get invoked.
when python interpreter runs the scripts It, the interpreter reads the scripts and assign the string __main__ to __name__ keyword.
The __name__ == "__main__" runs blocks of code only when our Python script is being executed directly from a user. This is powerful as it allows our code to have different behavior when it's being executed as a program instead of being imported as a module.

When writing large modules, we can opt for the more structured approach of having a __main__.py file to run a module. For a stand-alone script, including the if __name__ == "__main__" is a simpler method to separate the API from the program.
'''

'''
Docstring(Documentation string; which helps to create the documentation for the function, class and method and whatever.): It creates the documentation for python code within the code.
This in-code documentation works for modules, classes, methods, and functions, and it is the preferred way to document all Python code.
 https://stackabuse.com/python-docstrings/
'''


class Device:
    def __init__(self, temp):
        "Initialised the devide."  # it is the docstring()
        self.temprature = temp

    def get_temp(self):
        '''Retrun the temp'''
        return self.temp()

    def set_temp(self):
        """ set the temp value"""
        self.temprature = 50.0

    def multiLine(self):
        """
        This is for multiline string, where we can add multiple line
        like we can write something at line 1
        line2
        :return:
        """
