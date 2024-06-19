import time, sys
import keysus
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

user_name = keysus.user
pass_word = keysus.passw


class Browser:
    browser, service = None, None

   
    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        try:
            self.browser.get(url)
        except WebDriverException as e:
            if "net::ERR_INTERNET_DISCONNECTED" in str(e):
                print("Internet is disconnected. Please check your connection and try again.")
                sys.exit(1)
            else:
                print(f"An error occurred while trying to open the page: {e}")
                sys.exit(1)

    def add_input(
        self, by: By, value: str, text: str
    ):  # adds input into the text fields
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):  # button clicker
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_wifi(self, username: str, password: str):
        try:
            # Check if there's a login button present indicating the user hasn't logged in
            login_button_present = True 
            try:
                self.browser.find_element(By.TAG_NAME, "button")
            except NoSuchElementException:
                login_button_present = False

            if not login_button_present:
                print ("Already logged in")
                return
            
            # Find the right boxes for the username and password credentials
            username_field = self.browser.find_element(By.XPATH, "(//input[@class='form-control'])[1]")
            password_field = self.browser.find_element(By.XPATH, "(//input[@class='form-control'])[2]")

            # Paste the username and password
            username_field.send_keys(username)
            time.sleep(1)
            password_field.send_keys(password)
            time.sleep(1)

            # Click the login button 
            self.click_button(By.TAG_NAME, "button")

            # Wait to make suere the login process is completed 
            time.sleep(6)

            # Check to see if the log in button is still present 
            try:
                self.browser.find_element(By.TAG_NAME, "button")
                print("Login Failed ❌ . Try checking your credentials")
            except NoSuchElementException:
                print("Login successful ✅")
        
        except NoSuchElementException as e:
            print(f"An element wasn't found: {e}")
        except WebDriverException as e:
            print(f"A browser error has occured: {e}")
        finally: # Didn't even know this  existed 
            # Add a pause to allow the user to see the message before terminal dies
            time.sleep(5)
            # Close the bomboclat browser 
            self.browser.quit()
            

if __name__ == "__main__":
    browser = Browser(
        "C:/Users/HP/.cache/selenium/chromedriver/win64/124.0.6367.201/chromedriver.exe"
    )

    browser.open_page(
        "http://wifi.abu.ng/login?dst=http%3A%2F%2Fwww.msftconnecttest.com%2Fredirect"
    )
    time.sleep(5)

    browser.login_wifi(user_name, pass_word)


