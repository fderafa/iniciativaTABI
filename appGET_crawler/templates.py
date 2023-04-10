from django.shortcuts import render
from django.http import HttpResponse
from .views import clsMambo

def mamboView(request):
    """metodo que é executado a cada n intervalo de tempo e retorna todos os acessos por clientes"""
    methodsMambo = clsMambo(request)    #>>> inicializa a classe
    lRefId = methodsMambo.getAttributeGuest()  #>>> resgata se houve acesso de algum visitante
    if lRefId:
        methodsMambo.postCrawlerExecute(lRefId) #>>> atualiza o controle de execucao (crawler)
        tuple = methodsMambo.getAttributeAccess(lRefId)    #>>> havendo, resgata os devices e os ids
        if tuple[0]: methodsMambo.getAttributeAccessPoints(tuple[0])   #>>> havendo, resgata os access point
        if tuple[1]: methodsMambo.getAttributeGuestDevices(tuple[1])   #>>> havendo, resgata o device utilizado
        return HttpResponse(f'aqui é sucesso: {lRefId}')
    else:
        return HttpResponse(f'nao achou ninguem')
    
def mamboBacklog(request):
    """metodo que é executado a cada intervalo de tempo e retorna e atualiza o backlog de conexoes nao encerradas"""
    methodsMambo = clsMambo(request)    #>>> inicializa a classe
    lBackLogRefId = methodsMambo.AccessBacklog()
    if lBackLogRefId: methodsMambo.getAttributeAccess(lBackLogRefId)
    return HttpResponse(lBackLogRefId)