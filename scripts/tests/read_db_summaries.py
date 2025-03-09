import requests
from common.config import BASE_URL

def get_db_summaries(since: int) -> list[dict]:
    response = requests.get(BASE_URL + f"summarizations/since/{since}")
    return response.json()

def main():
    summaries = get_db_summaries(0)
    print(f"Succesfully fetched {len(summaries)} summaries.")
    print(summaries)

if __name__ == "__main__":
    main()