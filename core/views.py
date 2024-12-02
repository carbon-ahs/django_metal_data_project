from django.shortcuts import render
from django.views.generic import TemplateView
import urllib3
from bs4 import BeautifulSoup


# Create your views here.
def home(request):
    sol()

    context = {
        "test": "TEST",
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
