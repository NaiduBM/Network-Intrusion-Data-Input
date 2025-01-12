from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import sklearn 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

# Create your views here.

def manoj(request):
    if request.method == "POST":
        data = request.POST  # Define data here
        a = int(data.get('a1'))  # Correct the key name and add missing quote
        b = int(data.get('a2'))
        c = int(data.get('a3'))
        d = int(data.get('a4'))
        e = int(data.get('a5'))
        f = int(data.get('a6'))
        h = int(data.get('a7'))
        i = int(data.get('a8'))
        j = int(data.get('a9'))
        k = int(data.get('a10'))
        l = int(data.get('a11'))
        m = int(data.get('a12'))
        n = int(data.get('a13'))
        o = int(data.get('a14'))
        p = int(data.get('a15'))
        q = int(data.get('a16'))
        r = int(data.get('a17'))
        s = int(data.get('a18'))
        t = int(data.get('a19'))
        u = int(data.get('a20'))
        v = int(data.get('a21'))
        w = int(data.get('a22'))
        x = int(data.get('a23'))
        y1 = int(data.get('a24'))
        z = int(data.get('a25'))
        ab = int(data.get('a26'))
        ac = int(data.get('a27'))
        ad = int(data.get('a28'))
        ae = int(data.get('a29'))
        af = int(data.get('a30'))
        ai = int(data.get('a31'))
        
        path="C:\\Users\\Manoj BM\\OneDrive\\Desktop\\Karunadu\\ml\\manoj.csv"
        data = pd.read_csv(path)
        inputs=data.drop('a32','columns')
        output=data.drop(['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13','a14','a15','a16','a17','a18','a19','a20','a21','a22','a23','a24','a25','a26','a27','a28','a29','a30','a31'],'columns')
        import sklearn
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)
        
        from sklearn.linear_model import LogisticRegression
        model=LogisticRegression()
        model.fit(x_train,y_train)
        y_pred=model.predict(x_test)
        
        from sklearn.metrics import confusion_matrix
        cm=confusion_matrix(y_test,y_pred)

        if('predict' in request.POST):
            result=model.predict([[ a,b,c,d,e,f,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y1,z,ab,ac,ad,ae,af,ai ]])
           
            if result==[0]:
                info="Normal "
            elif result==[1]:
                info="Blackhole "
            elif result==[2]:
                info="TCP-SYN"
            elif result==[3]:
                info="PortScan"
            elif result==[4]:
                info="Diversion "
           
            else:
                info="Overflow "
           
        

        return render(request, "manoj1.html", context={'info': info})

    return render(request, 'manoj1.html')