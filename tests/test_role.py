import unittest
from app.models import Role

class TestRole(unittest.TestCase):
    '''
    Test class to test behaviours of the Role class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_role = Role(name='banana')
        
    def test_instance(self):
        '''
        Test case to check if new_role is an instance of Role
        '''
        self.assertTrue( isinstance( self.new_role, Role) )
