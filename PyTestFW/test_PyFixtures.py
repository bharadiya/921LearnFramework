import pytest

from PyTestFW.StudentDB import StudentDB

db = None
def setup_module(module):
    print('------------------set up method --------------------------------')
    global db
    db= StudentDB()
    db.connect("C:\\Users\\poona\\PycharmProjects\\LearnSelenium\\TestData\\data.json")

def teardown_module(module):
    print('------------------tear down method------------------------')
    db.close()

def test_shashank_data():
    checkData("Shashank","Shashank",1,"pass")

def test_payal_data():
    checkData("Payal","Payal",2,"fail")

def checkData(name,verifyName,verifyID,verifyResult):
    data = db.get_data(name)
    assert data['id'] == verifyID
    assert data['name'] == verifyName
    assert data['result'] == verifyResult






# IF you want to run through IDE pycharm
#
# - Tools > Python Integrated Tools > Change default test runner
