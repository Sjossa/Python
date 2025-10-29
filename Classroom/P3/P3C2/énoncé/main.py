import requests
from bs4 import BeautifulSoup
with open("/Python/Classroom/P3/P3C2/énoncé/index.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')


title = soup.title.string
print(title)


h1_text = soup.find("h1").string
print( h1_text)


all_products = dict()


products = soup.find_all("li")
for product in products:
    name = product.find("h2").string
    price_str = product.find("p", class_="price").string

    price_list = price_str.split(" ")

    all_products[name] = {"prix": price_list[1]}


    description = product.find_all("p")[-1].string
    all_products[name]["description"] = description


# print("Produits:", all_products)

for name in all_products.keys():
    price_str = all_products[name]["prix"]

    price = price_str.strip("€")

    price = float(price)
    dollar_price = price * 1.2
    all_products[name]["prix_dollar"] = f"{dollar_price}$"
print(f"Tous les produits: {all_products}\n")




