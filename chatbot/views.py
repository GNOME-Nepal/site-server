from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils.chat import chatbot_response  

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            text = data.get("message", "")

            if not text:
                return JsonResponse({"error": "Empty message"}, status=400)

            response = chatbot_response(text)
            return JsonResponse({"answer": response})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, "chatbot.html")