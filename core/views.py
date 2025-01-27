from django.shortcuts import render
from django.views.generic import TemplateView
import urllib3
from bs4 import BeautifulSoup

from core.models import MetalBidPrice


# Create your views here.
def home(request):
    ask_price_list, bid_price_list = sol()

    context = {
        "materials": ["Alum", "Lead", "Cobalt"],
        "ask_price_list": ask_price_list,
        "bid_price_list": bid_price_list,
    }
    return render(request, "core/home.html", context=context)


def sol():

    http = urllib3.PoolManager(cert_reqs="CERT_NONE")

    url = "https://www.metalsmarket.net/w_lmeCashSett.html"
    response = http.request("GET", url)
    # response = requests.get(url)
    soup = BeautifulSoup(response.data, "html.parser")

    # Find ALUM bid and ask values
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

    print(f"ALUM - Bid: {alum_bid}, Ask: {alum_ask}")
    print(f"LEAD - Bid: {lead_bid}, Ask: {lead_ask}")
    print(f"COBALT - Bid: {cobalt_bid}, Ask: {cobalt_ask}")

    bid_price_list = []
    bid_price_list.append(float(alum_bid))
    bid_price_list.append(float(lead_bid))
    bid_price_list.append(float(cobalt_bid))

    ask_price_list = []
    ask_price_list.append(float(alum_ask))
    ask_price_list.append(float(lead_ask))
    ask_price_list.append(float(cobalt_ask))

    metals = ["Alum", "Lead", "Cobalt"]

    for i, metal in enumerate(metals):
        MetalBidPrice.objects.create(material=metal, bid_price=bid_price_list[i])

    db_racords = MetalBidPrice.objects.all()
    print(db_racords.count())

    for record in db_racords:
        print(record.material, record.bid_price, record.created_at)

    return ask_price_list, bid_price_list


def something_cool(request):
    """This function does something.

    :param arg1: The first argument.
    :param arg2: The second argument.
    :return: The result of the operation.
    """
    # Do something
    context = {
        "test": "something_cool",
    }
    return render(request, "core/something_cool.html", context=context)


class SomethingCoolView(TemplateView):
    template_name = "something_cool.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Something Cool View"
        context["page_title"] = title
        return context
