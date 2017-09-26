from selenium import webdriver # webdriver is a module
from selenium.webdriver.common.keys import Keys # keys is a class
import unicodedata

import datetime, time, re, csv, sys # datetime, time,re, csv, sys are modules
import config # confi is module
SLEEP_SECONDS = 4
# RE_REMOVE_HTML = re.compile('<.+?>')

class TuroCrawler:

	def __init__(self):
		self.driver = webdriver.Chrome("/Users/su/Desktop/project/turotrytry/turo-automation_copy_forme/chromedriver")
		self.driver.set_page_load_timeout(30)
        # self.driver.set_page_load_timeout(30)

	def crawl(self, outfile):
		self.login()
		time.sleep(SLEEP_SECONDS)
		trips = self.get_trips()
		# self.write_to_file(trips, outfile)
		# self.stop()
		# unchange
	def login(self):
		self.driver.get('https://turo.com/login')

		username = self.driver.find_element_by_id('username')
		username.send_keys(config.TURO_USERNAME)

		password = self.driver.find_element_by_name('password')
		password.send_keys(config.TURO_PASSWORD)

		self.driver.find_element_by_id("submit").click()
# above all work. below to test each function

	def write_to_file(self, rows, out):
		print 'Writing to file', out
		with open(out, 'w') as f:
			w = csv.DictWriter(f, delimiter=',',
				fieldnames=['url_snippet', 'pickup', 'dropoff', 'cost', 'reimbursement_mileage', 'reimbursement_tolls', 'earnings']
				)
			w.writeheader()
			w.writerows(rows)
	def stop(self):
		self.driver.close()
	def get_datetime(self, el):
		date = el.find_element_by_class_name('scheduleDate').text
		time = el.find_element_by_class_name('scheduleTime').text

		date_str = datetime.datetime.now().strftime('%Y') + ' ' + date + ' ' + time

		return datetime.datetime.strptime(date_str, '%Y %b %d %I:%M %p')












	def get_trips(self, page_slug = None):
		if page_slug is None:
			self.driver.get('https://turo.com/trips')
		else:
			print 'Getting https://turo.com/trips?' + page_slug
			self.driver.get('https://turo.com/trips?' + page_slug)
		next_page = None
		last_page = self.driver.find_elements_by_class_name('paginator-link')[-1]



crawler = TuroCrawler()
su = "wps.csv"
crawler.crawl(su)


# if __name__ == '__main__':
#     outfile = 'stats.csv'
#     # if len(sys.argv) > 1:
#     #     outfile = sys.argv[1]

#     # crawler = TuroCrawler()
#     print(1)#.crawl(outfile)