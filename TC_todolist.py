import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webbrowser import get


driver=webdriver.Chrome()
# 3 below commands are used for config chrome option when we need to take full-screenshot.
# options = webdriver.ChromeOptions()
# options.headless = True
# driver=webdriver.Chrome(options=options)

base_url = "https://todo-list-login.firebaseapp.com/"
main_page = driver.current_window_handle
#####KEYWORDS#####
def login_by_git():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="btn btn-social btn-github"]'))).click()
    for handle in driver.window_handles:
        if handle != main_page:
                login_page = handle
    driver.switch_to.window(login_page)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "login_field"))).send_keys("myvng16870@gmail.com")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("khuyenlv@vng.com.vn")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="btn btn-primary btn-block js-sign-in-button"]'))).click()
    driver.switch_to.window(main_page)

def sign_out():
    driver.find_element_by_css_selector('[class="btn btn-default"]').click()

def take_fullscreenshot(file_name:str):
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height'))
    driver.find_element_by_tag_name('body').screenshot('%s.png' % file_name)

####TC01_Add_and_delete_list####
#Step 1: Access page and login by git account
driver.get(base_url)
login_by_git()

#Step 2: Create the 1st list
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html[@class='ng-scope']/body[@class='bg-primary ']/ng-view[@class='ng-scope']\
    /div[@class='ng-scope']/div[@class='row'][1]/div[@class='col-xs-offset-2 col-xs-4']/input[@class='form-control ng-pristine ng-untouched ng-valid ng-empty']"))).send_keys("List 1")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html[@class='ng-scope']/body[@class='bg-primary ']/ng-view[@class='ng-scope']\
    /div[@class='ng-scope']/div[@class='row'][1]/div[@class='col-xs-4']/button[@class='btn btn-success btn-block glyphicon glyphicon-plus task-btn']"))).click()

#Create the 2nd-10th list
time.sleep(1)
for i in range(2,11):
    driver.find_element_by_xpath("/html[@class='ng-scope']/body[@class='bg-primary ']/ng-view[@class='ng-scope']/div[@class='ng-scope']/div[@class='row'][1]\
        /div[@class='col-xs-offset-2 col-xs-4']/input[@class='form-control ng-valid ng-dirty ng-touched ng-empty']").send_keys("List ", i)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html[@class='ng-scope']/body[@class='bg-primary ']/ng-view[@class='ng-scope']\
        /div[@class='ng-scope']/div[@class='row'][1]/div[@class='col-xs-4']/button[@class='btn btn-success btn-block glyphicon glyphicon-plus task-btn']"))).click()
    time.sleep(1)
# take_fullscreenshot("add_10lists")  ##It only be opened when running chrome with headless option

#Step 3: Sign out
sign_out()
time.sleep(3)

#Step 4: Sign in again
driver.find_element_by_css_selector('[class="btn btn-social btn-github"]').click()
#Step 5: Delete list from 5-10th
for i in range (6):
    i_str=str(i)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html[@class='ng-scope']/body[@class='bg-primary ']/ng-view[@class='ng-scope']/div[@class='ng-scope']\
        /div[@class='row'][2]/div[@class=' col-xs-offset-2 col-xs-12']/ul[@class='list-group']/li[@class='disney1 ng-scope'][5]/div[@class='row']/div[@class='col-xs-1']\
            /button[@class='btn btn-danger btn-block glyphicon glyphicon-remove']"))).click()
    time.sleep(1)
#take_fullscreenshot("delete_6lists")  ##The same explain with above

#Step 6: Sign out and close browser
sign_out()
time.sleep(3)
driver.close()