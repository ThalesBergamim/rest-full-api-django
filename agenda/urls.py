from django.urls import include, path

from agenda.views import agendamento_detail, agendamentos_list

urlpatterns = [
    path('agendamentos/', agendamentos_list),
    path('agendamentos/<int:id>/', agendamento_detail)
]
