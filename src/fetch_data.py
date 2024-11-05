import requests
import logging
import json
import uuid
logging.basicConfig(level=logging.INFO)
# Function to fetch data from API

def build_url(date: str):
    base_url: str = "https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/eco2mix-regional-tr/records?"
    limit_url: str = "limit=100"
    order_by: str = 'order_by="date_heure"'
    filtre_region: str = "refine=libelle_region%3A%22Auvergne-Rh%C3%B4ne-Alpes%22"
    filtre_date: str = f'refine=date:"{date}"'  # 2024-03-07
    api_url: str = base_url + "&".join([limit_url, order_by, filtre_region, filtre_date])
    return api_url


# api_url: str = "https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/eco2mix-regional-tr/records?limit=100&refine=libelle_region%3A%22Auvergne-Rh%C3%B4ne-Alpes%22"
def fetch_data(api_url):
    response = requests.get(api_url)
    status_code: int = response.status_code
    if status_code == 200:
        data = response.json()
        id_json: uuid = uuid.uuid4()
        id_json = str(id_json).split("-")[0]
        with open(f"data/raw/{id_json}.json", "w") as f:
            json.dump(data, f)
    return status_code

if __name__ == "__main__":
    
    for d in range(1,8):
        date: str = f'2024-03-{d:02d}'
        print(date)
        fetch_data(build_url(date))
