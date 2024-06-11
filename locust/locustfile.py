from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    host = 'http://localhost:8000/api/ninja'

    @task
    def hello_world(self):
        self.client.get("/doctor/doctors/")
