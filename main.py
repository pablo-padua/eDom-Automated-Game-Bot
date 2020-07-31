from selenium import webdriver
from time import sleep
from login import username, password, cronometro, energy, no_energy, zero
import logging
from licensing.methods import Key, Helpers

RSAPubKey = ""
auth = ""


class eDomBot:
    def __init__(self, username, password):
        result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=, \
                   key="BZGYH-JBCLV-XIXWZ-VTAFY",\
                   machine_code=Helpers.GetMachineCode())

        if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
            print("The license does not work: {0}".format(result[1]))
        else:
            #logging in
            logging.warning("Initializing bot")
            license_key = result[0]
            print("License expires: " + str(license_key.expires))
            self.username = username
            self.password = password
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get("")
            logging.warning("Started")
            sleep(1)
            self.driver.find_element_by_xpath("//a[@href='https://www./en/login']").click()
            sleep(2)
            self.driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(username)
            sleep(2)
            self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
            sleep(2)
            self.driver.find_element_by_xpath('//button[@type="submit"]').click()
            sleep(5)
            try:
                self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul[2]/div/div/div/div/div/div/div[2]/div/button").click()
                self.driver.get("")
                sleep(5)
            except:
                    try: 
                        self.driver.get("")
                        sleep(2)
                    except:
                        sleep(2)
                        pass


    def moving_on(self, cronometro, energy, no_energy):
        a=1
        logging.warning("Initiating Collectors and Energy Loop")
        while a==1:
            logging.warning("Initiated")
            #collectors
            try:
                logging.warning("Checking collectors")
                if cronometro == self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/span").get_attribute("innerHTML"):
                    logging.warning("Activating Collectors")
                    self.driver.find_element_by_id("farmimage_1").click()
                    self.driver.find_element_by_id("farmimage_2").click()
                    self.driver.find_element_by_id("farmimage_3").click()
                    self.driver.find_element_by_id("farmimage_4").click()
                    self.driver.find_element_by_id("farmimage_5").click()
                else:
                    try:
                        a=self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/span").get_attribute("innerHTML")
                        if a==cronometro:
                            logging.warning("Second click Contador - please provide this information to the dev")
                            self.driver.find_element_by_id("farmimage_1").click()
                            self.driver.find_element_by_id("farmimage_2").click()
                            self.driver.find_element_by_id("farmimage_3").click()
                            self.driver.find_element_by_id("farmimage_4").click()
                            self.driver.find_element_by_id("farmimage_5").click()
                        else:
                            logging.warning("Collectors not ready yet")
                    except:
                        pass
            except:
                logging.warning("Collectors not visible, bot not on main page")
                pass
            #energy bar
            if self.driver.find_element_by_id("energyBarT").is_displayed() == True:
                a=1
                if a==1:
                    #full energy=attack
                    if self.driver.find_element_by_id("energyBarT").get_attribute("innerHTML") == energy:
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul[2]/li[4]/a").click()
                        sleep(1)
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[1]/a[2]").click()
                        sleep(1)
                        try:
                            self.driver.find_element_by_xpath("//a[contains(text(), 'Fight for')]").click()
                            logging.warning("Found a rev")
                            sleep(1)
                        except:
                            pass
                        sleep(1)
                        try:
                            a = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[9]/div[1]/p/span[1]/em").get_attribute("innerHTML")
                            a = int(a)
                            b = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[9]/div[1]/p/span[2]/em").get_attribute("innerHTML")
                            b = int(b)
                            sleep(1)
                            #WEAPON SELECTIONNNNNNNNN
                            # if a+b<2: #if it's land combat = tanks
                            #     try:
                            #         logging.warning("Selecionando tanks")
                            #         self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/a[3]/img").click()
                            #         self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/div[4]/div/ul/li[4]/a/img").click()
                            #         sleep(1)
                            #     except:
                            #         pass

                            # elif a+b>=5: #if it's air combat = aircraft
                            #     try:
                            #         logging.warning("Selecionando aircrafts")
                            #         self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/a[3]/img").click()
                            #         sleep(2)
                            #         self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/div[4]/div/ul/li[5]/a/img").click()
                            #         sleep(1)
                            #     except:
                            #         pass
                                    
                            # elif (a+b>2 and a+b<5): #if it's urban combat = machineguns
                            #     try:
                            #         logging.warning("Selecionando machineguns")
                            #         self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/a[3]/img").click()
                            #         sleep(2)
                            #         self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/div[4]/div/ul/li[3]/a/img").click()
                            #         sleep(1)
                            #     except:
                            #         pass
                            while self.driver.find_element_by_id("energyBarT").get_attribute("innerHTML") != no_energy:
                                    sleep(3)
                                    logging.warning("time to shoot up some bitches...")
                                    #after weapon selection, we are ready to continue:
                                    self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/a[2]').click()
                                    sleep(3)
                                    if self.driver.find_element_by_id("energyBarT").get_attribute("innerHTML") == no_energy:
                                        self.driver.get("")                            
                        except:
                            self.driver.get("")
                            logging.warning("First war on the war tab ended, waiting 15 seconds...")
                            sleep(15)
                    #if energy isnt full, then auto refill
                    elif self.driver.find_element_by_id("energyBarT").get_attribute("innerHTML") != energy:
                        try:
                            logging.warning("Energy refill")
                            self.driver.find_element_by_id("energyButton").click()
                            self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/span[4]").click()
                            sleep(5)
                            a=2
                        except:
                            logging.warning("-----------YOU DONT HAVE FOOD!!!!------------")
                            sleep(2)
                            self.driver.get("")
                            sleep(3)
                            a=2
                            pass
                else:
                    pass  
            else:
                pass
        a=2
        logging.warning("Loop ended")

    def my_productions(self, zero):
        sleep(2)
        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul[2]/li[3]/a/span[1]").click()
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul[2]/li[3]/ul/li[8]/a").click()
            logging.warning("Checking my productions tab...")
        except:
            pass
        try:
            try:
                n = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/div/span").get_attribute("innerHTML")
                m = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[2]/div/span").get_attribute("innerHTML")
                if n==zero and m==zero:
                    logging.warning("Mortar and Energy are ready!")
                    try:
                        logging.warning("Initiating mortar and energy")
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]/button").click()
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/button[1]").click()
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]/button").click()
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[3]/button").click()
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/button[1]").click()
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[3]/button").click()
                        sleep(2)
                        self.driver.get("")
                    except:
                        logging.warning("erro no 1 if do my_productions linha 188")
                        self.driver.get("")
                elif n==zero and m!=zero:
                    logging.warning("Only mortar is ready!")
                    try:
                        logging.warning("Initiating mortar only")
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]/button").click()
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/button[1]").click()
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]/button").click()
                        sleep(2)
                        self.driver.get("")
                    except:
                        logging.warning("erro no 2 if(elif) do my_productions linha 200")
                        self.driver.get("")
                elif n!=zero and m==zero:
                    logging.warning("Only energy is ready!")
                    try:
                        logging.warning("Initiating energy only")
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[3]/button").click()
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/button[1]").click()
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[3]/button").click()
                        sleep(2)
                        self.driver.get("")
                    except:
                        logging.warning("erro no 3 if(elif) do my_productions linha 214")
                        self.driver.get("")
                elif n!=zero and m!=zero:
                    logging.warning("my productions not ready yet!")
                    sleep(2)
                    self.driver.get("")             
            except:
                logging.warning("Couldnt start productions (provide this error to developer).")
                sleep(1)
                self.driver.get("")
        except:
            logging.warning("nao conseguiu NEM clicar em productions.")
            sleep(1)
            self.driver.get("")
