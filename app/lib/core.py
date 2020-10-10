from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from random import randint
import time
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import math

load_dotenv()

def Scholiast(test=False):

	driver = Firefox()
	driver.implicitly_wait(7)
			
	def get_now():
		now = datetime.now()
		return now.strftime("%H:%M:%S")

	def get_future(ref_time, minutes):
		future = ref_time + timedelta(minutes=minutes)
		return future.strftime("%H:%M:%S")

	def login():
		driver.get('https://instagram.com')

		username = driver.find_element_by_name('username')
		password = driver.find_element_by_name('password')

		enable_login = "document.getElementsByClassName('sqdOP')[0].removeAttribute('disabled')"
		driver.execute_script(enable_login)

		login_btn = driver.find_elements_by_css_selector('.sqdOP')[0]

		username.send_keys(os.getenv('IGUSER'))
		password.send_keys(os.getenv('PASSWORD'))
		login_btn.send_keys(Keys.ENTER)
		time.sleep(5)

	def comment(post_url, comment_content, interval_minutes=(30, 40)):

		print('Executing Scholiast with:')
		print('-', post_url)
		print('-', comment_content if len(comment_content) < 10 else len(comment_content) + ' registers')
		
		driver.get(post_url)
		time.sleep(2)

		post_btn_xpath = '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button'

		count = 1
		while True:
			print('[', get_now(), '] Round: ', count)

			get_out = False
			for comment in comment_content:

				if get_out:
					break

				print('[', get_now(), '] Commenting', comment)

				# Write
				enable_textarea = "document.getElementsByClassName('Ypffh')[0].removeAttribute('disabled')" # Textarea may be disabled
				driver.execute_script(enable_textarea)

				comment_area = driver.find_element_by_class_name('Ypffh')
				comment_area.click()

				comment_area = driver.find_element_by_class_name('Ypffh')
				comment_area.send_keys(comment)

				# Click post
				if not test:
					btn_comment = driver.find_element_by_xpath(post_btn_xpath)
					btn_comment.click()

					# Check if comment was successfuly made
					try:
						error_box = driver.find_element_by_class_name('gxNyb')
						if error_box:
							print(comment, 'could not be done. Refreshing page before next batch...')
							driver.refresh()
							get_out = True
					except:
						get_out = False
						pass

			count+=1

			next_time = math.floor(randint(interval_minutes[0] * 60, interval_minutes[1] * 60)) if get_out == False else 30 * 60
			print('Waiting', next_time / 60, ' minutes')
			print('Next batch at', get_future(datetime.now(), next_time / 60), '\n')
			time.sleep(next_time)

	return login, comment


