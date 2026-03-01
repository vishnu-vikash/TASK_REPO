from testUrl import Browser

url = 'https://www.guvi.in/'
browser = Browser('url')
my_browser = Browser(url)

def test_get_title():
    title_of_page = my_browser.get_title()
    if title_of_page == 'HCL GUVI | Learn to code in your native language':
        print("Test Passed, Title of page verification completed")
    else:
        print("Test Failed, Title of page verification failed")

        # Homework: Create / Edit
        # negative
        # testing
        # scenario
        # for validation of wrong url and title.The result of test case should be passed