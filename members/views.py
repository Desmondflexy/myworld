from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Member


# Create your views here.


def index(request):
    mymembers = Member.objects.all()
    context = {
        'mymembers': mymembers,
        'length': len(mymembers),
    }
    return render(request, 'members/index.html', context)


def add(request):
    # Opens add new member page
    return render(request, 'members/add.html')


def addRecord(request):
    # Gets the firstname and lastname with the request.POST statement.
    x = request.POST['firstname']
    y = request.POST['lastname']
    # Adds a new record to the members table.
    member = Member(firstname=x, lastname=y)
    member.save()
    # Redirects the user back to the index page.
    return HttpResponseRedirect(reverse('members:index'))


def details(request, id):
    # member detialed view
    member = Member.objects.get(id=id)
    context = {
        'id': id,
        'firstname': member.firstname,
        'lastname': member.lastname,
    }
    return render(request, 'members/details.html', context)


def update(request, id):
    # update member details
    member = Member.objects.get(id=id)
    context = {
        'firstname': member.firstname,
        'lastname': member.lastname,
    }
    return render(request, 'members/update.html', context)


def updateRecord(request, id):
    ## update button (confirm update)
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    return HttpResponseRedirect(reverse('members:index'))

def delete(request, id):
    ## delete button
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('members:index'))
