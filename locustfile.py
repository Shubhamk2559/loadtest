from locust import HttpUser, task, between


class U(HttpUser):
    wait_time = between(1, 3)

    @task
    def gateway(self):
        with self.client.get(
            "/f/IJEFAbg3",
            name="/f/token",
            catch_response=True,
        ) as r:
            if r.status_code == 200:
                r.success()
            elif r.status_code in (429, 403):
                r.failure(f"blocked {r.status_code}")
            else:
                r.failure(f"status {r.status_code}")
