from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
import pyrebase
from django.conf import settings
import datetime as dt
import json
import uuid
from ringly.settings import config


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

"""
Error Handling Functions
"""

def handler404(request,va):
	return render(request, 'error/404.html')

def handler500(request):
	return render(request, 'error/404.html')
# Create your views here.


def login_page(request):
	template_name = 'login/login.html'
	if request.method == "POST":
		email = request.POST.get('email')
		passwd = request.POST.get('passwd')
		try:
			user = auth.sign_in_with_email_and_password(email,passwd)
			session_id = user['idToken']
			request.session['uid'] = session_id
			message = "Login Succesfull"
			return redirect('dashboard')
		except:
			message = "Something went wrong!!!"
	return render(request, template_name,locals())


def dashboard_page(request):
	"""user listing"""
	template_name = 'admin_panel/dashboard.html'
	token_id = request.session['uid']
	all_agents = dict(db.child("Users").get(token_id).val())
	all_agents_list = []
	return render(request, template_name,locals())

def create_user_page(request):
	template_name = 'admin_panel/user_create.html'
	token_id = request.session['uid']
	if request.method == 'POST':
		data = request.POST
		user_dict = {'userEmail': data.get('email',''), 'userId': data.get('mobile',0), 'userName': data.get('username','')}
		db.child('Users').push(user_dict,token_id)
		message = "Successfully added"
		return redirect('dashboard')
	return render(request,template_name)


def delete_obj(request,uid,key,url):
	token_id = request.session['uid']
	if key == "user":
		user_obj = db.child('Users').child(uid)
		user_obj.remove(token_id)
	elif key == "category":
		category_obj = db.child('ProductCategory').child(uid)
		category_obj.remove(token_id)
	
	return redirect(url)

def list_ringtone(request):
	token_id = request.session['uid']
	template_name = 'admin_panel/ringtones.html'
	all_ringtones = dict(db.child("Ringtone").get(token_id).val())
	return render(request, template_name,locals())
