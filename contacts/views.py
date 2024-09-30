from django.shortcuts import render, HttpResponseRedirect

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template

# from django.core.mail import send_mail

from .forms import ContactForm


# version-2
def contacts(request):
    context = {'title': 'Контакты'}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = {'name': form.cleaned_data['name'],
                    'email': form.cleaned_data['email'],
                    # 'subject': form.cleaned_data['subject'],
                    'message': form.cleaned_data['message'], }

            html_content = render_to_string("contacts/message.html", data)
            msg = EmailMultiAlternatives(subject=form.cleaned_data['subject'], to=['mister.makss2000@gmail.com', ])
            msg.attach_alternative(html_content, 'text/html')
            mail = msg.send()
            if mail:
                context = {'success': 1}
    else:
        form = ContactForm()

    context['form'] = form

    return render(request, 'contacts/contact.html', context)
