from django.shortcuts import render_to_response

def success_order(request):
    return render_to_response("sucess.html")

def cancel_order(request):
    return render_to_response("cancel.html")  
