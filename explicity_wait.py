from handy_wrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *


class ExplicitWaitType:

    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)


    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            self.driver.implicitly_wait(0)
            byType = self.hw.getByType(locatorType)
            print(f"Espera maxima :: {timeout} :: hasta que el elemento sea visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,])
            element = wait.until(expected_conditions.visibility_of_element_located((byType, locator)))
            print("Elemento aparece en la pagina web")
        except:
            print("Elemento no aparece en la pagina web")

        self.driver.implicitly_wait(2)
        return element