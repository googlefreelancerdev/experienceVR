import json
from flask import Flask,request,render_template,url_for
app=Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/image",methods=['POST'])
def image():
    if request.method == 'POST':
        name=request.form['user']
        email=request.form['email']
        useragent=request.headers.get("user-Agent")
        if request.headers.getlist("X-Forwarded-For"):
            ip=request.headers.getlist('X-Forwarded-For')
        else:
            ip=request.remote_addr
        ip=(','.join(ip))
        print(ip)
        file=open('data.txt','a')
        payload={
            "User ":name,
            "Email ":email,
            'UserAgent ':useragent,
            'IP ':ip
        }
        jsonobject=json.dumps(payload,indent=4)
        with open('data.json','a') as file:
            result=jsonobject+'\n'
            file.write(result)
        return render_template('image.html')
if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')