from selenium import webdriver

chrome_browser = webdriver.Chrome("./chromedriver")
chrome_browser.maximize_window()
chrome_browser.get(
    "https://www.seleniumeasy.com/test/basic-first-form-demo.html")

show_message_button = chrome_browser.find_element_by_class_name("btn-default")
# print(show_message_button.get_attribute("innerHTML"))

assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_button = chrome_browser.find_elements_by_css_selector("#get-input > .btn")
user_message.clear()
user_message.send_keys("I AM TESTING THIS")

show_message_button.click()

output_message = chrome_browser.find_element_by_id("display")

assert "I AM TESTING THIS" in output_message.text
