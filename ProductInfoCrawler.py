# 1. 필요한 라이브러리 설치
#!pip install beautifulsoup4 pandas gspread oauth2client

# 2. 구글 드라이브 마운트
#from google.colab import drive
#drive.mount('/content/drive')

# 3. 필요한 라이브러리 임포트
import requests
from bs4 import BeautifulSoup
import pandas as pd
#import gspread
#from google.oauth2.service_account import Credentials

# JSON 파일 경로 설정
#json_file_path = '/content/drive/MyDrive/008_AutoMerch_Pro/automerch-pro-20240516-c193c95f498c.json'

# Google Sheets API 설정 및 인증
#credentials = Credentials.from_service_account_file(json_file_path)
#client = gspread.authorize(credentials)

# 스프레드시트 열기
#spreadsheet_id = '16MKGmkQWFvNhDpBMkJQXZSvZzs1gFo-eGlpfKYLyGS4'  # 스프레드시트 ID
#spreadsheet = client.open_by_key(spreadsheet_id)
#worksheet = spreadsheet.get_worksheet(0)  # 첫 번째 워크시트

# 4. 크롤링할 URL 설정
url = 'https://dometopia.com/goods/view?no=186427'  # 크롤링할 도메 사이트의 URL

# 페이지 가져오기
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 상품 정보 추출
product_name_tag = soup.find('div', class_='pl_name')
product_name = product_name_tag.find('h2').text.strip() if product_name_tag else 'No Name'

product_code_tag = soup.find('td', style='width:22%;')
product_code = product_code_tag.find('span', class_='goods_code').text.strip() if product_code_tag else 'No Code'

price = soup.find(class_="price_red").text
price = price.replace(',', '').replace('원', '') if price else 'No Price'

detail_imgs = soup.find(class_="detail-img").find("img")["src"]
detail_imgs = "https://dometopia.com" + detail_imgs if detail_imgs else 'No Image'

page_url = url

products = [{
    'Product Name': product_name,
    'Product Code': product_code,
    'Price': price,
    'Detail Image': detail_imgs,
    'URL': page_url
}]

# DataFrame 생성
df = pd.DataFrame(products)
print(df)

# DataFrame을 스프레드시트에 업로드
#worksheet.update([df.columns.values.tolist()] + df.values.tolist())

print("Data successfully written to Google Sheets.")
