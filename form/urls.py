from django.urls import path
from form import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('courses/', views.courses, name='courses'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('counselling/', views.counselling, name='counselling'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('bba/', views.bba, name='bba'),
    path('bba1/', views.bba1, name='bba1'),
    path('bba2/', views.bba2, name='bba2'),
    path('bba3/', views.bba3, name='bba3'),
    path('bba4/', views.bba4, name='bba4'),
    path('bba5/', views.bba5, name='bba5'),
    path('bba6/', views.bba6, name='bba6'),      
    path('bba-edit/', views.bba_edit, name='bba_edit'),
    path('bba-preview/', views.bba_preview, name='bba_preview'),
    path('bcom/', views.bcom, name='bcom'),
    path('bcom1/', views.bcom1, name='bcom1'),
    path('bcom2/', views.bcom2, name='bcom2'),
    path('bcom3/', views.bcom3, name='bcom3'),
    path('bcom4/', views.bcom4, name='bcom4'),
    path('bcom5/', views.bcom5, name='bcom5'),
    path('bcom6/', views.bcom6, name='bcom6'),      
    path('bcom-edit/', views.bcom_edit, name='bcom_edit'),
    path('bcom-preview/', views.bcom_preview, name='bcom_preview'),
    path('bjmc/', views.bjmc, name='bjmc'),
    path('bjmc1/', views.bjmc1, name='bjmc1'),
    path('bjmc2/', views.bjmc2, name='bjmc2'),
    path('bjmc3/', views.bjmc3, name='bjmc3'),
    path('bjmc4/', views.bjmc4, name='bjmc4'),
    path('bjmc5/', views.bjmc5, name='bjmc5'),
    path('bjmc6/', views.bjmc6, name='bjmc6'),      
    path('bjmc-edit/', views.bjmc_edit, name='bjmc_edit'),
    path('bjmc-preview/', views.bjmc_preview, name='bjmc_preview'),
    path('ballb/', views.ballb, name='ballb'),
    path('ballb1/', views.ballb1, name='ballb1'),
    path('ballb2/', views.ballb2, name='ballb2'),
    path('ballb3/', views.ballb3, name='ballb3'),
    path('ballb4/', views.ballb4, name='ballb4'),
    path('ballb5/', views.ballb5, name='ballb5'),
    path('ballb6/', views.ballb6, name='ballb6'),      
    path('ballb-edit/', views.ballb_edit, name='ballb_edit'),
    path('ballb-preview/', views.ballb_preview, name='ballb_preview'),
    path('bballb/', views.bballb, name='bballb'),
    path('bballb1/', views.bballb1, name='bballb1'),
    path('bballb2/', views.bballb2, name='bballb2'),
    path('bballb3/', views.bballb3, name='bballb3'),
    path('bballb4/', views.bballb4, name='bballb4'),
    path('bballb5/', views.bballb5, name='bballb5'),
    path('bballb6/', views.bballb6, name='bballb6'),      
    path('bballb-edit/', views.bballb_edit, name='bballb_edit'),
    path('bballb-preview/', views.bballb_preview, name='bballb_preview'),
    path('eco/', views.eco, name='eco'),
    path('eco1/', views.eco1, name='eco1'),
    path('eco2/', views.eco2, name='eco2'),
    path('eco3/', views.eco3, name='eco3'),
    path('eco4/', views.eco4, name='eco4'),
    path('eco5/', views.eco5, name='eco5'),
    path('eco6/', views.eco6, name='eco6'),      
    path('eco-edit/', views.eco_edit, name='eco_edit'),
    path('eco-preview/', views.eco_preview, name='eco_preview'),
    path('llm/', views.llm, name='llm'),
    path('llm1/', views.llm1, name='llm1'),
    path('llm2/', views.llm2, name='llm2'),
    path('llm3/', views.llm3, name='llm3'),
    path('llm4/', views.llm4, name='llm4'),
    path('llm5/', views.llm5, name='llm5'),
    path('llm6/', views.llm6, name='llm6'),      
    path('llm-edit/', views.llm_edit, name='llm_edit'),
    path('llm-preview/', views.llm_preview, name='llm_preview'),  
]

urlpatterns += staticfiles_urlpatterns()


# path('pdfs/', views.pdfs, name='pdfs'),   
# we dont need a pdf view because 'pdfs/' shall only be accesible to admin and not to normal users