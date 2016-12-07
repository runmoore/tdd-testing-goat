from django.conf import settings
from .base import FunctionalTest
from .server_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session


class MyListsTest(FunctionalTest):

	def create_pre_authenticated_session(self, email):
		if self.against_staging:
			session_key = create_session_on_server(self.server_host, email)
		else:
			session_key = create_pre_authenticated_session(email)

		# to set a cookie we first need to vist the domain
		# 404 pages load the quickest!
		self.browser.get(self.server_url + "/404_no_such_url/")
		self.browser.add_cookie(dict(
			name=settings.SESSION_COOKIE_NAME,
			value=session_key,
			path='/',
		))

	def test_logged_in_users_lists_are_saved_as_my_lists(self):
		email = 'edith@example.com'
		self.browser.get(self.server_url)
		self.assert_logged_out(email)

		# Edith is a logged-in user
		self.create_pre_authenticated_session(email)
		self.browser.get(self.server_url)
		self.assert_logged_in(email)

	def test_logged_in_users_lists_are_saved_as_my_lists(self):
		# Chris is a logged-in user
		self.create_pre_authenticated_session('chris@example.com')

		# He goes to the home page and starts a list
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('Reticulate splines\n')
		self.get_item_input_box().send_keys('Immanetize eschaton\n')
		first_list_url = self.browser.current_url

		# He notices a "My lists" link for the first time
		self.browser.find_element_by_link_text('My lists').click()

		# He finds that her list is in there, named according to its
		# first line item
		self.browser.find_element_by_link_text('Reticulate splines').click()
		self.assertEqual(self.browser.current_url, first_list_url)

		# He decides to start another list
		self.browser.get(self.server_url)
		selg.get_item_input_box().send_keys('Click cows\n')
		second_list_url = self.browser.current_url

		# Under "my lists", his new list appears
		self.browser.find_element_by_link_text('My lists').click()
		self.browser.find_element_by_link_text('Click cows').click()
		self.assertEqual(self.browser.current_url, second_list_url)

		# He logs out. The 'My lists' option disappears
		self.browser.find_element_by_link_text('Log out').click()
		self.assertEqual(
			self.browser.find_element_by_link_text('My lists'),
			[]
		)






