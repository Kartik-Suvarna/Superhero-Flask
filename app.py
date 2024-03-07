from flask import Flask,render_template,request
import requests

app = Flask(__name__)



#id="ironman"
#response = requests.get("https://superheroapi.com/api/992742352183307/search/"+str(id)).json()

@app.route("/",methods=["POST","GET"])
def search():
    if request.method=="POST":
        name=request.form["search"]
        response = requests.get("https://superheroapi.com/api/992742352183307/search/"+str(name)).json()
        try:
            image=response["results"][0]["image"]['url']
            print(image)
            return render_template("base.html",image=image,name=name.upper())
        except:
            return "<h2> No Such Character exsists </h2>" 
    else :
        return render_template("base.html", image="",name="")