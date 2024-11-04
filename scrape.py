from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# BeautifulSoup is a library that parses HTML and XML documents.
from bs4 import BeautifulSoup

def scrape_website(website):
    print(f"Scraping website: {website}")

    # specifies where our chrome driver is located
    chrome_driver_path = "./chromedriver"
    # specifies how chrome driver should run
    options = webdriver.ChromeOptions() 
    # creates a new chrome browser session
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        # get website link
        driver.get(website)
        print("Page loaded successfully")
        html = driver.page_source
        time.sleep(10)

        return html;
    finally:
        driver.quit()

# extracts the body of the website
def extract_body(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body = soup.body
    if body:
        return str(body)
    return ""

def clean_bdoy(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    # remove all script and style elements from body
    for script in soup(["script", "style"]):
        script.extract()
    
    # extracts the text from the body
    cleaned_content = soup.get_text(separator="\n")

    # removes any leading or trailing whitespace from each line
    cleaned_content = "\n".join(
        [line.strip() for line in cleaned_content.splitlines() if line.strip()]
        )

    return cleaned_content

def split_Dom_Content(dom_content, max_length=6000):
    return [
        # splits the content into an array of max_length characters, in this case 6000
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
    ]
