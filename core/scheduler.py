import datetime
from locale import currency

from bs4 import BeautifulSoup
import urllib3


def your_job_function():
    # put your scheduled task code here
    print(
        "Scheduler is running! <your_job_function> ||"
        + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


def scrap_data_from_metal_market():
    """
    Scraps data from Metal Market
    """
    http = urllib3.PoolManager(cert_reqs="CERT_NONE")

    url = "https://www.metalsmarket.net/w_lmeCashSett.html"
    response = http.request("GET", url)
    soup = BeautifulSoup(response.data, "html.parser")

    # Find Currency And Date
    currency_td = soup.find("td", text="USD")
    date_td = currency_td.find_next_sibling()

    currency_value = currency_td.text.strip()
    date_value = date_td.text.strip()

    # Find ALUMINIUM bid and ask values
    alum_bid = soup.find("td", text="ALUM").find_next_sibling().text
    alum_ask = soup.find("td", text="ALUM").find_next_sibling().find_next_sibling().text

    # Find LEAD bid and ask values
    lead_bid = soup.find("td", text="LEAD").find_next_sibling().text
    lead_ask = soup.find("td", text="LEAD").find_next_sibling().find_next_sibling().text

    # Find COBALT bid and ask values
    cobalt_bid = soup.find("td", text="COBALT").find_next_sibling().text
    cobalt_ask = (
        soup.find("td", text="COBALT").find_next_sibling().find_next_sibling().text
    )

    # Find Aluminum Alloy bid and ask values
    aluminum_alloy_bid = soup.find("td", text="A.ALLY").find_next_sibling().text
    aluminum_alloy_ask = (
        soup.find("td", text="A.ALLY").find_next_sibling().find_next_sibling().text
    )

    # Find ZINC bid and ask values
    zinc_bid = soup.find("td", text="ZINC").find_next_sibling().text
    zinc_ask = soup.find("td", text="ZINC").find_next_sibling().find_next_sibling().text

    # Find NICKEL bid and ask values
    nickel_bid = soup.find("td", text="NICKEL").find_next_sibling().text
    nickel_ask = (
        soup.find("td", text="NICKEL").find_next_sibling().find_next_sibling().text
    )

    # Find Copper bid and ask values
    copper_bid = soup.find("td", text="COPPER").find_next_sibling().text
    copper_ask = (
        soup.find("td", text="COPPER").find_next_sibling().find_next_sibling().text
    )

    print(f"Currency: {currency_value}, Date: {date_value}")
    print(f"ALUM - Bid: {alum_bid}, Ask: {alum_ask}")
    print(f"LEAD - Bid: {lead_bid}, Ask: {lead_ask}")
    print(f"COBALT - Bid: {cobalt_bid}, Ask: {cobalt_ask}")
    print(f"Aluminum Alloy - Bid: {aluminum_alloy_bid}, Ask: {aluminum_alloy_ask}")
    print(f"ZINC - Bid: {zinc_bid}, Ask: {zinc_ask}")
    print(f"NICKEL - Bid: {nickel_bid}, Ask: {nickel_ask}")
    print(f"COPPER - Bid: {copper_bid}, Ask: {copper_ask}")

    # bid_price_list = []
    # bid_price_list.append(float(alum_bid))
    # bid_price_list.append(float(lead_bid))
    # bid_price_list.append(float(cobalt_bid))

    # ask_price_list = []
    # ask_price_list.append(float(alum_ask))
    # ask_price_list.append(float(lead_ask))
    # ask_price_list.append(float(cobalt_ask))

    # metals = ["Alum", "Lead", "Cobalt"]

    # for i, metal in enumerate(metals):
    #     MetalBidPrice.objects.create(material=metal, bid_price=bid_price_list[i])

    # db_racords = MetalBidPrice.objects.all()
    # print(db_racords.count())

    # for record in db_racords:
    #     print(record.material, record.bid_price, record.created_at)

    pass
