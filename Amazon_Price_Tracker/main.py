import requests
import smtplib
from bs4 import BeautifulSoup

product_url = "https://www.amazon.com.br/QCY-HT05-Bluetooth-Cancelamento-Reprodução/dp/B0BN5WJ5V6/ref=sr_1_6?crid=M4SS656OOQFJ&dib=eyJ2IjoiMSJ9.NQwKilznRNiA8D0NwYiLE9M3q5-idaIpESMGxRLt9i9qrWnFtrAj6cqr_cxKnVNfh_dLoq_mF8BVq8bO0pAucmY71qXwCWmDNIH0E7U8stGGqQSaEzmNipGHERo9ryoWT46VLxfrjMCATJEOZqz_HKlujpfMh-S5AAbmILBrIlvY2iE4AMXTgnYfl1L4USjzZa6yOvUtvx_IJRhV94hDNvjTL_btQhBoGC1ywNALOsPJGk4AnNnP3iwGtZ26LsL0M4naQ7l8TEJq4MuhI3rB6whSFzBlaQAnH48VcubDrLw.PR00JndtnjhcFaCc4uqazkArdALnZHs2JPqmNye9TGc&dib_tag=se&keywords=fone%2Bht05%2Bqcy&qid=1720541641&sprefix=fones%2BHT05%2Caps%2C164&sr=8-6&ufe=app_do%3Aamzn1.fos.6121c6c4-c969-43ae-92f7-cc248fc6181d&th=1"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "pt-BR",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Opera GX\";v=\"111\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://www.amazon.com.br/s?k=QCY+HT05&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3CW0MEZEF59P8&sprefix=qcy+ht05%2Caps%2C254&ref=nb_sb_noss_1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0",
    "Cookie": "session-id=136-3001359-6572363; ubid-acbbr=134-0980234-8420114; x-acbbr=8jv06W58xdPGxQa2rLcRfiFKTicS5cBVvaps6j7Czh7ug9NeUbKYDa4tMqYETrJi; at-acbbr=Atza|IwEBIBVcJZobM7dSe-jYo59GhLZ9qY-fYDoT5COA13uP_lsOHNeNOvqtzpOzJXAbARk0RrO5w06R8YBmjtp7u24niPYWB4dyNDCNVo1r-YI9wz1FTxR18OIieG4crI1EvUQtG6zK7w2Za8nTIgfU0G68221jrG3hwkOqdZJNlu2JdVLt86R3w1xf6g1Awn3zPHWN-EMNJQesyDuWoVU-FTLw4UMk_LZqRR5cScGsBUpQTPmZWg; sess-at-acbbr='hxnjwsmOPzLm44b2HnfwkunwGl2aKs7gV2Yc/mzx6rY='; sst-acbbr=Sst1|PQHOTyY7WMT1A39SEmE29hgIDEeKkw7hTkgnlAPqPtLepamyC0w2oKyAleGIwYO2DTC5ew-Pa7H0tPHpH1YCdeJfUQYAfobdnflggvqlt9QXfe1AQIlSvgJHb0NhFA3vOBKBZaoNcPNu0KHRzYBGe3ATBLQz1cLE7gkYtysYNgLseqgevatoZVUsbkUadn4NiAwXRu6vRHBIhjo9ySwYEFy_whToCB5t0p59maKrbTg7PwBPvH9xCc6xa65MQmnsF_eMOLOP8rGeOaBCn1tOl8_1btcOXQwuz3SWypPMg8mpFrNnyQJlyFCJ_fhkYhmw_AYHEjKe61ASKOxWNUTG30_pUvSVxVnQ9bdkubgngKRhlyo; i18n-prefs=BRL; lc-acbbr=pt_BR; session-token='ONK4xtkltTjZReYIGgbu+mJmlyoEa9HphtI46o4e3mYGOK68haLvE8uhSQnUTa9xwFbv4eP4dhtwRjpBUdwX49nFW1CPC8HXJvu6dmlMXaV7GnBdt++f7NqHpwqctg2yc9+oEAgN7zvq5ABXy0MT6LB9UpOD5xvJl07WYijYew9pTaRb4dYmVD3PmieHo+TCNbsXHv39+dxNPWczjLt6sWU3pHWHVBmXfcRARLnOWC3/fteQJcrDF0OMQff8hzrrNHMkxnnkIHxiE3I7A0yxUGYH1P2jCJa83gvSQqQAX1btBDhPjxf8E92ttYMt0eG16Jp+34XwTl97lnuz01/DVTZzMLVYqPzmbge5kyirlsctU6kkpaOCEiLyl1mWPOr2gY4g43QHgwI='; session-id-time=2082787201l; csm-hit=YMKQB3904D0SP6PAXQAJ+s-RE0T22W8GQKDAFVAM0GQ|1720572656511"
}

response = requests.get(url=product_url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())

discount = soup.find_all(class_="savingsPercentage")

product_title = soup.find(id="productTitle").getText()
product_title = str.strip(product_title)
price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("$")[1].replace(',', '.')
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float <= 120:
    with smtplib.SMTP(host="smtp.gmail.com", port=578) as smtp:
        smtp.starttls()
        smtp.login(user="YOUR EMAIL", password="YOUR APP PASSWORD")
        smtp.sendmail(from_addr="YOUR EMAIL", to_addrs="ANOTHER EMAIL",
                      msg=f"Subject:Promocao\n\nO produto {product_title} está em promocao pelo valor de R${price:.2f}")
        smtp.close()
