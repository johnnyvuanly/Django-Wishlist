from django.test import TestCase
from django.urls import reverse

from .models import Place

# Create your tests here.

class TestHomePage(TestCase):
    def test_home_page_shows_empty_list_message_for_empty_database(self):
        home_page_url = reverse('place_list') # from urls.oy name=""
        response = self.client.get(home_page_url) # self is the test case and it has a client and that client makes a request to your webpage
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        # Check for certain content on the page
        self.assertContains(response, 'You have no places in your wishlist')

""" If we want to test that data is in the data base we can use test fixtures. 
That data is loaded into the database before test in one class start running. 
This is inside travel_wishlist folder """
class TestWishList(TestCase):
    # Load the fixture
    fixtures = ['test_users', 'test_places']

    def test_wishlist_contains_not_visited_places(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertContains(response, 'Tokyo')
        self.assertContains(response, 'New York')
        self.assertNotContains(response, 'San Francisco')
        self.assertNotContains(response, 'Moab')

""" Write a test that checks to see the visited page shows an empty place message """
class TestVisitedPage(TestCase):

    def test_visited_page_shows_empty_list_message_for_empty_database(self):
        response = self.client.get(reverse('places_visited')) # Again from urls.py name=""
        # Check if the right template was used
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        self.assertContains(response, 'You have not visited any places yet')

""" Test places that were visited """
class VisitedList(TestCase):

    fixtures = ['test_users', 'test_places']

    def test_visited_list_shows_visited_places(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        self.assertContains(response, 'San Francisco')
        self.assertContains(response, 'Moab')
        self.assertNotContains(response, 'New York')
        self.assertNotContains(response, 'Tokyo')

""" Test for adding new places """
class TestAddNewPlace(TestCase):

    def test_add_new_unvisited_place(self):
        add_place_url = reverse('place_list')
        new_place_data = {'name': 'Tokyo', 'visited': False }

        response = self.client.post(add_place_url, new_place_data, follow=True) # Added arguement follow=True which means make a post request. Two request made in views.py place_list function

        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        response_places = response.context['places']
        self.assertEqual(1, len(response_places)) # check only one place
        tokyo_from_response = response_places[0]

        tokyo_from_database = Place.objects.get(name='Tokyo', visited=False) # Make this is equal to the value that the view sent to the template in the DB

        self.assertEqual(tokyo_from_database, tokyo_from_response)

""" Test that when a places visited request is made to visit a place """
class TestVisitPlace(TestCase):

    fixtures = ['test_users', 'test_places']

    def test_visit_place(self):

        visit_place_url = reverse('place_was_visited', args=(2, )) # Here we can have arguements which turn into data to put into the place holders in the URL. Here we check primary key of 2
        response = self.client.post(visit_place_url, follow=True)

        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # Make sure New York is not there anymore
        self.assertNotContains(response, 'New York')
        # Check if Tokyo is still there
        self.assertContains(response, 'Tokyo')

        new_york = Place.objects.get(pk=2)
        self.assertTrue(new_york.visited)

    def test_non_existent_place(self):
        visit_nonexistent_place_url = reverse('place_was_visited', args=(123456, ))
        response = self.client.post(visit_nonexistent_place_url, follow=True)
        self.assertEqual(404, response.status_code)
