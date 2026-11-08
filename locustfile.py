from locust import HttpUser, task, between

class U(HttpUser):
    wait_time = between(1, 3)

    @task
    def gateway(self):
        self.client.get("/f/IJEFAbg3", name="/f/token")
