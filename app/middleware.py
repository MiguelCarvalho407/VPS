from datetime import date
from django.shortcuts import redirect
from .models import *
from django.urls import resolve

# def regime_inicio_mes(get_response):
#     def middleware(request):
#         if request.user.is_authenticated:
#             today = date.today()
#             regime_data = getattr(request.user, 'regime_data', None)

            
#             if today.day == 1 or not regime_data:
#                 if not regime_data or (regime_data.year != today.year or regime_data.month != today.month):
#                     if request.path != '/escolher-regime/':
#                         return redirect('escolher_regime')

#         return get_response(request)
#     return middleware


def regime_inicio_mes(get_response):
    def middleware(request):
        if request.user.is_authenticated:
            today = date.today()
            regime_data =  request.user.regime_data

            if (today.day == 1 or not regime_data or regime_data.year != today.year or regime_data.month != today.month):
                current_url = resolve(request.path_info).url_name
                if current_url != 'escolher_regime':
                    return redirect('escolher_regime')
        
        return get_response(request)
    return middleware

