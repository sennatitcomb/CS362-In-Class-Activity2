import pytest
def wordcount(userinput):
    if type(userinput) == str:
        count = len(userinput.split(" "))
        #print(userinput)
        return count
    else:
        return 0
def test_1():
    assert wordcount("tree bear thorn") == 3
def test_2():
    assert wordcount("flower bee") == 2
def test_3():
    assert wordcount(24) == 0