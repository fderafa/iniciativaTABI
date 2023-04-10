from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import datetime

class tNextCrawlerExecute(models.Model):
    """Tabela que armazena a ultima execucao que trouxe registro da API MAMBO"""
    idNext = models.BigAutoField(auto_created=True, primary_key=True)
    lastExecute = models.DateTimeField()
    recordTotal = models.IntegerField(default=0)

    class Meta:
        db_table = 'tNextcrawlerexecute'

    @classmethod
    def lastDateExecute(cls):
        """consulta que retorna a data/hora da ultima execucao"""
        dtLastExe = cls.objects.latest('lastExecute')   #>>> retorna o ultimo registro existente na tabela
        return dtLastExe.lastExecute.strftime('%Y-%m-%d %H:%M:%S')
    
    @classmethod
    def saveCrawlerExecute(cls, _now, total):   #>>> comando insert
        mCrawler = cls(
            lastExecute = _now,
            recordTotal = total
        )
        mCrawler.save()

class tGuests(models.Model):
    """Tabela que armazena todos os visitantes"""
    cpf = models.IntegerField(primary_key=True, default=0)
    refId = models.IntegerField(default=0)
    guestJson = models.JSONField()
    insertDate = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'tGuests'

    @classmethod
    def saveGuest(cls, cpf, refId, json):   #>>> comando insert
        mGuest = cls(
            cpf = cpf, 
            refId = refId,
            guestJson = json
        )
        mGuest.save()

class tAccess(models.Model):
    """Tabela que armazena os acessos dos visitantes"""
    refId = models.IntegerField(primary_key=True, default=0)
    accessJSON = models.JSONField()
    stopConnection = models.BooleanField(default=True)  #>>> campo utilizado para determinar se no momento da execucao do crawler o cliente ja tinha feito a desconexao
    insertDate = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'tAccess'
    
    @classmethod
    def saveAccess(cls, id, conn, json):  #>>> comando insert
        mAccess = cls(
            refId = id,
            stopConnection = conn,
            accessJSON = json
        )
        mAccess.save()
    
    @classmethod
    def backlogAccess(cls):
        """consulta que retorna os casos que nao temos o preenchimento do campo indicando a data/hora da desconexao"""
        lBacklog = cls.objects.filter(stopConnection__exact=False).values_list('refId',flat=True)   #>>> retorna somente o campo refId
        return list(lBacklog)

class tAccessPoint(models.Model):
    """tabela que armazena o Access Point do acesso"""
    refId = models.IntegerField(primary_key=True, default=0)
    identifier = models.CharField(max_length=50)
    accessPointJson = models.JSONField()
    insertDate = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'tAccessPoint'
    
    @classmethod
    def saveAccessPoint(cls, id, ident, json):
        mAccessPoint = cls(
            refId = id,
            identifier = ident,
            accessPointJson = json
        )
        mAccessPoint.save()

class tDevices(models.Model):
    """tabela que armazenara o device que foi utilizado na conexao"""
    refId = models.IntegerField(primary_key=True, default=0)
    macAddress = models.CharField(max_length=50)
    deviceJson = models.JSONField()
    insertDate = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'tDevices'

    @classmethod
    def saveDevice(cls, id, mc, json):
        mDevice = cls(
            refId = id,
            macAddress = mc,
            deviceJson = json
        )
        mDevice.save()

class tErrorHandler(models.Model):
    """Tabela que armazena todos os erros em qualquer pagina (middleware)"""
    idError = models.BigAutoField(auto_created=True, primary_key=True)
    request = models.CharField(max_length=255)
    exceptionError = models.CharField(max_length=800)
    insertDate = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'tErrorHandler'
    
    @classmethod
    def saveErrorHandler(cls, request, description):    #>>> comando insert
        mErrorHandler = cls(
            request = request,
            exceptionError = description
        )
        mErrorHandler.save()
