from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from flowersapp.models import Bouquet, Buyer
from flowersapp.models import Consultation, Order
from flowersapp.bot import tg_send_message


@csrf_exempt
def index(request):
    recommended_bouquets = Bouquet.objects.filter(recommend=True)

    if request.method == 'POST':
        full_name = request.POST.get('fname')
        phonenumber = request.POST.get('tel')

        buyer, created = Buyer.objects.get_or_create(
            phonenumber=phonenumber,
            defaults={
                'full_name': full_name},
        )
        Consultation.objects.create(
            full_name=full_name,
            phonenumber=phonenumber,
        ).buyer.set([buyer])
        tg_send_message(full_name, phonenumber)

    return render(
        request, 'index.html', context={'bouquets': recommended_bouquets}
        )


def card(request, bouquet_url):
    bouquet = get_object_or_404(Bouquet, slug=bouquet_url)
    return render(request, 'card.html', context={'bouquet': bouquet})


def catalog(request):
    bouquets = Bouquet.objects.all()
    return render(request, 'catalog.html', context={'bouquets': bouquets})


@csrf_exempt
def consultation(request):
    if request.method == 'POST':
        full_name = request.POST.get('fname')
        phonenumber = request.POST.get('tel')

        buyer, created = Buyer.objects.get_or_create(
            phonenumber=phonenumber,
            defaults={
                'full_name': full_name},
        )
        Consultation.objects.create(
            full_name=full_name,
            phonenumber=phonenumber,
        ).buyer.set([buyer])
        main(full_name, phonenumber)

    return render(request, 'consultation.html')


@csrf_exempt
def order(request, slug):
    if request.method == "POST":
        full_name = request.POST.get('fname')
        phonenumber = request.POST.get('tel')
        address = request.POST.get('adres')
        delivery_time = request.POST.get('orderTime')

        bouquet, created = Bouquet.objects.get_or_create(id=slug)
        buyer, created = Buyer.objects.get_or_create(
            phonenumber=phonenumber,
            defaults={
                'full_name': full_name,
                'address': address
            },
        )
        Order.objects.create(
            buyer=buyer,
            delivery_time=delivery_time,
            bouquet=bouquet
        )
    return render(request, 'order.html')


def order_step(request):
    return render(request, 'order-step.html')


def quiz(request):
    return render(request, 'quiz.html')


def quiz_step(request):
    return render(request, 'quiz-step.html')


def result(request):
    return render(request, 'result.html')
