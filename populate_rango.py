import os  # Import the os module to interact with the operating system
import random
# Set the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django  # Import Django

# Set up Django (must be done before working with models)
django.setup()

# Import the Category and Page models from the Rango app
from rango.models import Category, Page


def populate():
    """
    Populates the database with initial data.
    - Creates categories.
    - Adds related pages to each category.
    """

    # Define a list of dictionaries for Python-related pages
    python_pages = [
        {'title': 'Official Python Tutorial',  # Title of the page
         'url': 'http://docs.python.org/3/tutorial/'},  # URL of the page

        {'title': 'How to Think like a Computer Scientist',  # Title of the page
         'url': 'http://www.greenteapress.com/thinkpython/'},  # URL of the page

        {'title': 'Learn Python in 10 Minutes',  # Title of the page
         'url': 'http://www.korokithakis.net/tutorials/python/'}  # URL of the page
    ]

    # Define a list of dictionaries for Django-related pages
    django_pages = [
        {'title': 'Official Django Tutorial',  # Title of the page
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},  # URL of the page

        {'title': 'Django Rocks',  # Title of the page
         'url': 'http://www.djangorocks.com/'},  # URL of the page

        {'title': 'How to Tango with Django',  # Title of the page
         'url': 'http://www.tangowithdjango.com/'}  # URL of the page
    ]

    # Define a list of dictionaries for other frameworks' pages
    other_pages = [
        {'title': 'Bottle',  # Title of the page
         'url': 'http://bottlepy.org/docs/dev/'},  # URL of the page

        {'title': 'Flask',  # Title of the page
         'url': 'http://flask.pocoo.org'}  # URL of the page
    ]

    # Dictionary containing categories and their corresponding pages
    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}
    }

    # If you want to add more categories or pages,
    # simply extend the dictionaries above.

    # Loop through each category in the dictionary
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])  # Pass the expected values
        for p in cat_data['pages']:  # Loop through pages in this category
            add_page(c, p['title'], p['url'])  # Add the page to the category

    # Print out all categories and their associated pages
    for c in Category.objects.all():  # Loop through all categories
        for p in Page.objects.filter(category=c):  # Get all pages for this category
            print(f'- {c}: {p}')  # Print category name and page title


def add_page(cat, title, url, views=None):
    if views is None:
        views = random.randint(1, 100)  # assign random views (1-100)
    """
    Adds a page to the database.
    If the page already exists, it is retrieved instead.
    """
    p = Page.objects.get_or_create(category=cat, title=title)[0]  # Get or create the page
    p.url = url  # Assign the URL to the page
    p.views = views  # Assign the number of views (default is 0)
    p.save()  # Save the page to the database
    return p  # Return the created or retrieved page object


def add_cat(name,views =0, likes=0):
    """
    Adds a category to the database.
    If the category already exists, it is retrieved instead.
    """
    c = Category.objects.get_or_create(name=name)[0]  # Get or create the category
    c.views = views #assign th eviews value
    c.likes = likes #assign the likes value
    c.save()  # Save the category to the database
    return c  # Return the created or retrieved category object


# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')  # Print a message to indicate script start
    populate()  # Call the populate function to populate the database

#CAT FOR CATAGORY NOT THE ANIMALOLLLLL
#The __name__ == '__main__' trick is a useful one that allows a Python module
#to act as either a reusable module or a standalone Python script.
#Code within a conditional if __name__ == '__main__' statement will therefore
#only be executed when the module is run as a standalone Python script.
