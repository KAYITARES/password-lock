
class User:
    """
    Class that generate new instances of password
    """


    user_list = [] #empty user list
    #Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)


    def __init__(self,first_name,last_name,password,confirmation_password):
        '''
        _init_method that helps us define properties for our objects.

        Args:
             first_name:New contact first name.
             last_name:New contact last name.
             password: New user creation password.
             confirmation-password:New user confirmation password
        '''
        # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.confirmation_password = confirmation_password
    