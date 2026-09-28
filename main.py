import json
import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# LOAD BIRTHDAYS


def load_birthdays():

    with open("birthdays.json", "r") as file:
        return json.load(file)



# GET TODAY'S BIRTHDAYS


def get_todays_birthdays(birthdays):

    today = datetime.now()

    print("Today:", today)
    print("Date:", today.day)
    print("Month:", today.month)
    print("Year:", today.year)

    today_birthdays = []

    for person in birthdays:

        if (
            person["birth_month"] == today.month
            and person["birth_date"] == today.day
        ):
            today_birthdays.append(person)

    return today_birthdays



# CREATE MESSAGE


def create_message(name):
    return "Happy Birthday 🎉🥳🎂"



# LOAD SENT BIRTHDAYS


def load_sent_birthdays():

    if not os.path.exists("sent_birthdays.json"):
        return {}

    with open("sent_birthdays.json", "r") as file:
        return json.load(file)



# SAVE SENT BIRTHDAYS


def save_sent_birthdays(sent_birthdays):

    with open("sent_birthdays.json", "w") as file:

        json.dump(
            sent_birthdays,
            file,
            indent=4
        )



# CHECK IF ALREADY SENT


def already_sent(sent_birthdays, name):

    today = datetime.now().strftime("%Y-%m-%d")

    if today in sent_birthdays:

        if name in sent_birthdays[today]:
            return True

    return False



# MARK AS SENT


def mark_as_sent(sent_birthdays, name):

    today = datetime.now().strftime("%Y-%m-%d")

    if today not in sent_birthdays:

        sent_birthdays[today] = []

    if name not in sent_birthdays[today]:

        sent_birthdays[today].append(name)

    save_sent_birthdays(sent_birthdays)



# START BROWSER


def start_browser():

    profile_path = os.path.abspath("chrome_profile")

    options = webdriver.ChromeOptions()

    options.add_argument(
        f"--user-data-dir={profile_path}"
    )

    driver = webdriver.Chrome(
        options=options
    )

    driver.get(
        "https://web.whatsapp.com/"
    )

    print("WhatsApp Web opened.")

    print(
        "If QR code appears, scan it once."
    )

    # Wait for WhatsApp Web
    time.sleep(5)

    return driver



# SEARCH CONTACT


def search_contact(driver, name):

    wait = WebDriverWait(
        driver,
        30
    )

    selectors = [

        (
            By.XPATH,
            '//div[@contenteditable="true"][@role="textbox"]'
        ),

        (
            By.XPATH,
            '//div[@contenteditable="true"]'
        ),

        (
            By.XPATH,
            '//input[@type="text"]'
        )
    ]

    search_box = None

    # Find search box
    for by, selector in selectors:

        try:

            search_box = wait.until(
                EC.presence_of_element_located(
                    (by, selector)
                )
            )

            print(
                "Search box found!"
            )

            break

        except:

            continue

    if search_box is None:

        print(
            f"Search box not found for {name}"
        )

        return False

    try:

        search_box.click()

   
        # IMPORTANT:
        # Clear old search text 
   

        search_box.send_keys(
            Keys.COMMAND,
            "a"
        )

        search_box.send_keys(
            Keys.BACKSPACE
        )

        time.sleep(1)

        #  new contact name
        search_box.send_keys(
            name
        )

        print(
            f"Searching for: {name}"
        )

        # Wait search results
        time.sleep(2)

        return True

    except Exception as e:

        print(
            f"Could not search for {name}"
        )

        print(
            "Error:",
            e
        )

        return False



# OPEN CHAT


def open_chat(driver, name):

    wait = WebDriverWait(
        driver,
        15
    )

    try:

        # Find contact
        contact = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f'//span[@title="{name}"]'
                )
            )
        )

        # Scroll contact into center
        driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            contact
        )

        time.sleep(1)

      
        # Try normal click
  

        try:

            contact.click()

        except:

           
            # Try parent element
       

            try:

                parent = contact.find_element(
                    By.XPATH,
                    "./ancestor::*[@role='listitem'][1]"
                )

                driver.execute_script(
                    "arguments[0].click();",
                    parent
                )

            except:

               
                # Final JavaScript click


                driver.execute_script(
                    "arguments[0].click();",
                    contact
                )

        print(
            f"Chat opened: {name}"
        )

        time.sleep(2)

        return True

    except Exception as e:

        print(
            f"Contact not found: {name}"
        )

        print(
            "Error:",
            e
        )

        return False



# SEND MESSAGE

def send_message(driver, message):

    wait = WebDriverWait(
        driver,
        30
    )

    try:

        # Find message box
        message_box = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//footer//div[@contenteditable="true"][@role="textbox"]'
                )
            )
        )

        message_box.click()



        # Clear any previous text


        message_box.send_keys(
            Keys.COMMAND,
            "a"
        )

        message_box.send_keys(
            Keys.BACKSPACE
        )

        time.sleep(1)


        # Type message


        message_box.send_keys(
            message
        )

        print(
            f"Message typed: {message}"
        )

        # Give WhatsApp time
        time.sleep(2)


        # Send message


        message_box.send_keys(
            Keys.ENTER
        )

        print(
            "Enter pressed. Waiting for WhatsApp..."
        )

        # Wait after sending
        time.sleep(3)

        print(
            "Message sent!"
        )

        return True

    except Exception as e:

        print(
            "Message could not be sent."
        )

        print(
            "Error:",
            e
        )

        return False



# MAIN PROGRAM


birthdays = load_birthdays()

print(
    "\nAll Birthdays:"
)

print(
    birthdays
)


# LOAD SENT RECORDS

sent_birthdays = load_sent_birthdays()


# GET TODAY'S BIRTHDAYS

today_birthdays = get_todays_birthdays(
    birthdays
)


print(
    "\nToday's Birthdays:"
)


if len(today_birthdays) == 0:

    print(
        "No birthdays today."
    )

else:

    for person in today_birthdays:

        print(
            person["name"]
        )



# FIND PENDING BIRTHDAYS


pending_birthdays = []


for person in today_birthdays:

    name = person["name"]

    if already_sent(
        sent_birthdays,
        name
    ):

        print(
            f"\nAlready sent to {name} today. Skipping..."
        )

    else:

        pending_birthdays.append(
            person
        )


# SEND BIRTHDAY MESSAGES

if len(pending_birthdays) == 0:

    print(
        "\nNo birthday messages need to be sent."
    )

else:

    print(
        "\nPending Birthday Messages:"
    )

    for person in pending_birthdays:

        print(
            person["name"]
        )


    # START WHATSAPP

    driver = start_browser()

    print(
        "\nWhatsApp Web is ready!"
    )

    # PROCESS EACH BIRTHDAY

    for person in pending_birthdays:

        name = person["name"]

        print(
            f"\nSending birthday message to: {name}"
        )


       
        # SEARCH CONTA

        search_success = search_contact(
            driver,
            name
        )

        if not search_success:

            print(
                f"Skipping {name}"
            )

            continue



        # OPEN CHAT
   

        chat_success = open_chat(
            driver,
            name
        )

        if not chat_success:

            print(
                f"Skipping {name}"
            )

            continue



        # CREATE MESSAGE


        message = create_message(
            name
        )


        # SEND MESSAGE
      

        message_success = send_message(
            driver,
            message
        )


        # MARK AS SENT IF SUCCESSFUL

        if message_success:

            print(
                f"Birthday message sent to {name}."
            )

            mark_as_sent(
                sent_birthdays,
                name
            )

        else:

            print


        # Small gap before next person
        time.sleep(2)


    # FINISH

    print(
        "\nAll birthday messages processed!"
    )

    time.sleep(2)

    driver.quit()

    print(
        "WhatsApp closed automatically."
    )