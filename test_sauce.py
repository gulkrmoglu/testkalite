from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driveri bekleten yapı
from selenium.webdriver.support import expected_conditions as ec # beklenen koşullar 
from selenium.webdriver.common.action_chains import ActionChains # bir dizi zincir misali aksşyonlar
import pytest

class Test_Sauce: 
    def precondition(self):
        driver =webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")  
        return driver
    def setup_method(self): #pytest tarafından tanımlanan bir metod her test öncesi otomaik olarak çalıştırılır.
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")  

    def teardown_method(self): #her test bitiminde çalışacak fonksiyon
        self.driver.quit()

    def test_invalid_login(self): 
        driver = self.precondition()
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
    @pytest.mark.parametrize("username,password",[("1","1"),("abc","123"),("deneme","secret_sauce")])
    def test_invalid_login(self,username,password): 
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))

        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        #print(errorMessage.text)
        testResult = errorMessage.text == "ERROR!!! Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"


# Case 1     
# -Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.

    def test_null_value(self):
        driver = self.precondition()
        loginButton = driver.find_element(By.ID,"login-button")
    @pytest.mark.parametrize("username,password",[("","")])
    def test_null_value(self,username,password):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        sleep(2)
        expectedMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Username is required"
        print(f"Epic sadface: Username is required uyarı mesajı gösterilmiştir = {testResult}")
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Username is required"


#Case 2
#-Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    def test_null_password(self):
        driver = self.precondition()
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("standard_user")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
    @pytest.mark.parametrize("username,password",[("standart_user","")])
    def test_null_password(self, username, password):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))

        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        sleep(2)
        expectedMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Password is required"
        print(f"Epic sadface: Password is required uyarı mesajı gösterilmiştir = {testResult}")
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Password is required"

#case 3
#Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def test_user_locked(self):
        driver = self.precondition()
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("locked_out_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginButton = driver.find_element(By.ID,"login-button")
    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_user_locked(self,username,password):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))

        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        expectedMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Epic sadface: Sorry, this user has been locked out. uyarı mesajı gösterilmiştir = {testResult}")
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

#case 4
#-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def test_products_list(self):
        driver = self.precondition()
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginButton = driver.find_element(By.ID,"login-button")
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))

        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        sleep(2)
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)
        productList = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Ürün sayısı {len(productList)} adettir.")
        sleep(3)

        baslik = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='header_container']/div[1]/div[2]/div")))

        assert baslik.text == "Swag Labs"
