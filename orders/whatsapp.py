from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from urllib.parse import quote


def send_whatsapp_message(message):

    owner_number = "919420629380"

    encoded_message = quote(message)

    options = webdriver.ChromeOptions()

    options.add_argument(
        r"--user-data-dir=C:\Users\Ateet\whatsapp_profile"
    )

    driver = webdriver.Chrome(
        options=options
    )

    try:

        url = (
            f"https://wa.me/{owner_number}?text={encoded_message}"
        )

        driver.get(url)

        print("Opening WhatsApp...")

        time.sleep(10)

        try:

            continue_btn = driver.find_element(
                By.XPATH,
                '//a[contains(@href,"web.whatsapp.com")]'
            )

            continue_btn.click()

            print("Continue to WhatsApp clicked")

            time.sleep(10)

        except:

            print("Continue button not found")

        print("Waiting for chat to load...")

        time.sleep(8)

        actions = ActionChains(driver)

        actions.send_keys(Keys.ENTER)

        actions.perform()

        print("Message Sent Successfully")

        time.sleep(5)

    except Exception as e:

        print("Error:", e)

    finally:

        driver.quit()