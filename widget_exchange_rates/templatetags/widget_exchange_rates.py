from django import template
from ..models import Rate
import xml.etree.cElementTree as etree
import os

register = template.Library()

@register.inclusion_tag('exchange_rates.html')
def get_exchange_rates():

    fileDirName = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(fileDirName,"../external_sources/rates.xml");

    xmlDoc = open(path,"r")
    xmlDocData = xmlDoc.read()
    xmlDocTree = etree.XML(xmlDocData)


    rates = []

    visibleRates = Rate.objects.all().filter(visible=True)
    visibleRatesNames = []
    for vr in visibleRates:
        visibleRatesNames.append(vr.currency)

    for rate in xmlDocTree.iter("pozycja"):
        vals = []
        if rate[2].text in visibleRatesNames:
            vals.append(rate[1].text + " " + rate[2].text)
            vals.append(rate[3].text)
            rates.append(vals)
    return {'rates': rates}
