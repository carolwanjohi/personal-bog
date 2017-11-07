# the C blog
## This is a personal blogging website where [I](https://github.com/carolwanjohi) can create and share my opinions via a blog post and other users can read and comment on posts, 3/11/2017


## By **[Carol Wanjohi](https://github.com/carolwanjohi)**

## Description
[This](https://python-personal-blog.herokuapp.com/) is a web application that allows me, as a writer, to create blog posts to share my opinions. Users, who are readers, can reader my posts and comment on them. They can also subscribe for updates when there is a new blog post.<br>

Other functionalities that the writer has are: <br>
- deleting a post
- updating a post
- deleting comments that the writer finds insulting or degrading

## User Stories
As a user I would like:
* to view the blog posts submitted
* to comment on blog posts
* to be alerted when a new post is made by joining a subscription. <br>

As a writer I would like:
* to sign in to the blog.
* to create blog posts from the application.
* to delete comments that I find insulting or degrading.
* to update or delete blogs posts I have created.

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email : jane@doe.com <br> Username : jane101 <br> Password : doe1 | New user is registered |
| User Log in | Your email : jane@doe.com <br> Password : doe1 | Logged in |
| Display post title | N/A | List of post titles with the writer's name |
| See an entire post | **Click** on a **post's title** | Directed to a page with the post's title, writer's name and comments on the post |
| Comment on a post | **Click Comment** | An authenticated user is directed to a page with a form where the user can create and submit a comment on a post |
| Writer Log in | Your email : writer@login.com <br> Password : writer | Logged in and can access writer's routes |
| Create a Post | **Click Create Post** | An authenticated user with a writer's role is directed to a page with a form where the user can create and submit a new post |
| Delete a comment | **Click delete** for the specific comment | An authenticated user with a writer's role deletes a comment |
| Delete a post | **Click Delete Post** | An authenticated user with a writer's role deletes a post and its comments |
| Update a post | **Click Update Post** | An authenticated user with a writer's role is directed to a page with a form where the user can update the post and submit it |

## Setup/Installation Requirements

* Click [the C blog](https://python-personal-blog.herokuapp.com/) <br/>
  or <br/>
* Copy [the C blog](https://python-personal-blog.herokuapp.com/) and  Paste the link on your prefered browerser

This requires internet connection.

## Known Bugs

No known bugs

## Technologies Used
- Python3.6
- Flask
- Bootstrap
- Postgres Database
- CSS
- HTML

### License

MIT (c) 2017 **[Carol Wanjohi](https://github.com/carolwanjohi)**



