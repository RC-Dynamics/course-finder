import requests
from bs4 import BeautifulSoup

page  = requests.get("https://www.cars.com/vehicledetail/detail/738001937/overview/")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')
tabela = soup.find_all(class_="vdp-details-basics__item")


for item in tabela:
    if(item.get_text().split()[0] == "Fuel"):
        fuel = item.get_text().split(":")[-1]
        fuel = fuel.strip().replace('\n','')
    elif(item.get_text().split()[0] == "Exterior"):
        exterior_color = item.get_text().split(":")[-1]
        exterior_color = exterior_color.strip().replace('\n','')
    elif(item.get_text().split()[0] == "Interior"):
        interior_color = item.get_text().split(":")[-1]
        interior_color = interior_color.strip().replace('\n','')
    elif(item.get_text().split()[0] == "Engine:"):
        engine = item.get_text().split(":")[-1]
        engine = engine.strip().replace('\n','')
    elif(item.get_text().split()[0] == "VIN:"):
        vin = item.get_text().split(":")[-1]
        vin = vin.strip().replace('\n','')

print(fuel)
print(str(exterior_color))
print(str(interior_color))
print(str(engine))
print(str(vin))