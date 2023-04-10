from django.utils.deprecation import MiddlewareMixin
from appGET_crawler.models import tErrorHandler
import traceback

class ErrorMiddleware(MiddlewareMixin):
    """classe para tratamento de erro geral"""
    def process_exception(self, request, exception):
        error_message = "-".join([str(request), str(exception)])  #>>> captura a mensagem de erro
        traceback_info = traceback.format_exc() #>>> captura linha, arquivo e mais detalhes do erro
        tErrorHandler.saveErrorHandler(error_message, traceback_info)
