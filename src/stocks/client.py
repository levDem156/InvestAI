from tinkoff.invest import Client
from tinkoff.invest.constants import INVEST_GRPC_API

from src.common.settings import tinkoff


class TinkoffClient:
    """Singleton-клиент для Tinkoff Invest API"""
    
    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            token = tinkoff.TOKEN.get_secret_value()
            target = INVEST_GRPC_API
            cls._client = Client(token, target=target)
        
        return cls._client

    @classmethod
    def close(cls):
        if cls._client is not None:
            cls._client.close()
            cls._client = None