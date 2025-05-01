from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice Anderson')
        user2 = User.objects.create(email='bob@example.com', name='Bob Brown')
        user3 = User.objects.create(email='carol@example.com', name='Carol Clark')

        # Teams
        team1 = Team.objects.create(name='Team Octopus')
        team1.members.add(user1, user2)
        team2 = Team.objects.create(name='Team Kraken')
        team2.members.add(user3)

        # Workouts
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups', points=10)
        workout2 = Workout.objects.create(name='Running', description='Run 1 mile', points=20)

        # Activities
        Activity.objects.create(user=user1, type='run', duration=30, points=20)
        Activity.objects.create(user=user2, type='pushups', duration=10, points=10)
        Activity.objects.create(user=user3, type='run', duration=25, points=20)

        # Leaderboard
        Leaderboard.objects.create(name='May Leaderboard')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
