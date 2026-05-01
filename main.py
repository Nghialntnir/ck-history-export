import requests
import pandas as pd
import time
import random

# --- CẤU HÌNH ---
TOKEN = ""
BASE_URL = "http://p-app.circlek.com.vn/api/transaction-points"
FILE_NAME = "circlek_transactions.xlsx"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "User-Agent": "Dart/3.6 (dart:io)",
    "Accept": "application/json"
}

def fetch_transactions():
    all_data = []
    current_page = 1
    total_pages = 1 
    
    print("Crawing Circle K by Nghia...")

    while current_page <= total_pages:
        retry_count = 0
        success = False
        
        while retry_count < 3:
            try:
                print(f"Load page {current_page}/{total_pages if total_pages > 1 else '?'}")
                response = requests.get(f"{BASE_URL}?page={current_page}", headers=headers, timeout=30)
                
                if response.status_code == 200:
                    res_json = response.json()
                    data_part = res_json.get('data', {})
                    transactions = data_part.get('data', [])
                    
                    if transactions:
                        all_data.extend(transactions)
                        if current_page == 1:
                            total_pages = data_part.get('last_page', 1)
                        success = True
                        break
                    else:
                        print(f"Page {current_page} empty.")
                        success = True
                        break
                else:
                    retry_count += 1
                    print(f"HTTP {response.status_code}. Retry {retry_count}/3...")
                    time.sleep(40)

            except Exception as e:
                retry_count += 1
                print(f"Error {e}. Again {retry_count}/3...")
                time.sleep(10)
        
        if not success:
            print(f"Test fail 3 times {current_page}. Skip to next page.")
            if current_page == 1:
                total_pages = 70 
        
        current_page += 1
        wait = random.uniform(30, 45)
        print(f"Sleep {wait:.2f}s avoid block...")
        time.sleep(wait)

    return all_data

def save_to_excel(raw_data):
    if not raw_data:
        print("No data to save.")
        return
        
    clean_data = []
    for item in raw_data:
        clean_data.append({
            "Ngày giao dịch": item.get('date_create'),
            "Cửa hàng": item.get('store_name'),
            "Tổng tiền (VND)": float(item.get('total', 0))
        })

    df = pd.DataFrame(clean_data)
    df['Ngày giao dịch'] = pd.to_datetime(df['Ngày giao dịch'])
    df.to_excel(FILE_NAME, index=False)
    
    print("-" * 30)
    print(f"Total transactions: {len(raw_data)}")
    print(f"Total money: {df['Tổng tiền (VND)'].sum():,.0f} VND")
    print(f"File: {FILE_NAME}")

if __name__ == "__main__":
    data = fetch_transactions()
    save_to_excel(data)