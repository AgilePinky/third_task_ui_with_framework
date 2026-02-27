from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages_dir.base_page import BasePage
from elements_dir.label import Label
from elements_dir.button import Button

class HoverPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@id='content']//h3")
    PROFILE_IMG_LOC_STR = "(//div[contains(@class, 'figure')]//img)[{}]"
    PROFILE_NAME_LOC_STR = "(//div[contains(@class, 'figure')]//div[contains(@class, 'figcaption')]//h5)[{}]"
    PROFILE_URL_LOC_STR = "(//div[contains(@class, 'figure')]//div[contains(@class, 'figcaption')]//a)[{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.profile_num = None

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.profile_img_element = None
        self.profile_name_element = None
        self.profile_url_element = None


    def hover_element(self, profile_num):
        self.profile_num = profile_num
        self.profile_img_element = Button(self.browser,
                                        self.PROFILE_IMG_LOC_STR.format(self.profile_num),
                                        "Profile img {}".format(self.profile_num))

        ActionChains(self.browser.driver)\
        .move_to_element(self.profile_img_element.wait_for_visible())\
        .perform()

        self.profile_name_element = Label(self.browser,
                                        self.PROFILE_NAME_LOC_STR.format(str(self.profile_num)),
                                        "Profile name {}".format(self.profile_num))
        self.profile_name_element.wait_for_visible()

        self.profile_url_element = Button(self.browser,
                                        self.PROFILE_URL_LOC_STR.format(str(self.profile_num)),
                                        "Profile url {}".format(self.profile_num))







