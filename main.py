from flask import Flask,render_template, redirect, url_for
import requests 
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("main.html")

@app.route("/mangalore")
def mangalore(data=None,name="Spice Paradise Mangalore"):
    #post-title entry-title
    res=requests.get("https://www.holidify.com/pages/food-in-mangalore-2051.html")
    soup=BeautifulSoup(res.text,"html.parser")
    heads=soup.select('.article h2')
    video=["https://www.youtube.com/watch?v=5OF5vcCdx6c&pp=ygUMR2Fzc2kgcmVjZWlw",
           "https://www.youtube.com/watch?v=-l_FdCXeZxA&pp=ygURR29saSBCYWpqaSByZWNlaXA%3D",
           "https://www.youtube.com/watch?v=iZqYjIRT0Kg&pp=ygURS29ycmkgUm90aSByZWNlaXA%3D",
           "https://www.youtube.com/watch?v=dt5vKZSP9do&pp=ygURR3VqamUgUG9kaSByZWNlaXA%3D",
           "https://www.youtube.com/watch?v=RcbkuD9ShCU&pp=ygUQIE1hbmRha2tpIHJlY2VpcA%3D%3D",
           "https://www.youtube.com/watch?v=bKFTrKTfKQs&pp=ygUUS2FkYWxlIE1hbm9saSByZWNlaXA%3D",
           "https://www.youtube.com/watch?v=jn8B3TpQH84&pp=ygUNU2Ftb3NhIHJlY2VpcA%3D%3D",
           "https://www.youtube.com/watch?v=EcnHCapZk6o&pp=ygUbU2VlciBGaXNoIE1hc2FsYSBGcnkgcmVjZWlw",
           "https://www.youtube.com/watch?v=7dV4Qw8qdsA&pp=ygUQT21lbGV0dGV5IHJlY2VpcA%3D%3D",
           "https://www.youtube.com/watch?v=xg7iNd0qkDM&pp=ygUZQ2hpY2tlbiBHaGVlIFJvYXN0IHJlY2VpcA%3D%3D",
           "https://www.youtube.com/watch?v=47fRmufjdQ4&pp=ygUVS2VyYWxhIFBhcm90dGEgcmVjZWlw",
           "https://www.youtube.com/watch?v=LrmNSksAYbE&pp=ygURQmFkYW0gTWlsayByZWNlaXA%3D",
           "https://www.youtube.com/watch?v=VtOsgR1mB_Q&pp=ygUYTWFuZ2Fsb3JlIEJpcnlhbmkgcmVjZWlw",
           "https://www.youtube.com/watch?v=mPeSfkpPCp0&pp=ygUXTWFuZ2Fsb3JlYW4gQnVucyByZWNlaXA%3D",
           "https://www.youtube.com/watch?v=nNC--lm6tTE&pp=ygUYUHJhd25zIGFuZCBDcmFic3MgcmVjZWlw"

           ]
    dict={}
    for i,j in zip(range(0,len(heads)),video):
        if i==15:
            break
        dict[heads[i].text]=j
    #return list
    return render_template("index.html",data=dict,name=name)

# @app.route("/shimoga")
# def shimoga(data=None,name="Shimoga"):
#     res=requests.get("https://superrlife.com/north-karnataka-foods/")
#     soup=BeautifulSoup(res.text,"html.parser")
#     heads=soup.select('.wp-block-heading')
#     list=[]
#     for i in range(1,len(heads)):
#         list.append(heads[i].text)
#     return render_template("index.html",data=list,name=name)

@app.route("/mysore")
def mysore(data=None,name="Royal Delights Mysore"):
    res=requests.get("https://superrlife.com/north-karnataka-foods/")
    soup=BeautifulSoup(res.text,"html.parser")
    heads=soup.select('h2')
    video=["https://www.youtube.com/watch?v=LTNVvmSZKj0","https://www.youtube.com/watch?v=ZL4WZZE-aGk&pp=ygURa29yaSBnYXNzaSByZWNpcGU%3D",
           "https://www.youtube.com/shorts/hXkuqVQ-aPc","https://www.youtube.com/watch?v=ChCbRH8lBQE&pp=ygUTYmlzaWJlbGViYXRoIHJlY2lwZQ%3D%3D",
           "https://www.youtube.com/watch?v=OXuH-G_-FDU&pp=ygUQa2hhcmFiYXRoIHJlY2lwZQ%3D%3D","https://www.youtube.com/watch?v=xXPiVFP-dO0&pp=ygURbXlzb3JlIHBhayByZWNpcGU%3D",
           "https://www.youtube.com/watch?v=NGwzOXaybKA&pp=ygUTbXlzb3JlIGJvbmRhIHJlY2lwZQ%3D%3D","https://www.youtube.com/watch?v=ftG4q-Wrzmc&pp=ygUQbmVlciBkb3NhIHJlY2lwZQ%3D%3D",
           "https://www.youtube.com/watch?v=We8Kdc0cWGA&pp=ygUScHVsaXlvZGhhcmEgcmVjaXBl","https://www.youtube.com/watch?v=dApl7nkaVqE&pp=ygUOdXR0YXBhbSByZWNpcGU%3D"]
    dict={}
    for i,j in zip(range(1,len(heads)-2),video):
        dict[heads[i].text]=j
    return render_template("index.html",data=dict,name=name)

@app.route("/bangalore")
def bangalore(data=None,name="Taste the flavors of Bangalore"):
    res=requests.get("https://www.bakingo.com/blog/famous-dishes-of-bangalore/")
    soup=BeautifulSoup(res.text,"html.parser")
    heads=soup.select('h2')
    video=["https://www.youtube.com/watch?v=BiO1SXyRAs4&pp=ygUOVXR0YXBhbSByZWNlaXA%3D",
           "https://www.youtube.com/watch?v=0q7zFaReQIY&pp=ygUWIE1hbmdhbG9yZSBCdW5zIHJlY2VpcA%3D%3D",
           "https://www.youtube.com/watch?v=bWbm_tRcZy8&pp=ygUaSWRsaSwgVmFkYSBhbmQgRG9zYSByZWNlaXA%3D",
           "https://www.youtube.com/watch?v=bj6tfGCiuJw&pp=ygUQIFZhZGEgUGF2IHJlY2VpcA%3D%3D",
           "https://www.youtube.com/watch?v=KuiT-FrJkCc&pp=ygUQUmF2YSBJZGxpIHJlY2VpcA%3D%3D",
           "https://www.youtube.com/watch?v=aEFvNsBDCWs&pp=ygUYQ2hvY28gY2hpcCBjdXBjYWtlcmVjZWlw",
           "https://www.youtube.com/watch?v=yWPQBHgAwuk&pp=ygURUHVsaXlvZ2FyZSByZWNlaXA%3D",
           "https://www.youtube.com/watch?v=B7C_5o6-9kc&pp=ygUNSG9saWdlIHJlY2VpcA%3D%3D",
           "https://www.youtube.com/watch?v=xWOtSgyymq0&pp=ygUjIEhhemVsbnV0IENob2NvbGF0ZSBKYXIgQ2FrZSByZWNlaXA%3D",
           "https://www.youtube.com/watch?v=ZZwtDwwOawM&pp=ygUSTWFzYWxhIHB1cmkgcmVjZWlw"]
    dict={}
    for i,j in zip(range(0,len(heads)),video):
        dict[heads[i].text]=j
    return render_template("index.html",data=dict,name=name)



@app.route("/coorg")
def coorg(data=None,name="Indulge in the flavors of Coorg"):
    response = requests.get('https://travel.earth/coorg-cuisine-famous-foods')
    soup = BeautifulSoup(response.text, "html.parser")
    heads = soup.select('h3>strong')
    video=["https://www.youtube.com/watch?v=9qWMmT8dPJU&pp=ygUpS2FkYW1idXR0dTogU3RlYW1lZCBSaWNlIER1bXBsaW5ncyByZWNlaXA%3D",
          "https://www.youtube.com/watch?v=i5XfXLUiG_E&pp=ygUTIFBhbmRpIEN1cnJ5IHJlY2VpcA%3D%3D",
           "https://www.youtube.com/watch?v=VlTLFgn5IZM&pp=ygUPIFBhcHV0dHUgcmVjZWlw",
            "https://www.youtube.com/watch?v=QhBRC1Gq8QM&pp=ygUQTm9vbHB1dHR1IHJlY2VpcA%3D%3D",
             "https://www.youtube.com/watch?v=O0190fgPx4o&pp=ygUQQWtraSBPdHRpIHJlY2VpcA%3D%3D",
               "https://www.youtube.com/watch?v=fk7YLVNQvsg&pp=ygUbIEtha2thZGEgTnllbmQgQ3VycnkgcmVjZWlw",
               "https://www.youtube.com/watch?v=vlZ9eO7I03k&pp=ygUVQmFpbWJhbGUgQ3VycnkgcmVjZWlw",
               "https://www.youtube.com/watch?v=EOODS8oFn7g&pp=ygUTIEt1bW11IEN1cnJ5IHJlY2VpcA%3D%3D",
               "https://www.youtube.com/watch?v=2xiwUnEuewQ&pp=ygUTTWFhbmdlIEN1cnJ5IHJlY2VpcA%3D%3D",
               "https://www.youtube.com/watch?v=adibLW8Qroo&pp=ygUTS29vdmFsZXB1dHR1IHJlY2VpcA%3D%3D",
               "https://www.youtube.com/watch?v=_7KeY_GClfI&pp=ygURIFRoYW1idXR0dSByZWNlaXA%3D"]
    dict={}
    for i,j in zip(range(0,len(heads)),video):
        dict[heads[i].text]=j
    return render_template("index.html",data=dict,name=name)


@app.route("/kannada")
def kannada(data=None,name="Coastal Feas Uttar Kannada"):
    response = requests.get('https://superrlife.com/north-karnataka-foods')
    soup = BeautifulSoup(response.text, "html.parser")
    heads = soup.select('h2>strong')
    video=["https://www.youtube.com/watch?v=GvfQHrm64dM&pp=ygUTSm9sYWRhIFJvdHRpIHJlY2VpcA%3D%3D","https://www.youtube.com/watch?v=U9eSvIzvH48&pp=ygUUTWVudGhlIEthZHVidSByZWNlaXA%3D",
           "https://www.youtube.com/watch?v=4Mi1moPIlpI&pp=ygUbR2lybWl0L1ZhZ2dhbmkvU3VzbGEgcmVjZWlw",
          "https://www.youtube.com/watch?v=8JgFjnRXBOI&pp=ygUfTWlyY2hpIEJhamppLyBDdXQgTWlyY2hpIHJlY2VpcA%3D%3D",
            "https://www.youtube.com/watch?v=0JgCGj8-YUI&pp=ygUPRW5uZWdheWkgcmVjZWlw", "https://www.youtube.com/watch?v=mVFQmHA6UzQ&pp=ygUYSmF2YWxpa2FheWkgUGFseWEgcmVjZWlw",
           "https://www.youtube.com/watch?v=2TpuoScxN28&pp=ygUMSnVua2EgcmVjZWlw", "https://www.youtube.com/watch?v=kwijfK_0njs&pp=ygUiU29wcGluYSBQYWx5YSAmIEthYWx1IFBhbHlhIHJlY2VpcA%3D%3D",
           "https://www.youtube.com/watch?v=LwWb--iuCHg&pp=ygUnRGlmZmVyZW50IHR5cGVzIG9mIENodXRuZXkgUHVkaXMgcmVjZWlw",
          "https://www.youtube.com/watch?v=aGDQJzRtCEU&pp=ygUUU2hlbmdhIEhvbGlnZSByZWNlaXA%3D",
           "https://www.youtube.com/watch?v=GownjDBmbWg&pp=ygUUIERoYXJ3YWQgUGVkYSByZWNlaXA%3D",
            ]
    dict={}
    for i,j in zip(range(1,len(heads)),video):
        dict[heads[i].text]=j
    return render_template("index.html",data=dict,name=name)


# @app.route("/Mangalore")
# def button_click():
#     # Handle button click logic here
#     return redirect(url_for("mangalore"))


app.run()