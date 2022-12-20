# Goto a weather website 
# Get the current temperature and weather for your local city. 
# Print the current temperature and weather

# Hit the website using requests module
# Parse the HTML returned by requests module using the bs4 module
# Fetch the current temp and weather using parsed HTML. 
# Print it

import requests
import bs4

def send_request(website_url: str) -> str: 
   return requests.get(website_url).text

def parse_html_string(html_str: str) -> bs4.BeautifulSoup: 
    soup = bs4.BeautifulSoup(html_str, 'html.parser')
    return soup

def fetch_current_nepali_date(parsed_html: bs4.BeautifulSoup) -> str: 
    top_element = parsed_html.find(id = "top")
    date_element = top_element.find('div', class_ = "date")
    current_date = date_element.span.string.removeprefix('\n')
    return current_date

def main():
    website = "https://www.hamropatro.com/"
    html_str = send_request(website)
    parsed_html = parse_html_string(html_str)
    current_date = fetch_current_nepali_date(parsed_html)
    print(f'The current date {current_date} .')

if __name__ == '__main__':
    main()