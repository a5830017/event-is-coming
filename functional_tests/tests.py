from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title_and_head_at_home(self):
        self.browser.get(self.live_server_url)

        self.assertIn('Event Start', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Event', header_text)


    def test_can_create_new_event(self):
        self.browser.get(self.live_server_url+'/new_event')

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Create', header_text)

        time.sleep(1)


        inputbox_event_name = self.browser.find_element_by_id('id_name')
        self.assertEqual(
            inputbox_event_name.get_attribute('placeholder'),
            'Event name'
        )

        inputbox_event_name.send_keys('No idea event')

        time.sleep(1)

        #inputbox.send_keys(Keys.ENTER)
        
        
        inputbox_detail = self.browser.find_element_by_id('id_detail')
        self.assertEqual(
            inputbox_detail.get_attribute('placeholder'),
            'Event detail'
        )

        inputbox_detail.send_keys('share idea for new event')

        time.sleep(1)


        inputbox_location = self.browser.find_element_by_id('id_location')
        self.assertEqual(
            inputbox_location.get_attribute('placeholder'),
            'Event Location'
        )

        inputbox_location.send_keys('Event Hall')

        time.sleep(1)


        inputbox_num = self.browser.find_element_by_id('id_numset')
        self.assertEqual(
            inputbox_num.get_attribute('placeholder'),
            ''
        )

        inputbox_num.send_keys('100')

        time.sleep(1)

        submit = self.browser.find_element_by_id('id_submit')
        submit.click()

        self.fail('Finish the test!')

        

    def interested_event_can_register_name(self):
        self.browser.get(self.live_server_url+'/1/')

        self.fail('Finish the test!')



        