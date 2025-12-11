from django.shortcuts import render

from django.views import View

class SubscriptionView(View):

    template = 'subscriptions/subscription.html'

    def get(self,request,*args,**kwargs):

        return render(request,self.template)