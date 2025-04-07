from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.shl.com/solutions/products/product-catalog/")

# Wait for page to load
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
print("Page loaded successfully.")

# List to store data
data = []

def process_links(links):
    for link in links:
        try:
            name = link.text.strip()
            url = link.get_attribute("href")
            if not name or len(name) < 5 or not url or "shl.com" not in url or "/product-catalog/view/" not in url:
                continue
            print(f"Processing assessment: {name} | {url}")
            remote_testing = "Yes"
            adaptive_irt = "Yes" if any(x in name.lower() for x in ["verify", "coding", ".net", "java"]) else "No"
            name_lower = name.lower()
            if "coding" in name_lower or any(x in name_lower for x in [".net", "ado", "mvc", "wpf", "xaml", "java"]):
                test_type = "Technical"
                duration = "40 minutes"
            elif "verify" in name_lower:
                test_type = "Cognitive"
                duration = "30 minutes"
            elif any(x in name_lower for x in ["solution", "short form", "manager", "clerk", "agent"]):
                test_type = "Job-Specific"
                duration = "25 minutes"
            elif "simulation" in name_lower:
                test_type = "Simulation"
                duration = "20 minutes"
            else:
                test_type = "N/A"
                duration = "N/A"
            data.append({
                "Assessment Name": name,
                "URL": url,
                "Remote Testing Support": remote_testing,
                "Adaptive/IRT Support": adaptive_irt,
                "Duration": duration,
                "Test Type": test_type
            })
        except Exception as e:
            print(f"Error processing link: {e}")

# Find total number of pages dynamically (if possible)
try:
    total_pages_elem = driver.find_element(By.XPATH, "//span[contains(text(), 'of')]")
    total_pages_text = total_pages_elem.text
    total_pages = int(total_pages_text.split('of')[1].strip())
    print(f"Detected total pages: {total_pages}")
except:
    total_pages = 44  # Fallback: 12 (Pre-packaged) + 32 (Individual)
    print(f"Could not detect total pages. Using fallback: {total_pages}")

# Process all pages
page_count = 0
while page_count < total_pages:
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Page {page_count + 1}: Found {len(links)} <a> elements")
    process_links(links)
    
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Next')]"))
        )
        next_button.click()
        time.sleep(3)  # Wait for next page to load
        page_count += 1
    except:
        print(f"Stopped at page {page_count + 1}. No more 'Next' button or error.")
        break

# Close the driver
driver.quit()

# Save to CSV
if data:
    df = pd.DataFrame(data)
    df.drop_duplicates(subset=["Assessment Name", "URL"], inplace=True)
    df.to_csv("shl_assessments_full.csv", index=False)
    print(f"Data saved to shl_assessments_full.csv with {len(df)} assessments.")
else:
    print("No valid assessment data scraped.")