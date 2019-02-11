import unittest # importing the unittest module
from credential import Credential # importing the user class

class TestCredential(unittest.TestCase):

    '''
    Test class that defines text cases for the credential class behaviours.

    Args:
        unittest.TestCase: TextCase that help in creating text cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("cycy","vyvy321") # create credential object

    def test_init(self):
        '''
        test_init test case to test if the object is initialiazed properly
        '''

        self.assertEqual(self.new_credential.account_name,"cycy")
        self.assertEqual(self.new_credential.password,"vyvy321")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new contact
        self.assertEqual(len(Credential.credential_list),1)

    # Items up here...

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","user") #new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    #setUp and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    # other test cases here
    def test_save_multiple_credential(self):
        '''
        test_save _multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","user") #new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    # More tests above
    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user") # new user
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a user object
            self.assertEqual(len(Credential.credential_list),1)


    def test_find_credential_by_name(self):
        '''
        test to check if we can find a credential by name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_name("user")

        self.assertEqual(found_credential.password,test_credential.password)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the password.
        '''

        self.credential.save_credential()
        test_credential = Credential("Test","user") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("user")

        self.assertTrue(credential_exists)

if __name__=='__main__':
        unittest.main()