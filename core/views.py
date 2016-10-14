from django.shortcuts import render

# Create your views here.



from core.models import TemperatureLog
from django.shortcuts import get_object_or_404, render_to_response



def index(request):
    query_result = TemperatureLog.objects.all()
    context = {'query_result': query_result}
    return render(request, 'core/index.html',context)



def chart(request):
    query_result = TemperatureLog.objects.all()
    context = {'query_result': query_result}
    return render(request, 'core/chart.html',context)




