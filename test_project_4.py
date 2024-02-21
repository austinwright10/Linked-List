from SList import SList
from Course import Course
def test_size():
    mylist = SList()
    mylist.insert(1)
    mylist.insert(2)
    mylist.insert(3)
    mylist.insert(4)
    mylist.remove(1)
    assert len(mylist) == 3

def test_insert():
    mylist = SList()
    mycourse = Course(150)
    mylist.insert(3)
    mylist.insert(4)
    mylist.insert(1)
    mylist.insert(2)
    mylist.insert(mycourse.number)
    for value in mylist:
        print(value)

def test_remove_all():
    mylist = SList()
    mylist.insert(1)
    mylist.insert(-2)
    mylist.insert(3)
    mylist.insert(4)
    mylist.insert(1)
    mylist.insert(2)
    mylist.insert(3)
    mylist.insert(4)
    mylist.remove_all(1)
    assert str(mylist) == '[-2, 2, 3, 3, 4, 4]'

def test_get_item():
    mylist = SList()
    mylist.insert(1)
    mylist.insert(2)
    mylist.insert(3)
    mylist.insert(4)
    assert mylist[1] == 2

def test_name():
    my_class = Course(1030, "Introduction to Computers", 4.0, 3.2)
    assert my_class.name == "Introduction to Computers"

def test_greater_than():
    my_class = Course(1030, "Introduction to Computers", 4.0, 3.2)
    second_class = Course(2420, "Algorithms and Data Structures", 3.0, 4.0)
    assert my_class.number < second_class.number
