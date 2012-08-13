from django.shortcuts import render, redirect
from django.contrib import messages

from honeypot.decorators import check_honeypot

from rsvp.forms import GuestForm


@check_honeypot()
def rsvp(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
                                 'Thanks for your RSVP!')
            return redirect('rsvp')
    else:
        form = GuestForm()
    context = {'form': form}
    return render(request, "rsvp/rsvp.html", context)
