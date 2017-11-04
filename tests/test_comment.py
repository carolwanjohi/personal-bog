import unittest
from app.models import Comment,Post

class TestComment(unittest.TestCase):
    '''
    Test class to test behaviours of the Comment class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment(comment_content="You need more practice with your grammar")

    def test_instance(self):
        '''
        Test case to check if new_comment is an instance of Comment
        '''

        self.assertTrue( isinstance( self.new_comment, Comment) )

    def test_save_comment(self):
        '''
        Test case to check if a comment is saved to the databse
        '''

        self.new_comment.save_comment()

        self.assertTrue( len(Comment.query.all()) > 0)

    def test_get_comments(self):
        '''
        Test case to check if a comment and its information is returned by the get_comments function that takes in an id and match it to a post id
        '''
        self.new_comment.save_comment()

        gotten_comments = Comment.get_comments(4990826417581240726341234)

        self.assertFalse( len(gotten_comments) == 1)

    def test_delete_single_comment(self):
        '''
        Test case to check if test_comment is deleted from the database
        '''

        self.new_comment.save_comment()

        test_comment = Comment(comment_content="You work is crap")

        test_comment.save_comment()

        test_comment.delete_single_comment(test_comment.id)

        gotten_comments = Comment.get_comments(4990826417581240726341234)

        self.assertFalse( len(gotten_comments) == len(Comment.query.all()) )




