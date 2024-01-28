import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import shutil
import time

# This files automatize the access of csv from original website. The script will create a folder csv_files

def create_json_file(folder_path, year, month):
    json_data = {
        "last_file": {
            "year": year,
            "month": month,
            "file_path": f"{year}_{month}.csv"
        }
    }
    json_file_path = os.path.join(folder_path, "last_checkpoint.json")
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)
    print(f"JSON file created successfully: {json_file_path}")

def create_folder(folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"The folder {folder_name} already exists in {os.getcwd()}.")

def wait_for_file_download(download_directory, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        files = [f for f in os.listdir(download_directory) if f.endswith('.crdownload')]
        if not files:
            return True
        time.sleep(1)
    return False

def exportar_dados(driver, download_directory, folder_path, year, month):
    # Wait for the 'Exportar Dados' button to be clickable
    export_button = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-warning.btn-sm.dropdown-toggle"))
    )
    print("Find the 'Exportar Dados button.'")
    
    # Move to the 'Exportar Dados' button to ensure it's in the viewport
    webdriver.ActionChains(driver).move_to_element(export_button).perform()
    
    # Click the 'Exportar Dados' button
    export_button.click()
    
    csv_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@ng-click='ctrl.gerarCSV()']"))
    )
    print("Find the CSV button")
    csv_option.click()
    print("Click the CSV button")

    # Wait for the download to complete in the system Downloads directory
    downloaded_file_path = os.path.join(os.path.expanduser("~"), "Downloads", "DETALHAMENTO DA FOLHA DE PAGAMENTO DE PESSOAL.csv")
    WebDriverWait(driver, 30).until(lambda x: os.path.exists(downloaded_file_path))

    # Move the downloaded file to the 'csv_files' directory and rename it
    renamed_file_path = os.path.join(folder_path, f"{year}_{month}.csv")
    shutil.move(downloaded_file_path, renamed_file_path)
    print(f"Moved and renamed the file to {renamed_file_path}")

def select_dropdown_option(driver, dropdown_id, option_text):
    dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, dropdown_id))
    )
    dropdown_select = Select(dropdown)
    dropdown_select.select_by_visible_text(option_text)

def click_buscar_button(driver):
    buscar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btn-search"))
    )
    buscar_button.click()
    print("Clicked 'Buscar' button.")

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')


# Specify the download directory
download_directory = os.path.join(os.getcwd(), "csv_files")
options.add_argument(f'download.default_directory={download_directory}')

# Set up Chrome service
service = Service(executable_path=r'chromedriver-linux64/chromedriver')

# Create a Chrome driver instance
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://transparencia.tjba.jus.br/transparencia/home#!/remuneracao")
    print("Opened page successfully.")

    # Create the 'csv_files' folder
    create_folder("csv_files")

    # Read the last downloaded file information from JSON
    last_downloaded_file_path = os.path.join(download_directory, "last_checkpoint .json")
    if os.path.exists(last_downloaded_file_path):
        with open(last_downloaded_file_path, 'r') as last_downloaded_file:
            last_downloaded_data = json.load(last_downloaded_file)
            last_year = last_downloaded_data["last_file"]["year"]
            last_month = last_downloaded_data["last_file"]["month"]
            print(f"Last downloaded file info found. Resuming from {last_year}_{last_month}.")

            # Wait until the 'ano' dropdown is visible
            years = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//select[@id='ano']/option[position()>1]"))
            )

            # Iterate over the years
            for year_option in years:
                year_text = year_option.text
                print(f"\nYear: {year_text}")

                # Select the year
                select_dropdown_option(driver, "ano", year_text)
                print("Selected the year.")

                # Iterate over the months
                months = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//select[@id='mes']/option[position()>1]"))
                )

                # Skip to the next year if the current year is before the last downloaded year
                if year_text < last_year:
                    continue

                for month_option in months:
                    month_text = month_option.text
                    print(f"\nMonth: {month_text}")

                    # Skip to the next month if the current year is the last downloaded year and the month is before the last downloaded month
                    if year_text == last_year and month_text < last_month:
                        continue

                    # Select the month
                    select_dropdown_option(driver, "mes", month_text)
                    print("Selected the month.")

                    # Click the 'Buscar' button
                    click_buscar_button(driver)

                    table = WebDriverWait(driver, 50).until(
                        EC.presence_of_all_elements_located((By.ID, "tableExport"))
                    )
                    print("The table is visible.")

                    # Call the exportar_dados function with year and month information
                    exportar_dados(driver, download_directory, download_directory, year_text, month_text)

                    # Create checkpoint JSON
                    create_json_file(download_directory, year_text, month_text)

    else:
        print("No last downloaded file info found. Starting from the beginning.")

finally:
    driver.quit()
