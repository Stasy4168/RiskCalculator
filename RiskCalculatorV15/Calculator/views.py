from django.shortcuts import render
from django.views import View
from .forms import AssetsForm
import operator
from .models import AssetsModel

# Create your views here.


class Index(View):
    def get(self,request):
        form = AssetsForm()
        return render(request, 'Calculator/index.html', {'form': form})

    def post(self,request):
        form = AssetsForm(request.POST)

        if form.is_valid():
            
            portfolio = ["высокий", "низкий", "средний"]

            interest_rate = form.cleaned_data['interest_rate']
            dividend = form.cleaned_data['dividend_stock'] 
            growth = form.cleaned_data['growth_stock'] 
            bond = form.cleaned_data['state_bond'] 
            floater = form.cleaned_data['corporate_floater'] 
            gld = form.cleaned_data['gold'] 
            form.save()

            # total investment
            total_investment = dividend + growth + bond + floater + gld
            
            #gain
            gain_dividend = (dividend*15)/100
            gain_growth = (growth*50/100)
            gain_bond = (bond*(interest_rate-5)/100)
            gain_floater = (floater*(interest_rate+2)/100)
            gain_gold = (gld*10/100)

            total_gain = gain_dividend + gain_growth + gain_bond + gain_floater + gain_gold
            total_gain = round(total_gain, 3)

            # # risk
            risk_dividend = (dividend*-10)/100
            risk_growth = (growth*-20/100)
            risk_bond = (bond*(-1)/100)
            risk_floater = (floater*(-15)/100)
            risk_gold = (gld*-3/100)

            total_risk = risk_dividend + risk_growth + risk_bond + risk_floater + risk_gold
            total_risk = round(total_risk,3)

            # not enough assets risk
            assets = [dividend, growth, bond, floater, gld]
            empty = operator.countOf (assets,0)
            if empty >= 3:
                scarce = (5- empty)
            else: 
                full = (5-empty)
                scarce = full

             # gain and risk percentage 
            try:
                gain_percentage = (total_gain*100/total_investment)
            except ZeroDivisionError:
                gain_percentage = 0


            try:
               risk_percentage = (total_risk*100/total_investment)
            except ZeroDivisionError:
                risk_percentage = 0


            try:
                gain_percentage = round(gain_percentage,2)
            except ZeroDivisionError:
                gain_percentage = 0


            try:
                risk_percentage = round(risk_percentage,2)
            except ZeroDivisionError:
                risk_percentage = 0

            # portfolio profile calculation
            if risk_percentage <= -15:
                profile = portfolio[0]
            elif risk_percentage >= -5:
                profile = portfolio[1]
            else:
                profile = portfolio[2]
            

            # create context
            context = {
                'dividend': int(dividend),
                'growth': int(growth),
                'bond': int(bond),
                'floater': int(floater),
                'gld': int(gld),
                'total_investment': total_investment,
                'total_gain': total_gain,
                'total_risk': total_risk,
                'scarce': scarce,
                'profile': profile,
            }
            
        
         # render the template
        return render(request, 'Calculator/result.html', context)