from locust import HttpUser, between, task


class AlePedroUser(HttpUser):
    host = "http://localhost"
    wait_time = between(5, 10)

    @task
    def post_1mb(self):
        self.client.get("/2024/05/04/uma-imagem-de-1mb/")

    @task
    def post_300kb(self):
        self.client.get("/2024/05/04/uma-imagem-de-300kb/")

    @task
    def post_400kb(self):
        self.client.get("/2024/05/04/um-texto-de-aproximadamente-400kb/")