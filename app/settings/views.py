from django.shortcuts import render, redirect
from app.settings.models import Settings, Info, About, AboutMe, Works, Contact
from django.core.mail import send_mail


def index(request):
    settings_id = Settings.objects.latest("id")
    info_all = Info.objects.all()
    about = About.objects.latest("id")
    aboutme = AboutMe.objects.all()
    work_all = Works.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        send_mail(
            'Geeks',
            f"""
            Здраствуйте.
            Спасибо за обратный связ, мы скоро с  вами свяжимся.
            Ваше Имя " {name},
            Ваш почта: {email}
            ваш номер телефона : {phone}
            ваш объект: {subject}
            ваше сообщение: {message}
                                    """,
            "noreply@somehost.local",
            ["nurlanuuulubeksultan@gmail.com"]
        )
        Contact.objects.create(name=name, email=email,phone=phone, subject=subject, message=message)
        return redirect("http://127.0.0.1:4000/admin/settings/works/")

    return render(request, "index.html", locals())