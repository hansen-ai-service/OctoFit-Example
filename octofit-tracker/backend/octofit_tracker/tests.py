from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        spider = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=spider, type='Running', duration=30, calories=300)
        Workout.objects.create(name='Hero HIIT', description='High intensity', suggested_for='Marvel')
        Leaderboard.objects.create(team=marvel, points=100)

    def test_team_count(self):
        self.assertEqual(Team.objects.count(), 2)

    def test_user_count(self):
        self.assertEqual(User.objects.count(), 2)

    def test_activity_count(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout_count(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard_count(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
