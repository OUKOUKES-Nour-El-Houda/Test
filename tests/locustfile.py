from locust import HttpUser, task, between

class PokemonApiUser(HttpUser):
    wait_time = between(2, 5)

    @task
    def get_battle(self):
        # Utilise GET avec les paramètres dans l'URL
        self.client.get("/?first_id=1&second_id=2")

