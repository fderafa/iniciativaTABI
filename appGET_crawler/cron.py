from django_cron import CronJobBase, Schedule
from django.shortcuts import render
from .templates import mamboView

class mamboCronJob(CronJobBase):
    """Classe para execucao automatica"""
    RUN_EVERY_MINS = 5  #>>> tempo de execucao a cada 5 minutos
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'getCrawler' #>> nome do schedulle

    def do(self):
            mamboView(None)
