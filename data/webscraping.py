import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Create a randomized User-Agent
ua = UserAgent()
headers = {'User-Agent': ua.random}

# Specify the company name
company_name = 'microsoft'
# Specify the number of results you want to retrieve
num_results = 10

# Construct the search query
query = company_name + ' reviews'

# Send a request to Bing's advanced search feature
url = f'https://www.bing.com/search?q={query}&count={num_results}'
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the URLs from the HTML
urls = []
for item in soup.find_all('li', {'class': 'b_algo'}):
    url = item.find('a').get('href')
    urls.append(url)
# Define a dictionary of class names for different websites
class_names = {
    'www.glassdoor.com': 'gdReview',
    'www.consumeraffairs.com': 'rvw-aut',
    'pcmag': 'line-clamp-2 text-gray-darker',
    'www.indeed.com' : 'reviewDescription',
    'www.trustradius.com' : 'review-layout__review',
    'www.trustpilot.com' : 'styles_reviewContent__0Q2Tg',
}

# loop through each URL and extract the reviews
reviews = []
for url in urls:
    # Get the domain name of the URL
    domain_name = url.split('//')[-1].split('/')[0]
    # Get the class name for the current website
    class_name = class_names.get(domain_name, '')
    print(domain_name)
    if class_name:
        # send a request to the webpage
        response = requests.get(url, headers=headers)
        # parse the html content
        soup = BeautifulSoup(response.content, 'html.parser')
        # extract the reviews
        data = soup.find_all('div', {'class': class_name})
        # add the reviews to the list
        for item in data:
            reviews.append(item.text)
    else:
        print(f"Review class not found for {domain_name}")

# print the reviews
for review in reviews:
    print(review)

# write the reviews to a file
with open("reviews.txt", "w") as file:
    for review in reviews:
        file.write(review + '\n')
    
