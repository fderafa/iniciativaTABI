import requests
from datetime import datetime
from .models import tGuests, tNextCrawlerExecute, tAccess, tAccessPoint, tDevices
from personalID_project.middleware import ErrorMiddleware


class clsMambo():
    def __init__(self, request):
        """metodo construtor da classe"""
        self.nextLink = 'InitLink'
        self.dateFrom = tNextCrawlerExecute.lastDateExecute()  #>>> Captura a data da ultima execucao que retornou valor
        self.dateTo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.dominio = 'https://testesprodutoux.mambowifi.com/api/'
        self.request = request

    def getAttributeGuest(self):
        """metodo que captura os visitantes de acordo com o tempo agendado"""
        lGuests = []
        while self.nextLink:
            if self.nextLink == 'InitLink': url = f'{self.dominio}v2/guests?filter=lastAccess&from={self.dateFrom}&to={self.dateTo}'
            else: url = f'{self.dominio}v2/guests?nextToken={self.nextLink}'
            tmpJson = self.allGetPost(url, 'get')
            if isinstance(tmpJson, dict):   #>>> verifica se o retorno é um dicionario (json)
                if tmpJson['elements']: #>>> verifica se houve retorno de visitantes
                    for vElements in tmpJson['elements']:
                        lGuests.append(vElements['id'])
                        tGuests.saveGuest(vElements['properties']['document'], vElements['id'], vElements)
                self.nextLink = tmpJson['nextLink']
            else:
                ErrorMiddleware.process_exception(self, tmpJson, url)
                self.nextLink = None
        return lGuests
    
    def postCrawlerExecute(self, lGuests):
        """metodo que registra execucao do crawler"""
        tNextCrawlerExecute.saveCrawlerExecute(self.dateTo, len(lGuests)) #>>> grava a data/hora da ultima execucao q retornou visitantes
        
    def getAttributeGuestDevices(self, refId):
        """metodo que retornara o device do acesso que ele esta usando na conexao atual"""
        for i in range(len(refId)):
            url = f'{self.dominio}v2/guests/{refId[i]}/devices'
            tmpJson = self.allGetPost(url, 'get')
            if isinstance(tmpJson, dict):
                tDevices.saveDevice(refId[i], tmpJson['mac_address'], tmpJson)
            else:
                ErrorMiddleware.process_exception(self, tmpJson, url)    

    def getAttributeAccess(self, refId):
        """metodo que captura os acessos dos visitantes"""
        lAccess = []
        lAccessPoint = []
        ids = ''
        for i in range(len(refId)):
            ids = ids + str(f'ids={refId[i]}&')
        url = f'{self.dominio}access-by-ids?{ids}'
        tmpJson = self.allGetPost(url, 'post')
        if isinstance(tmpJson, dict):   #>>> verifica se o retorno é um dicionario (json)
            if tmpJson['data']: #>>> verifica se houve retorno de acessos para os visitantes retornados
                for vData in tmpJson['data']:
                    lAccessPoint.append(vData['id'], vData['identifier'])    #>>> identificador do Access Point do acesso concatenado com o refid
                    lAccess.append(vData['id']) #>>> id do acesso
                    if vData['stop']:   #>>> se nao houver hora de desconexao, tratar no backlog
                        tAccess.saveAccess(vData['id'], vData)
                    else:
                        tAccess.saveAccess(vData['id'],False, vData)    #>>> casos que serao tratados como backlog
        else:
            ErrorMiddleware.process_exception(self, tmpJson, url)
        return lAccessPoint, lAccess
    
    def getAttributeAccessPoints(self, lAccessPoint):
        """metodo que retorna o ponto de acesso utilizado"""
        for i in range(len(lAccessPoint)):
            url = f'{self.dominio}access-points?identifier={lAccessPoint(i, 1)}'
            tmpJson = self.allGetPost(url, 'get')
            if isinstance(tmpJson, dict):
                tAccessPoint.saveAccessPoint(lAccessPoint(i, 0), lAccessPoint(i, 1), tmpJson)
            else:
                ErrorMiddleware.process_exception(self, tmpJson, url)

    def allGetPost(self, url, method):
        """metodo que realiza todos os GET e POST necessarios"""
        with requests.Session() as req:
            req.headers.update({'X-TOKEN':'ddc1a1f3b9580983a7ff3dac3233a779'})
            if method == 'get': 
                response = req.get(url)
            else: 
                response = req.post(url)
            if response.status_code == 200:
                return response.json()
            else:
                return response.status_code
    
    def AccessBacklog(self):
        """metodo que resgata os acessos que estavam conectados na execucao do crawler"""
        lBacklog = tAccess.backlogAccess()
        return list(lBacklog)