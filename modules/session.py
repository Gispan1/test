from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class amazon:
    def __init__(self):
        #self.mainWindow = webdriver.Chrome()
        self.mainWindow = webdriver.Firefox()
        self.search_element_id = 'twotabsearchtextbox'
        self.element_results_class = 'sx-price-whole'
        self.cart_button_id = 'add-to-cart-button'
        self.no_thanks_popup_id = 'siNoCoverage-announce'
        self.cart_total_xpath = '//*[@id="hlb-subcart"]/div[1]/span/span[2]'
        self.add_also_bought_class_name = 'huc-upsell-big-face-box-inner'
        self.go_to_cart_id = 'nav-cart'
        self.proceed_to_checkout_name = 'proceedToCheckout'
        self.create_new_account_id = 'createAccountSubmit'
        self.new_user_name_id = 'ap_customer_name'
        self.new_user_email_id = 'ap_email'
        self.new_user_password_id = 'ap_password'
        self.new_user_password_check_id = 'ap_password_check'

    def open_amzon_site(self,site_url="https://www.amazon.com/"):
        self.mainWindow.get(site_url)

    def search_items(self, query):
        search_element = self.mainWindow.find_element_by_id(self.search_element_id)
        search_element.send_keys(query)
        search_element.send_keys(Keys.RETURN)

    def add_items_to_cart(self,max_amount=500):
        search_result_item = self.mainWindow.find_element_by_class_name(self.element_results_class)
        search_result_item.click()
        self.click_add_to_cart()
        self.dismiss_add_to_order_popup()
        if self.check_cart_balance(max_amount) == 'below_max_amount':
            amount_too_small =True
            while amount_too_small:
                self.click_add_another_to_cart()
                self.dismiss_add_to_order_popup()
                if self.check_cart_balance(max_amount) == 'above_max_amount':
                    amount_too_small = False

    def click_add_to_cart(self):
        self.mainWindow.find_element_by_id( self.cart_button_id).click()

    def dismiss_add_to_order_popup(self):
        try:
            time.sleep(2)
            self.mainWindow.find_element_by_id(self.no_thanks_popup_id).click()
        except:
            pass

    def click_add_another_to_cart(self):
        self.mainWindow.find_element_by_class_name(self.add_also_bought_class_name).click()
        self.click_add_to_cart()

    def proceed_to_checkout(self):
        self.mainWindow.find_element_by_id(self.go_to_cart_id).click()
        self.mainWindow.find_element_by_name(self.proceed_to_checkout_name).click()
        self.mainWindow.find_element_by_id(self.create_new_account_id).click()

    def check_cart_balance(self,max_amount):
        time.sleep(1)
        total_amount = self.mainWindow.find_element_by_xpath(self.cart_total_xpath).text
        total = total_amount.split('$') #remove currency sign
        if float(total[1]) < float(max_amount):
            return 'below_max_amount'
        else:
            return 'above_max_amount'

    def fill_user_details(self,user_name,user_email,user_password):
        self.mainWindow.find_element_by_id(self.new_user_name_id).send_keys(user_name)
        self.mainWindow.find_element_by_id(self.new_user_email_id).send_keys(user_email)
        self.mainWindow.find_element_by_id(self.new_user_password_id).send_keys(user_password)
        self.mainWindow.find_element_by_id(self.new_user_password_check_id).send_keys(user_password)

    def end_session(self):
        self.mainWindow.quit()

class perimeterx:
    def __init__(self):
        self.mainWindow = webdriver.Firefox()
        self.tempWindow = webdriver.Firefox()

    def open_perimeterx_site(self, site_url="http://www.perimeterx.com/"):
        self.mainWindow.get(site_url)

    def get_all_pages(self):
        elems = self.mainWindow.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            print elem.get_attribute("href")
            self.print_page_content(elem.get_attribute("href"))

    def print_page_content(self,page_url):
        self.tempWindow.get(page_url)
        content= self.tempWindow.find_element_by_xpath('/html/body').text
        print content

    def end_session(self):
        self.mainWindow.quit()
        self.tempWindow.quit()
