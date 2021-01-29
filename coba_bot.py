from selenium import webdriver
from time import sleep
from secrets import username, password
import re


class cobaBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://passport.villamaria.qc.ca/pednet/login.asp')
        #ouvrir coba

        sleep(2)
        #waiting to load...

        usager_in = self.driver.find_element_by_xpath(
            '//*[@id="txtCodeUsager"]')
        usager_in.send_keys(username)
        #selectionner le xpath pour le usager et envoyer le "userame" contenu dans "secrets.py"

        pw_in = self.driver.find_element_by_xpath('//*[@id="txtMotDePasse"]')
        pw_in.send_keys(password)
        #selectionner le xpath pour le usager et envoyer le "password" contenu dans "secrets.py"

        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="btnConnecter"]')
        login_btn.click()
        #clique sur le login button

        sleep(2)
        #donne du temp pour le browser de loaeder

        #gets "travaux" section
        self.driver.get(
            'https://passport.villamaria.qc.ca/pednet/travaux.asp?GKfUxuyc6+0qE/eD8ALqQhX5eCMdXq9QDUYUh0Qlui6Sp4GULv+Uso4LFduO0Q2iGy7Sp5BUcOBu+Tw3dfzbKE6tYuHzzmlYJBghw+V3p3zDFNOd'
        )

        rwdata = self.driver.find_elements_by_xpath(
            '//*[@id="divPrincipal"]/form/div/table[2]/tbody/tr/td[2]/div/table[*]'
        )
        list_everything = [x.text for x in rwdata]
        #sauve le html contenu dans le xpath

        sleep(4)
        # beginning of the strip function
        regex = r"\((.*?)\)"
        subst = ", "
        string_everything = (", ".join(list_everything))
        match = re.findall(regex, string_everything)
        string_1 = subst.join(match)
        numbers_split = string_1.replace('.0', '').replace('.1', '').replace(
            '.2',
            '').replace('.3', '').replace('.4', '').replace('.5', '').replace(
                '.6', '').replace('.7', '').replace('.8', '').replace(
                    '.9', '').replace('a', '').replace('b', '').replace(
                        'c', '').replace('d', '').replace('e', '').replace(
                            'f', '').replace('g', '').replace('h', '').replace(
                                'i', '').replace('j', '').replace(
                                    'k', '').replace('l', '').replace(
                                        'm', '').replace('n', '').replace(
                                            'o', '').replace('p', '').replace(
                                                'q', ''
                                            ).replace('r', '').replace(
                                                's', ''
                                            ).replace('t', '').replace(
                                                'u', ''
                                            ).replace('v', '').replace(
                                                'w', ''
                                            ).replace('x', '').replace(
                                                'y', ''
                                            ).replace('z', '').replace(
                                                'A', ''
                                            ).replace('B', '').replace(
                                                'C', ''
                                            ).replace('D', '').replace(
                                                'E', ''
                                            ).replace('F', '').replace(
                                                'G', ''
                                            ).replace('H', '').replace(
                                                'I', ''
                                            ).replace('J', '').replace(
                                                'K', ''
                                            ).replace('L', '').replace(
                                                'M', ''
                                            ).replace('N', '').replace(
                                                'O', ''
                                            ).replace('P', '').replace(
                                                'Q', ''
                                            ).replace('R', '').replace(
                                                'S', ''
                                            ).replace('T', '').replace(
                                                'U', ''
                                            ).replace('V', '').replace(
                                                'W', ''
                                            ).replace('X', '').replace(
                                                'Y', '').replace(
                                                    'Z', '').replace(
                                                        ' ,', '').replace(
                                                            ' ', '').replace(
                                                                '%',
                                                                '').replace(
                                                                    ',', ', ')
        numbers_final = list(map(int, numbers_split.split(',')))
        average = sum(numbers_final) / len(numbers_final)
        print("ta note moyenne est: " + str(round(average, 2)) + "%")


bot = cobaBot()
bot.login()
bot.driver.quit()