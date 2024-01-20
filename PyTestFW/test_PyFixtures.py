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
    assertAndVerifyData('Shashank',1,'Shashank','pass')
def test_payal_data():
    assertAndVerifyData('Payal',2,'Payal','fail')

def assertAndVerifyData(studentName,id,name,result):
    data = db.get_data(studentName)
    assert data['id'] == id
    assert data['name'] == name
    assert data['result'] == result

# IF you want to run through IDE pycharm
#
# - Tools > Python Integrated Tools > Change default test runner
