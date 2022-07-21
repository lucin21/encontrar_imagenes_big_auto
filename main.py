from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from explicity_wait import ExplicitWaitType
from selenium.webdriver.common.keys import Keys




class UsingWrappers1():

    def test(self):
        image_default = "https://tienda.bigauto.solutionslion.com/img/p/mx-default-home_default.jpg"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()


        driver.implicitly_wait(10)
        wait = ExplicitWaitType(driver)
        n = 1
        for _ in range(625):
            baseUrl = f"https://tienda.bigauto.solutionslion.com/mx/2704-empaques-de-motor?page={n}"
            driver.get(baseUrl)
            n += 1
            element1 = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[1]/div/div[1]/div/a/img[1]', locatorType='xpath')
            element1.get_attribute("attribute src")
            print(element1.get_attribute("src"))
            if element1.get_attribute("src") == image_default:
                element1_part = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[1]/div/div[2]/div[2]/a/div/b', locatorType='xpath')
                print(element1_part.text)
                with open("balata_disco_results.txt", "a") as archivo:
                    archivo.write(f"{element1_part.text}\n")

            element2 = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[2]/div/div[1]/div/a/img[1]', locatorType='xpath')
            element2.get_attribute("attribute src")
            print(element2.get_attribute("src"))
            if element2.get_attribute("src") == image_default:
                element2_part = wait.waitForElement(
                    locator='//*[@id="js-product-list"]/div/article[2]/div/div[2]/div[2]/a/div/b', locatorType='xpath')
                with open("balata_disco_results.txt", "a") as archivo:
                    archivo.write(f"{element2_part.text}\n")

            element3 = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[3]/div/div[1]/div/a/img[1]',locatorType='xpath')
            element3.get_attribute("attribute src")
            print(element3.get_attribute("src"))
            if element3.get_attribute("src") == image_default:
                element3_part = wait.waitForElement(
                    locator='//*[@id="js-product-list"]/div/article[3]/div/div[2]/div[2]/a/div/b', locatorType='xpath')
                with open("balata_disco_results.txt", "a") as archivo:
                    archivo.write(f"{element3_part.text}\n")

            element4 = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[4]/div/div[1]/div/a/img[1]', locatorType='xpath')
            element4.get_attribute("attribute src")
            print(element4.get_attribute("src"))
            if element4.get_attribute("src") == image_default:
                element4_part = wait.waitForElement(
                    locator='//*[@id="js-product-list"]/div/article[4]/div/div[2]/div[2]/a/div/b', locatorType='xpath')
                with open("balata_disco_results.txt", "a") as archivo:
                    archivo.write(f"{element4_part.text}\n")

            element5 = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[5]/div/div[1]/div/a/img[1]',locatorType='xpath')
            element5.get_attribute("attribute src")
            print(element5.get_attribute("src"))
            if element5.get_attribute("src") == image_default:
                element5_part = wait.waitForElement(
                    locator='//*[@id="js-product-list"]/div/article[5]/div/div[2]/div[2]/a/div/b', locatorType='xpath')
                with open("balata_disco_results.txt", "a") as archivo:
                    archivo.write(f"{element5_part.text}\n")

            element6 = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[6]/div/div[1]/div/a/img[1]',locatorType='xpath')
            element6.get_attribute("attribute src")
            print(element6.get_attribute("src"))
            if element6.get_attribute("src") == image_default:
                element6_part = wait.waitForElement(
                    locator='//*[@id="js-product-list"]/div/article[6]/div/div[2]/div[2]/a/div/b', locatorType='xpath')
                with open("balata_disco_results.txt", "a") as archivo:
                    archivo.write(f"{element6_part.text}\n")

            element7 = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[7]/div/div[1]/div/a/img[1]',
                                           locatorType='xpath')
            element7.get_attribute("attribute src")
            print(element7.get_attribute("src"))
            if element7.get_attribute("src") == image_default:
                element7_part = wait.waitForElement(
                    locator='//*[@id="js-product-list"]/div/article[7]/div/div[2]/div[2]/a/div/b', locatorType='xpath')
                with open("balata_disco_results.txt", "a") as archivo:
                    archivo.write(f"{element7_part.text}\n")

            element8 = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[8]/div/div[1]/div/a/img[1]',
                                           locatorType='xpath')
            element8.get_attribute("attribute src")
            print(element8.get_attribute("src"))
            if element8.get_attribute("src") == image_default:
                element8_part = wait.waitForElement(
                    locator='//*[@id="js-product-list"]/div/article[8]/div/div[2]/div[2]/a/div/b', locatorType='xpath')
                with open("balata_disco_results.txt", "a") as archivo:
                    archivo.write(f"{element8_part.text}\n")

            element9 = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[9]/div/div[1]/div/a/img[1]',
                                           locatorType='xpath')
            element9.get_attribute("attribute src")
            print(element9.get_attribute("src"))
            if element9.get_attribute("src") == image_default:
                element9_part = wait.waitForElement(
                    locator='//*[@id="js-product-list"]/div/article[9]/div/div[2]/div[2]/a/div/b', locatorType='xpath')
                with open("balata_disco_results.txt", "a") as archivo:
                    archivo.write(f"{element9_part.text}\n")

            element10 = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[10]/div/div[1]/div/a/img[1]',
                                           locatorType='xpath')
            element10.get_attribute("attribute src")
            print(element10.get_attribute("src"))
            if element10.get_attribute("src") == image_default:
                element10_part = wait.waitForElement(
                    locator='//*[@id="js-product-list"]/div/article[10]/div/div[2]/div[2]/a/div/b', locatorType='xpath')
                with open("balata_disco_results.txt", "a") as archivo:
                    archivo.write(f"{element10_part.text}\n")

            element11 = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[11]/div/div[1]/div/a/img[1]',
                                           locatorType='xpath')
            element11.get_attribute("attribute src")
            print(element11.get_attribute("src"))
            if element11.get_attribute("src") == image_default:
                element11_part = wait.waitForElement(
                    locator='//*[@id="js-product-list"]/div/article[11]/div/div[2]/div[2]/a/div/b', locatorType='xpath')
                with open("balata_disco_results.txt", "a") as archivo:
                    archivo.write(f"{element11_part.text}\n")

            element12 = wait.waitForElement(locator='//*[@id="js-product-list"]/div/article[12]/div/div[1]/div/a/img[1]',
                                           locatorType='xpath')
            element12.get_attribute("attribute src")
            print(element12.get_attribute("src"))
            if element12.get_attribute("src") == image_default:
                element12_part = wait.waitForElement(
                    locator='//*[@id="js-product-list"]/div/article[12]/div/div[2]/div[2]/a/div/b', locatorType='xpath')
                with open("balata_disco_results.txt", "a") as archivo:
                    archivo.write(f"{element12_part.text}\n")


            time.sleep(5)




        driver.quit()

ff = UsingWrappers1()
ff.test()