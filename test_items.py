from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_see_button(browser):
    browser.get(link)
    time.sleep(30)
    b = browser.find_elements(By.CSS_SELECTOR, "form.navbar-form button.btn.btn-default")
    assert len(b)>0, 'basket button not found'