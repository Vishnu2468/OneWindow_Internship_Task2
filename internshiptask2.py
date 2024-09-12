import requests
from bs4 import BeautifulSoup
import json

# Define the base URL
url = 'https://www.4icu.org/de/universities/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Initialize an empty list to store the university data
universities = []

# Function to extract social media links (with proper checks)
def extract_social_links(row):
    links = {
        "facebook": None,
        "twitter": None,
        "instagram": None,
        "officialWebsite": None,
        "linkedin": None,
        "youtube": None
    }
    
    for a_tag in row.find_all('a', href=True):
        href = a_tag['href']
        if 'facebook.com' in href:
            links['facebook'] = href
        elif 'twitter.com' in href:
            links['twitter'] = href
        elif 'instagram.com' in href:
            links['instagram'] = href
        elif 'linkedin.com' in href:
            links['linkedin'] = href
        elif 'youtube.com' in href:
            links['youtube'] = href
        elif 'http' in href:
            links['officialWebsite'] = href
    
    return links

# Iterate over the table rows to extract details (adjust based on actual HTML structure)
university_rows = soup.find_all('tr')

for row in university_rows[1:]:  # Skipping the header
    try:
        # Extract the university name and logo URL
        name_tag = row.find('a')
        name = name_tag.text.strip() if name_tag else None
        
        logo_tag = row.find('img')
        logo_src = f"https://www.4icu.org{logo_tag['src']}" if logo_tag else None
        
        # Dummy data for state, city, and other fields (replace with actual scraping logic)
        location = {
            "country": "Germany",  # All universities are in Germany
            "state": "State_Name",  # Placeholder for state
            "city": "City_Name"     # Placeholder for city
        }
        
        type_of_uni = "public"  # Placeholder (adjust based on actual data)
        established_year = "1829"  # Placeholder (adjust based on actual data)
        
        # Extract phone number (dummy placeholder for now)
        phone_number = "1234567890"  # Replace with actual scraping logic

        # Extract social media links
        contact = extract_social_links(row)

        # Store the university data
        universities.append({
            "name": name,
            "location": location,
            "logoSrc": logo_src,
            "type": type_of_uni,
            "establishedYear": established_year,
            "contact": contact,
            "phone": phone_number
        })
        
    except Exception as e:
        print(f"Error processing row: {e}")

# Save the extracted data to a JSON file
with open('universities2.json', 'w', encoding='utf-8') as f:
    json.dump(universities, f, indent=4, ensure_ascii=False)

print("Data saved to universities.json")
