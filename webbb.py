import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

books = []

# Find all book cards
cards = soup.find_all("article", class_="product_pod")

for card in cards:
    
    # Book Title
    title = card.h3.a["title"]
    
    # Price
    price = card.find("p", class_="price_color").get_text()
    
    # Availability
    availability = card.find("p", class_="instock availability").get_text(strip=True)
    
    # Rating (stored in class)
    rating_class = card.find("p", class_="star-rating")["class"]
    rating = rating_class[1]   # e.g., 'Three', 'Five'
    
    books.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Availability": availability
    })

# Convert to DataFrame
df = pd.DataFrame(books)

# Show output
print(df)

# Save to CSV (optional)
choice = input("\nSave to CSV? (yes/no): ")
if choice.lower() == "yes":
    df.to_csv("books.csv", index=False)
    print("Saved to books.csv")