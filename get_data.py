import requests
from bs4 import BeautifulSoup

kompas_100_ticker = [
  "ABMM", "BNGA", "GOTO", "MBMA", "SIDO",
  "ACES", "BRIS", "HEAL", "MDKA", "SILO",
  "ADMR", "BRMS", "HMSP", "MEDC", "SMGR",
  "ADRO", "BRPT", "HRUM", "MIKA", "SMIL",
  "AKRA", "BSDE", "ICBP", "MNCN", "SMRA",
  "AMMN", "BTPS", "INCO", "MPMX", "SMSM",
  "AMRT", "BUKA", "INDF", "MTEL", "SRTG",
  "ANTM", "CMRY", "INDY", "MYOR", "SSIA",
  "ARTO", "CPIN", "INKP", "NCKL", "SSMS",
  "ASII", "CTRA", "INTP", "NISP", "TBIG",
  "AUTO", "DOID", "ISAT", "PANI", "TINS",
  "AVIA", "DSNG", "ITMG", "PGAS", "TKIM",
  "BBCA", "ELSA", "JPFA", "PGEO", "TLKM",
  "BBNI", "EMTK", "JSMR", "PNLF", "TOWR",
  "BBRI", "ENRG", "KIJA", "PTBA", "TPIA",
  "BBTN", "ERAA", "KLBF", "PTMP", "ULTJ",
  "BBYB", "ESSA", "MAHA", "PTPP", "UNTR",
  "BFIN", "EXCL", "MAPA", "PTRO", "UNVR",
  "BMRI", "GGRM", "MAPI", "PWON", "VKTR",
  "BMTR", "GJTL", "MARK", "SCMA", "WIFI"
]

def fetch_data (url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    return response.text


def get_stock_price_data (ticker):
    data = []

    try:
        response = fetch_data(f"https://finance.yahoo.com/quote/{ticker}.JK/history/")

        result = BeautifulSoup(response, 'html.parser')

        table = result.find('table', class_='noDl')
        body = table.find("tbody")
        
        for row in body:
            col = row.find_all('td')

            if len(col) == 7:

                closing_price = col[4].string
                final_closing_price = []

                for i in range(len(closing_price)):

                    if closing_price[i] == ',':
                        continue
                    elif closing_price[i] == '.':
                        break
                    
                    final_closing_price.append(closing_price[i])

                final_closing_price = ''.join(final_closing_price)

                data.append(int(final_closing_price))
        
        return data
    except requests.RequestException as e:
        print(f"Request failed: {e}")



def get_date():

    data = []
    
    response = fetch_data("https://finance.yahoo.com/quote/BBRI.JK/history/")

    html_content = BeautifulSoup(response, 'html.parser')

    table = html_content.find("table", class_="noDl")

    table_body = table.find("tbody")
    
    rows = table_body.find_all("tr")

    for row in rows:
        cols = row.find_all('td')

        if len(cols) > 2:
            date = cols[0].text
            data.append(date)

    return data

print(get_stock_price_data('BBCA'))

