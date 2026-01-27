#This file will hold the test cases for my calculator module

#Pytest is a module that allows us to write our unit tests
#Name our file with our tests using test_.. OR .._test.py 
# The module searches for the files with the 'test' beginning or end

#In order to write our tests with pytest, we need to import 2 things:
#pytest itself
# code from the module we are testing

#Unit testing allows us to test the smallest portion of our code("bite-sized-pieces")
#Unit test directly call the code under the test
# this introduces some considerations for when your code communicates with other systems
#external apis, databases

import pytest
from calculator import add, substract, multiply, divide

#naming convention for python tests
#test_{method name}_{what you are testing for}

def test_add_success():
    
    #Unit tests typically follow an A-A-A structure
    #Arrange, Act, Assert
    
    #arrange - any variables or test data that wwe need to set up 
    x = 4
    y = 8


    #Act - here is where we actually call the code under test
    result = add(x, y)

    #Assert - we know what data was fed in, we know what we should get back
    #we assert the result is what was intended

    assert result == 12

def test_divide_success():

    #AAA

    #Arrange
    x = 5
    y = 9

    #Act
    result = divide(x, y)

    #Assert
    assert result == 5 / 9

def test_divide_divide_by_zero_exception():

    x = 4
    y = 0 # intentionally dividing by zero




    with pytest.raises(ValueError) as ex:
        divide(x, y) #inside this with we call the method

    #Assert
    #Cast to a string for easy comparison
    assert str(ex.value) == "Cannot divide by zero"