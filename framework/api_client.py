import requests


class ApiClient:
    default_expected_result = 200

    def __init__(self):
        self.url = 'http://127.0.0.1:4000'

    def get(self, url):
        # if not expected_result:
        #    expected_result = self.default_expected_result
        session = requests.Session()
        return session.get(url).json()
        # assert expected_result == result


class ApiFunctions(ApiClient):
    def __init__(self):
        super().__init__()

    def get_deploy_collection(self):
        url = f'{self.url}/events'
        return self.get(url)

    def get_deploy_collection_id(self):
        """Выполняем запрос и берем последнюю созданную
         коллекцию и возвращаем id
         коллекции для создания NFT"""
        url = f'{self.url}/events'
        collection_name_event_create = self.get(url)
        result_collection_id = collection_name_event_create[0].get('collection')
        return result_collection_id
