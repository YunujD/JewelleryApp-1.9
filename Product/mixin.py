from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.contrib.admin.views.decorators import staff_member_required   #for staff required


class LoginRequiredMixin(object):
	@classmethod
	def as_view(self,*args,**kwargs):
		view=super(LoginRequiredMixin,self).as_view(*args,**kwargs)                   #anything having as_view in url.py will be effected
		return login_required(view)

	@method_decorator(login_required)              
	def dispatch(self,request,*args,**kwargs):
		return super(LoginRequiredMixin,self).dispatch(request,*args,**kwargs)               #redirected to login page

