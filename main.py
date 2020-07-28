from selenium import webdriver
from time import sleep
from login import username, password, cronometro, energy, no_energy, zero
import logging




class gameBot:
    def __init__(self, username, password):
        #logging in
        logging.warning("Initializing bot")
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("website name")
        logging.warning("Started")
        sleep(1)
        self.driver.find_element_by_xpath("//a[@href='websitename/login']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(username)
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        sleep(2)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)
        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul[2]/div/div/div/div/div/div/div[2]/div/button").click()
            self.driver.get("websitename")
            sleep(5)
        except:
                try: 
                    self.driver.get("websitename")
                    sleep(2)
                except:
                    sleep(2)
                    pass


    def moving_on(self, cronometro, energy, no_energy):
        a=1
        logging.warning("Moving on")
        while a==1:
            logging.warning("Loop")
            #collectors
            try:
                logging.warning("vendo se valor tá 00 no contador")
                if cronometro == self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/span").get_attribute("innerHTML"): #xpath=cronometro zero
                    logging.warning("Ativando Contador")
                    self.driver.find_element_by_id("farmimage_1").click()
                    self.driver.find_element_by_id("farmimage_2").click()
                    self.driver.find_element_by_id("farmimage_3").click()
                    self.driver.find_element_by_id("farmimage_4").click()
                    self.driver.find_element_by_id("farmimage_5").click()
                else:
                    try:
                        a=self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/span").get_attribute("innerHTML")
                        if a==cronometro:
                            logging.warning("second click Contador")
                            self.driver.find_element_by_id("farmimage_1").click()
                            self.driver.find_element_by_id("farmimage_2").click()
                            self.driver.find_element_by_id("farmimage_3").click()
                            self.driver.find_element_by_id("farmimage_4").click()
                            self.driver.find_element_by_id("farmimage_5").click()
                        else:
                            logging.warning("nao tem como NTC")
                    except:
                        pass
            except:
                logging.warning("else from first 'if' on collectors")
                pass
            #energy bar
            if self.driver.find_element_by_id("energyBarT").is_displayed() == True:
                myElem2 = self.driver.find_element_by_id("energyBarT").get_attribute("innerHTML")
                a=1
                if a==1:
                    #full energy=attack
                    if self.driver.find_element_by_id("energyBarT").get_attribute("innerHTML") == energy:
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul[2]/li[4]/a").click() #Battles
                        sleep(1)
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[1]/a[2]").click() #First war
                        sleep(1)
                        try:
                            self.driver.find_element_by_xpath("//a[contains(text(), 'Fight for')]").click() #if there's a rev:
                            logging.warning("Encontramos uma rev")
                            sleep(1)
                        except:
                            pass
                        sleep(1)
                        try:
                            a = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[9]/div[1]/p/span[1]/em").get_attribute("innerHTML") #attacker score
                            a = int(a)
                            b = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[9]/div[1]/p/span[2]/em").get_attribute("innerHTML") #defender score
                            b = int(b)
                            sleep(1)
                            #WEAPON SELECTIONNNNNNNNN
                            if a+b<2: #if it's land combat = tanks
                                try:
                                    logging.warning("Selecionando tanks")
                                    self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/a[3]/img").click() #click to select which weapon to use = hand icon
                                    self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/div[4]/div/ul/li[4]/a/img").click() #selects q5 tanks
                                    sleep(1)
                                except:
                                    pass

                            elif a+b>=5: #if it's air combat = aircraft
                                try:
                                    logging.warning("Selecionando aircrafts")
                                    self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/a[3]/img").click() #click to select which weapon to use = hand icon
                                    sleep(2)
                                    self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/div[4]/div/ul/li[5]/a/img").click() #selects q5 air
                                    sleep(1)
                                except:
                                    pass
                                    
                            elif (a+b>2 and a+b<5): #if it's urban combat = machineguns
                                try:
                                    logging.warning("Selecionando machineguns")
                                    self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/a[3]/img").click() #click to select which weapon to use = hand icon
                                    sleep(2)
                                    self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/div[4]/div/ul/li[3]/a/img").click() #selects q5 machineguns
                                    sleep(1)
                                except:
                                    pass
                            while self.driver.find_element_by_id("energyBarT").get_attribute("innerHTML") != no_energy:
                                    sleep(3)
                                    logging.warning("hora de meter bala... tra tra tra")
                                    #after weapon selection, we are ready to continue:
                                    self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[20]/div/a[2]').click() #hits
                                    sleep(3)
                                    if self.driver.find_element_by_id("energyBarT").get_attribute("innerHTML") == no_energy: #no more hits available
                                        self.driver.get("websitename")                            
                        except:
                            self.driver.get("websitename")
                            logging.warning("A primeira guerra acabou, esperando 15 segundos...")
                            sleep(15)
                    #if energy isnt full, then auto refill
                    elif self.driver.find_element_by_id("energyBarT").get_attribute("innerHTML") != energy:
                        try:
                            logging.warning("Energy refill")
                            self.driver.find_element_by_id("energyButton").click()
                            self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/span[4]").click() #day button
                            sleep(5)
                            a=2
                        except:
                            logging.warning("NAO REABASTECEUUUUU")
                            sleep(5)
                            self.driver.get("websitename")
                            a=2
                            pass
                else:
                    pass  
            else:
                pass
        a=2
        logging.warning("moving_on finished.------------")

    def my_productions(self, zero):
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul[2]/li[3]/a/span[1]").click() #my buildings tab
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul[2]/li[3]/ul/li[8]/a").click() #my productions tab
        logging.warning("checking my productions tab...")
        try:
            try:
                n = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/div/span").get_attribute("innerHTML") #first counter
                m = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[2]/div/span").get_attribute("innerHTML") #second counter
                if n==zero and m==zero:
                    logging.warning("N e M igual a zero!")
                    try:
                        logging.warning("Iniciando mortar e energy")
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]/button").click()#get reward button click
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/button[1]").click() #confirm
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]/button").click() #start production button click
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[3]/button").click()#get reward button click
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/button[1]").click() #confirm
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[3]/button").click() #start production button click
                        sleep(2)
                        self.driver.get("websitename")
                    except:
                        logging.warning("erro no 1 if do my_productions linha 188")
                        self.driver.get("websitename")
                elif n==zero and m!=zero:
                    logging.warning("N igual a zero!")
                    try:
                        logging.warning("Iniciando mortar apenas")
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]/button").click()#get reward button click
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/button[1]").click() #confirm
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[3]/button").click() #start production button click
                        sleep(2)
                        self.driver.get("websitename")
                    except:
                        logging.warning("erro no 2 if(elif) do my_productions linha 200")
                        self.driver.get("websitename")
                elif n!=zero and m==zero:
                    logging.warning("M igual a zero!")
                    try:
                        logging.warning("Iniciando energy apenas")
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[3]/button").click()#get reward button click
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/button[1]").click() #confirm
                        sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[3]/button").click() #start production button click
                        sleep(2)
                        self.driver.get("websitename")
                    except:
                        logging.warning("erro no 3 if(elif) do my_productions linha 214")
                        self.driver.get("websitename")
                elif n!=zero and m!=zero:
                    logging.warning("my productions ainda nao está pronto!")
                    sleep(2)
                    self.driver.get("websitename")             
            except:
                logging.warning("nao conseguiu startar productions.")
                sleep(1)
                self.driver.get("websitename")
        except:
            logging.warning("nao conseguiu NEM clicar em productions.")
            sleep(1)
            self.driver.get("websitename")


bot=gameBot(username, password)
while True:
    bot.moving_on(cronometro, energy, no_energy)
    bot.my_productions(zero)
    for x in range(1, 1320):
        logging.warning("Loopin for the " + str(x) + "° time.")
        bot.moving_on(cronometro, energy, no_energy)
