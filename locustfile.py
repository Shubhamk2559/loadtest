from locust import HttpUser, task, between


class U(HttpUser):
    wait_time = between(1, 3)

    @task
    def gateway(self):
        with self.client.get(
            "/f/IJEFAbg3",
            name="/f/token",
            allow_redirects=False,
            catch_response=True,
        ) as r:
            if r.status_code in (200, 302):
                r.success()
            else:
                r.failure(f"status {r.status_code}")
