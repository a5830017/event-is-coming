from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_title_and_head_at_home(self):
        #Joe and Judy visit this site
        self.browser.get(self.live_server_url)
        #They look at title and header
        self.assertIn('Event Start', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Event', header_text)


    def test_can_create_new_event_and_register(self):
        #Joe wanna create event
        #Joe click link to create event
        self.browser.get(self.live_server_url+'/new_event')
        #Joe look at header
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Create', header_text)

        time.sleep(1)

        #Joe add data in inputbox
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

        inputbox_num.send_keys('10')

        time.sleep(1)

        submit = self.browser.find_element_by_id('id_submit')
        submit.click()

        #Joe success create event and wait for someone interested her event
        #Joe go to sleep

        time.sleep(1)

        #Judy see new event was created
        #Judy interesting this event and click to see event detail

        self.browser.get(self.live_server_url+'/1/')

        time.sleep(1)

        #Judy register her name to this event

        fname_box = self.browser.find_element_by_id('id_firstname')

        fname_box.send_keys('จอน')

        lname_box = self.browser.find_element_by_id('id_lastname')

        lname_box.send_keys('ชาวไร่')

        time.sleep(3)

        submit = self.browser.find_element_by_id('id_submit')
        submit.click()

        #after she submit her name she go to sleep

        time.sleep(3)

        self.fail('Finish the test!')

    
    '''def interested_event_can_register_name(self):
        self.browser.get(self.live_server_url+'/1/')

        self.fail('Finish the test!')'''