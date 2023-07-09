import requests


class ApiClient:
    default_expected_result = 200

    def __init__(self):
        self.url = 'http://localhost:4000'

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
