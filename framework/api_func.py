from api_client import ApiClient


class ApiFunc(ApiClient):
    def __init__(self):
        super().__init__()

    def get_deploy_collection(self):
        url = f'{self.url}/events'
        return self.get(url)
