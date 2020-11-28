from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

login_url = "https://www.chess.com/login_and_go?returnUrl=https%3A%2F%2Fwww.chess.com%2F"
username = "test1564"
password = "Test1564"

script = "window.frames['mce_0_ifr'].contentDocument.getElementById(\"tinymce\").textContent=\"Test message sadfasd\""

driver = webdriver.Chrome(ChromeDriverManager().install())

def site_login():
	driver.get(login_url)
	driver.find_element_by_id("username").send_keys(username)
	driver.find_element_by_id("password").send_keys(password)
	driver.find_element_by_id("login").click()


def goToMessagePage(user):
	driver.get("https://www.chess.com/messages/for-inet-purchase")

def setMessage(message):
	driver.implicitly_wait(30)

	frame = driver.switch_to.frame(driver.find_element_by_id("mce_0_ifr"))
	element = driver.find_element_by_id("tinymce")
	driver.execute_script("arguments[0].textContent = 'Test message for example'", element)

	driver.switch_to.default_content()

def sendMessage():
	driver.implicitly_wait(10)
	driver.switch_to.default_content()
	driver.find_element_by_id("message-submit").click()
	driver.find_element_by_id("message-submit").click()


site_login()
goToMessagePage("for-inet-purchase")
setMessage("test")
sendMessage()
