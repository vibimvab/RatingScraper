import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

df = pd.read_excel("산업기능요원 업체.xlsx")
company_names = df["업체명"].dropna().tolist()

driver = webdriver.Chrome()  # Make sure chromedriver is installed
driver.get("https://www.jobplanet.co.kr/")
time.sleep(2)

ratings = []


# name = company_names[0].split(')')[-1]
# driver.get(f"https://www.jobplanet.co.kr/search?query={name}")
# try:
#     rating_element = driver.find_element(By.XPATH, '//main//div[@id="contentsWrap"]//div[@class="group desktop"]//ul/a[1]/div/div/div[2]/div/div/div/span[2]')
#     print(rating_element)
#     print(f"Rating found: {rating_element.text}")
# except Exception as e:
#     ratings.append("N/A")
#     print(f"Failed for {name}: {e}")
# time.sleep(5)

# i = 0
for name in company_names:
    # i += 1
    try:
        name = name.split(')')[-1]
        driver.get(f"https://www.jobplanet.co.kr/search?query={name}")
        time.sleep(3)

        # Select first result (may vary)
        rating_element = driver.find_element(By.XPATH, '//main//div[@id="contentsWrap"]//div[@class="group desktop"]//ul/a[1]/div/div/div[2]/div/div/div/span[2]')
        rating = rating_element.text
        ratings.append(rating)
        print(f"Rating found for {name}: ", rating)

    except Exception as e:
        ratings.append("N/A")
        print(f"Failed for {name}: {e}")

    # if i > 20:
    #     break

df["잡플래닛 별점"] = ratings
df.to_excel("업체_별점_결과.xlsx", index=False)
