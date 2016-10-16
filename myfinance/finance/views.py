from django.shortcuts import render
from django.http import HttpResponse
from finance.controller import Account
from finance.controller import Charge
from finance import controller


def home(request):
    home_page = open('finance\\home\\home.html', 'r')
    response = home_page.read()
    return HttpResponse(response)


def random_account(request):
    account = controller.random_account()
    first = open('finance\\table\\first.html', 'r')
    response = first.read()
    end = open('finance\\table\\end.html', 'r')
    for i in account:
        response += '<tr><td>{0}</td>'.format(i.value())
        response += '<td>{0}</td></tr>'.format(i.cause())

    response += '</tbody></table></div>'
    response += '<div class="container"><p style="text-align:right"><b>Your total: {0}</p></div>'.format(account.get_total())
    response += '<div class="control-group"><p style="text-align:center"><a class="btn btn-primary btn-lg" href="../" role="button">Home</a></p></div>'

    response += end.read()
    return HttpResponse(response)


# Create your views here.
