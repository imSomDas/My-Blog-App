# Django Blog Website

## Overview

This is a full-featured blog website built using Django. The website allows users to:

- View blog posts on a dedicated blog page.
- Search for posts using keywords.
- Comment on posts and reply to other users' comments.
- Register, log in, and log out.

## Features

1. **Home Page:**
   - A welcoming landing page for users, showcasing key sections like the blog and contact form.

2. **About Page:**
   - Provides details about the blog or the creators.

3. **Contact Form:**
   - A form that allows users to contact the blog admins.
   - Validates input fields and saves the data to the database.

4. **Search Functionality:**
   - Users can search for blog posts using keywords in the title, author, or content.
   - Prevents searches with more than 50 characters to optimize performance.

5. **User Authentication:**
   - Users can sign up, log in, and log out securely using Django's built-in authentication system.
   - Passwords are validated to ensure user security.

6. **Blog Pages:**
   - Lists all blog posts on the main blog page.
   - Each post has its own dedicated page where users can view the full content, post comments, and reply to other comments.

7. **Commenting System:**
   - Users can post comments on blog posts.
   - Replies to comments are also supported and displayed in a nested format.

## Setup and Installation

### Prerequisites

- Python 3.x
- Django 3.x or newer
- A working knowledge of how to run a Django project.

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/django-blog-website.git
   cd django-blog-website
2. **Install the Required Dependencies: Ensure you have pipenv or a similar virtual environment tool:**

   ```bash
   pip install -r requirements.txt
3. Apply Migrations: To set up the database and create the necessary tables, run:

   ```bash
   python manage.py migrate
4. Run the Development Server: Start the Django development server:

   ```bash
   python manage.py runserver
Now, visit http://127.0.0.1:8000/ to see the website in action.

### Usage
**Homepage:** Visit the home page to navigate to different sections of the blog.
**Search:** Use the search bar to find posts by keywords in the title, author name, or content.
**Sign Up / Log In:** Create a new account or log in with an existing one to post comments on blog posts.
**Commenting:** Once logged in, visit a post and leave a comment or reply to existing comments.
