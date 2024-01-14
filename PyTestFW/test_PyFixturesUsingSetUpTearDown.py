import pytest

from PyTestFW.StudentDB import StudentDB


@pytest.fixture(scope='module')
def db():
    print('------------------set up method --------------------------------')
    db= StudentDB()
    db.connect("C:\\Users\\poona\\PycharmProjects\\LearnSelenium\\TestData\\data.json")
    yield db

    print('------------------tear down method------------------------')
    db.close()

def test_shashank_data(db):
    # db = StudentDB()
    # db.connect("C:\\Users\\poona\\PycharmProjects\\LearnSelenium\\TestData\\data.json")
    shashank_data = db.get_data("Shashank")
    assert shashank_data['id'] == 1
    assert shashank_data['name'] == 'Shashank'
    assert shashank_data['result'] == 'pass'


def test_payal_data(db):
    # db = StudentDB()
    # db.connect("C:\\Users\\poona\\PycharmProjects\\LearnSelenium\\TestData\\data.json")
    payal_data = db.get_data("Payal")
    assert payal_data['id'] == 2
    assert payal_data['name'] == 'Payal'
    assert payal_data['result'] == 'fail'
