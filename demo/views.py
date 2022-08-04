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
            response = "CON Barka da zuwa  Mexpert \n"
            # response .= "1.My Account \n"
            response += "1.Harshe\n"
            response+="2.Wurin ajiya\n"
            response+="3.Yanayi- Noma Mai Wayo\n"
            response+="4.Taimako\n"
         



        elif text == "1":
            response = "CON Zaɓi harshen da kuka fi so\n"
            response +="1.Hausa\n"
            response +="2.Igbo\n"
            response +="3.Yoruba\n"
            response +="4.baya\n"
        elif text=="2":
            response="CON Zaɓi Jihar ku\n"
            response+="1.kaduna\n"
            response+="2.kano\n"
            response+="3.katsina\n"
            response +="4.baya\n"
        elif text=="2*1":
            response="CON Zaɓi Karamar hukuma \n"
            response+="1.Lere\n"
            response+="2.Zaria\n"
            response+="3.Kafancan\n"
            response +="4.gaba\n"
        elif text=="2*1*1":
            response="END muna taya murna Zamu hadaka da wakilin mu nanda minti 30,Mun gode \n"
           
            
        return HttpResponse(response)

