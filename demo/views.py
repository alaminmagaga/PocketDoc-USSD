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
            response = "CON CON Welcome to Sports News subscription service  \n"
            response += "1. Football \n"
            response += "2. Tennis\n"
            response += "3. Volley Ball \n"
            response += "4. Rugby \n"

        elif text == "1":
            response = "CON Select Your Preferred football Plans \n"
            response += "1. Daily @ N100 \n"
            response += "2. Weekly @ N50 \n"
            response += "3. Monthly @ N25 "

        elif text=="2":
            response = "CON You will be charged N100 for your Daily Football news \n"
            response += "1. Auto-Renewal \n"
            response += "2. One-off Purchase \n"

        elif text == "1*1*1":   
            response = "END thank you for subscribing to our daily football news plan \n"

        elif text == "1*1*2":     #one off
            response = "END thank you for your one-off daily football news plan \n"  
  
        elif text == "1*2":      #weekly football
            response = "CON You will be charged N50 for our weekly Sports news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "1*2*1":
            response = "END thank you for subscribing to our weekly football news plan \n"

        elif text == "1*2*2":
            response = "END thank you for your one-off weekly football news plan \n"    
    
        elif text == "1*3":
            response = "CON You will be charged N25 for our monthly football news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"
         
        elif text == "1*3*1":
            response = "END thank you for subscribing to our monthly football news plan \n"
    
        elif text == "1*3*2":
            response = "END thank you for your one-off monthly football news plan \n"


        return HttpResponse(response)

