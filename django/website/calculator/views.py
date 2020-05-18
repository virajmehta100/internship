from django.shortcuts import render

# Create your views here.
def calories_calculator(request):
    return render(request,'calculator/calculator.html')
