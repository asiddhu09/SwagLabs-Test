import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = (
    webdriver.Chrome()
)  # to create an instance of a browser so we dont need to download the driver

# login variables
url = "https://www.saucedemo.com/v1/"
username = "standard_user"
passwrd = "secret_sauce"

# checkout variables
chkoutfname = "ABC"
chkoutlname = "XYZ"
postal_code = "12345"

driver.maximize_window()
driver.get(url)

driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(passwrd)

driver.find_element(By.ID, "login-button").click()

# to verify that the correct page is loaded

current_url = driver.current_url

# Word to check
word = "inventory"

# Check if the word is in the URL
if word in current_url:
    print(f"The word '{word}' found, User Logged in Successfully")
else:
    print(f"The word '{word}'not found, User Login Failed")

# more Actions
button = driver.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()
# time.sleep(2)

cart_icon = driver.find_element(
    By.XPATH,
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/a[1]/*[name()='svg'][1]/*[name()='path'][1]",
)
cart_icon.click()


# below code if for verifying that the item is added to the cart after clicking the button
item_number = driver.find_element(
    By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]"
)

number = item_number.text

if number.isdigit() and int(number) > 0:
    print(f"Number of item added is {number}")
else:
    print(f"No item even after clicking the Add to Cart button")


# checkOUT process
driver.find_element(
    By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[2]/a[2]"
).click()


current_url = driver.current_url

# Word to check
word = "checkout"

# Check if the word is in the URL
if word in current_url:
    print(f"The word '{word}' found, Checkout page loaded succesfully")
else:
    print(f"The word '{word}'not found, Checkout page not loaded")

checkout_fname = driver.find_element(By.ID, "first-name").send_keys(chkoutfname)
checkout_lname = driver.find_element(By.ID, "last-name").send_keys(chkoutlname)
postalcode = driver.find_element(By.ID, "postal-code").send_keys(postal_code)

driver.find_element(
    By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[2]/input[1]"
).click()

check_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]")

# Expected text to verify
expected_text = "Checkout: Overview"

# Get the text from the element
actual_text = check_element.text

# Verify the text
if actual_text == expected_text:
    print(
        f"Successfully visited the last page of the checkout process and the number of item in the cart is {number}"
    )
else:
    print("Failed to load the page")


driver.find_element(
    By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[8]/a[2]"
).click()

current_url = driver.current_url

word = "complete"

if word in current_url:
    print("Your Order is completed : THANK YOU!!")
else:
    print("Failed to place your order")

time.sleep(2)

driver.quit()
