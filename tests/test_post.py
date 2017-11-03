import unittest
from app.models import Post

class TestRole(unittest.TestCase):
    '''
    Test class to test behaviours of the Post class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post(post_title='Banana', post_content='I eat bananas. I love bananas')
        
    def test_instance(self):
        '''
        Test case to check if new_post is an instance of Post
        '''
        self.assertTrue( isinstance( self.new_post, Post) )

    def test_save_post(self):
        '''
        Test case to check if a post is saved to the database
        '''

        self.new_post.save_post()

        self.assertTrue( len(Post.query.all()) > 0 )

    def test_get_posts(self):
        '''
        Test case to check if all posts are returned by the get_posts function
        '''

        self.new_post.save_post()

        test_post = Post(post_title='Banana v.2', post_content='Bananas are yellow')

        test_post.save_post()

        gotten_posts = Post.get_posts()

        self.assertTrue( len(gotten_posts) == len(Post.query.all()) )

    def test_delete_post(self):
        '''
        Test case to check if test_post is deleted from the database
        '''

        self.new_post.save_post()

        test_post = Post(post_title='Banana v.2', post_content='Bananas are yellow')

        test_post.save_post()

        test_post.delete_post(test_post.id)

        gotten_posts = Post.get_posts()

        self.assertTrue( len(gotten_posts) == len(Post.query.all()) )







