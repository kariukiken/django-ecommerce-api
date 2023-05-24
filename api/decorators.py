from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			if request.user.groups.exists():
				for group in request.user.groups.all():
					if group.name in allowed_roles:
						break
				else:
					return HttpResponse('[403] Not Authorised')

			return view_func(request, *args, **kwargs)
		return wrapper_func
	return decorator
