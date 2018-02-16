# selenium automatic friends adder
import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':

    # parse the parameters
    parser = argparse.ArgumentParser(description='LinkedInAdder is a small tool that helps you add your friends on LinkinedIn automatically.')
    parser.add_argument('--email', type=str, help='LinkedIn Email', required=True)
    parser.add_argument('--password', type=str, help='LinkedIn Password', required=True)
    parser.add_argument('--chromeDriver', type=str, default='./chromedriver', help='Chrome Driver Location')
    parser.add_argument('--keyWords', type=str, default='', help='Connection Filter')
    parser.add_argument('--refreshTime', type=int, default=10, help='How long you want to refresh the page')
    parser.add_argument('--batchSize', type=int, default=10, help='how many pages you want to refresh in a batch')
    parser.add_argument('--batchInterval', type=int, default=120, help='the gap between each batch')
    args = parser.parse_args()
    if args.keyWords != '':
        # to do handle this
        addAll = False
        keyWords = set([keyWord.strip().lower() for keyWord in args.keyWords.split(',')])
    else:
        addAll = True

    # parameters
    BATCH_SIZE = args.batchSize
    BATCH_INTERVAL = args.batchInterval
    REFRESH_TIME = args.refreshTime   # wait for the JS request to finish
    WAIT_AFTER_CLICK_TIME = 1         # wait after click the 'connect' button

    # login the LinkedIn
    driver = webdriver.Chrome(args.chromeDriver)
    driver.get("https://www.linkedin.com")
    email = driver.find_element_by_id("login-email")
    email.send_keys(args.email)
    password = driver.find_element_by_id("login-password")
    password.send_keys(args.password)
    driver.find_element_by_id("login-submit").click()

    # click 'connect' on LinkedIn Pages
    driver.get("https://www.linkedin.com/mynetwork/")
    time.sleep(REFRESH_TIME)

    counter = 0
    # loop the whole process
    while True:
        # for each page
        counter += 1
        person_index = 0
        while True:
            # get the info cards on the current page
            person_infos = driver.find_elements_by_class_name("mn-pymk-list__card")
            # if there is no candidates left
            if person_index == len(person_infos):
                break
            try:
                # if not addAll apply filter
                if not addAll:
                    # select the keywords
                    occupation = person_infos[person_index].find_element_by_class_name("mn-person-info__occupation")
                    occupation_description = occupation.text.lower()
                    toClick = False
                    for keyWord in keyWords:
                        if keyWord in occupation_description:
                            toClick = True
                            break
                    if not toClick:
                        # if not click the profile to stay where it is, so move the index by 1
                        person_index += 1
                        continue
                # if click, person_info will disappear so do not need to move the index
                person_infos[person_index].find_element_by_class_name("button-secondary-small").click()
                time.sleep(WAIT_AFTER_CLICK_TIME)
            except:
                break  
        driver.refresh()
        if counter % BATCH_SIZE == 0:
            time.sleep(BATCH_INTERVAL)
        else:
            time.sleep(REFRESH_TIME)