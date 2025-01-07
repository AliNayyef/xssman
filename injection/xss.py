from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


def xss(target_url, input_id, button_value, xss_path):
    try:
        with open(xss_path, "r", encoding="utf-8") as file:
            xss_payloads = file.readlines()
    except Exception as e:
        print(f"Error reading file: {e}")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(target_url)
    time.sleep(1)

    # iframe = driver.find_element(By.TAG_NAME, "iframe") # this if we have I frame
    # driver.switch_to.frame(iframe)

    for payload in xss_payloads:
        inputs = driver.find_elements(By.ID, input_id)
        print(f"Found {len(inputs)} input fields.")

        buttons = driver.find_elements(By.XPATH, f"//input[@value='{button_value}']")
        print(f"Found {len(buttons)} button fields.")

        print(f"Testing payload: {payload}")
        for input_field in inputs:
            try:
                input_field.clear()
                input_field.send_keys(payload)
            except Exception as e:
                print(f"Error inputting payload in field: {e}")
        try:
            for button in buttons:
                button.click()
                time.sleep(1)
        except Exception as e:
            print(f"Error submitting form: {e}")

        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert triggered with payload: '{payload}', alert text: {alert_text}")
            alert.accept()
            break

        except:
            print("no alert found")
    time.sleep(5)
