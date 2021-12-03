from django.shortcuts import render,redirect
from .models import Customer


# Create your views here.
def home(request):
    #prods = Product.objects.all()
    #n=len(prods)
    #n_slides=(n//4)+ceil(n/4-(n//4))
    #range=range(1,n_slides)
    #context={'prods':prods,'n_slides':n_slides,'range':range(1,n_slides)}
    #allProds=[[prods,range(1,n_slides),n_slides],[prods,range(1,n_slides),n_slides]]
    # allProds=[]
    # cats=Product.objects.values('category','id')
    # final_cats={item['category'] for item in cats}
    # for cat in final_cats:
    #     prods=Product.objects.filter(category=cat)
    #     n = len(prods)
    #     n_slides = (n // 4) + ceil(n / 4 - (n // 4))
    #     allProds.append([prods,range(1,n_slides),n_slides])
    if request.method=='POST':
        email=request.POST.get('email','')
        cust=Customer(email=email)
        cust.save()
        return redirect('https://www.quora.com/') 
    return render(request,'babyfunnel/bridgepage.html')


def cbank(request):
    return render(request,'babyfunnel/cbank.html')