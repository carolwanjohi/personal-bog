import unittest
from app.models import User,Role

class TestUser(unittest.TestCase):
    '''
    Test class to test behaviours of the User class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_role = Role(name="Banana Eater")
        self.new_user = User(password='banana', role=self.user_role)

    def test_instance(self):
        '''
        Test case to check if new_user is an instance of User
        '''
        self.assertTrue( isinstance( self.new_user, User) )

    def test_password_setter(self):
        '''
        Test case to ascertain when a password is being hashed and pass_secure contains a value
        '''
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        '''
        Test case to confirm the application raises an AttributeError when we try to access the password property
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        '''
        Test case that confirms that our user password_hash can be verified when we pass in the correct the password
        '''
        self.assertTrue(self.new_user.verify_password('banana'))