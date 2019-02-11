import unittest # importing the unittest module
from user import User # importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TextCase that help in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("cycy","kaka","vyvy123","vyvy321") # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialiazed properly
        '''

        self.assertEqual(self.new_user.first_name,"cycy")
        self.assertEqual(self.new_user.last_name,"kaka")
        self.assertEqual(self.new_user.password,"vyvy123")
        self.assertEqual(self.new_user.confirmation_password,"vyvy321")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

     # Items up here...

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","fefe121","lili1") #new credential
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

if __name__=='__main__':
    unittest.main()
