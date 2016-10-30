from flask import Flask,render_template,request
from fpdf import FPDF
import base64
import string
import random
#import cv2
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/PerformInvert',methods=['GET','POST'])
def InvertFile():
	pdf=FPDF()
	for val in request.json:
		name=id_generator();
		g = open(name+".png", "wb")
		g.write(base64.decodestring(val))
		g.close()
		#tempImage=cv2.imread(name+".png",cv2.IMREAD_GRAYSCALE)
		#res,invert=cv2.threshold(tempImage,0,255,cv2.THRESH_TOZERO)		
		#newImg=(255-invert)
		pdf.add_page()
		pdf.image(name+".png",50,50,100,100)
	pdf.output(name+".pdf","F")
	return name+".pdf",200
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
   app.run(debug=True)