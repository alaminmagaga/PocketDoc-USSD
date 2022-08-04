from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON Welcome to Mexpert \n"
            # response .= "1. My Account \n"
            response += "1.Language\n"
            response+="2.Storage Facility\n"
            response+="3.Climate-Smart Agriculture\n"
            response+="4.Support\n"
         



        elif text == "1":
            response = "CON Select your preferred language\n"
            response +="1.Hausa\n"
            response +="2.Igbo\n"
            response +="3.Yoruba\n"
            response +="4.back\n"
        elif text=="2":
            response="CON Select Your State\n"
            response+="1.kaduna\n"
            response+="2.kano\n"
            response+="3.katsina\n"
        return HttpResponse(response)

