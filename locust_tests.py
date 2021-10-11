from locust import HttpUser, task, between


class LocustTest(HttpUser):
    wait_time = between(0.1, 0.2)

    @task
    def test_display_competition(self):
        self.client.post('/showSummary', data={'email': 'john@simplylift.co'})

    @task
    def test_update_club_points_and_competition_places(self):
        self.client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Spring Festival',
                                                  'places': 1})
