
class Credential:
    """
    Class that generate new instances of credential
    """

    credential_list = [] #empty credential list
    #Init method up here
    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a credential that matches that name.

        Args:
            name: name to search for
        Returns :
            Credential of person that matches the name.
        '''

        for credential in cls.credential_list:
            if credential.password == name:
                return credential


    def __init__(self,account_name,password):
        '''
        _init_method that helps us define properties for our objects.

        Args:
             account_name:New credention account name.
             password:New credential password.
             
        '''
         # docstring removed for simplicity

        self.account_name = account_name
        self.password = password
          