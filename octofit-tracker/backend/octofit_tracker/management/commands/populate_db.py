from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        self.stdout.write(self.style.SUCCESS('Connected to MongoDB'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email field
        db.users.create_index('email', unique=True)
        self.stdout.write(self.style.SUCCESS('Created unique index on email field'))

        # Insert Teams
        self.stdout.write('Creating teams...')
        teams_data = [
            {
                '_id': 'team_marvel',
                'name': 'Team Marvel',
                'description': 'Earth\'s Mightiest Heroes',
                'created_at': datetime.now(),
                'member_count': 0
            },
            {
                '_id': 'team_dc',
                'name': 'Team DC',
                'description': 'Justice League United',
                'created_at': datetime.now(),
                'member_count': 0
            }
        ]
        db.teams.insert_many(teams_data)
        self.stdout.write(self.style.SUCCESS(f'Created {len(teams_data)} teams'))

        # Insert Users (Superheroes)
        self.stdout.write('Creating users...')
        users_data = [
            # Team Marvel
            {
                '_id': 'user_ironman',
                'name': 'Tony Stark',
                'email': 'tony.stark@marvel.com',
                'superhero_name': 'Iron Man',
                'team_id': 'team_marvel',
                'created_at': datetime.now(),
                'avatar': '🦾',
                'total_points': 0
            },
            {
                '_id': 'user_cap',
                'name': 'Steve Rogers',
                'email': 'steve.rogers@marvel.com',
                'superhero_name': 'Captain America',
                'team_id': 'team_marvel',
                'created_at': datetime.now(),
                'avatar': '🛡️',
                'total_points': 0
            },
            {
                '_id': 'user_thor',
                'name': 'Thor Odinson',
                'email': 'thor@marvel.com',
                'superhero_name': 'Thor',
                'team_id': 'team_marvel',
                'created_at': datetime.now(),
                'avatar': '🔨',
                'total_points': 0
            },
            {
                '_id': 'user_hulk',
                'name': 'Bruce Banner',
                'email': 'bruce.banner@marvel.com',
                'superhero_name': 'Hulk',
                'team_id': 'team_marvel',
                'created_at': datetime.now(),
                'avatar': '💚',
                'total_points': 0
            },
            {
                '_id': 'user_widow',
                'name': 'Natasha Romanoff',
                'email': 'natasha.romanoff@marvel.com',
                'superhero_name': 'Black Widow',
                'team_id': 'team_marvel',
                'created_at': datetime.now(),
                'avatar': '🕷️',
                'total_points': 0
            },
            # Team DC
            {
                '_id': 'user_superman',
                'name': 'Clark Kent',
                'email': 'clark.kent@dc.com',
                'superhero_name': 'Superman',
                'team_id': 'team_dc',
                'created_at': datetime.now(),
                'avatar': '🦸',
                'total_points': 0
            },
            {
                '_id': 'user_batman',
                'name': 'Bruce Wayne',
                'email': 'bruce.wayne@dc.com',
                'superhero_name': 'Batman',
                'team_id': 'team_dc',
                'created_at': datetime.now(),
                'avatar': '🦇',
                'total_points': 0
            },
            {
                '_id': 'user_wonderwoman',
                'name': 'Diana Prince',
                'email': 'diana.prince@dc.com',
                'superhero_name': 'Wonder Woman',
                'team_id': 'team_dc',
                'created_at': datetime.now(),
                'avatar': '⚔️',
                'total_points': 0
            },
            {
                '_id': 'user_flash',
                'name': 'Barry Allen',
                'email': 'barry.allen@dc.com',
                'superhero_name': 'The Flash',
                'team_id': 'team_dc',
                'created_at': datetime.now(),
                'avatar': '⚡',
                'total_points': 0
            },
            {
                '_id': 'user_aquaman',
                'name': 'Arthur Curry',
                'email': 'arthur.curry@dc.com',
                'superhero_name': 'Aquaman',
                'team_id': 'team_dc',
                'created_at': datetime.now(),
                'avatar': '🔱',
                'total_points': 0
            }
        ]
        db.users.insert_many(users_data)
        self.stdout.write(self.style.SUCCESS(f'Created {len(users_data)} users'))

        # Update team member counts
        db.teams.update_one({'_id': 'team_marvel'}, {'$set': {'member_count': 5}})
        db.teams.update_one({'_id': 'team_dc'}, {'$set': {'member_count': 5}})

        # Insert Workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                '_id': 'workout_cardio',
                'name': 'Cardio Blast',
                'description': 'High-intensity cardio workout',
                'category': 'cardio',
                'duration_minutes': 30,
                'calories_burned': 300,
                'difficulty': 'intermediate'
            },
            {
                '_id': 'workout_strength',
                'name': 'Strength Training',
                'description': 'Full body strength workout',
                'category': 'strength',
                'duration_minutes': 45,
                'calories_burned': 250,
                'difficulty': 'advanced'
            },
            {
                '_id': 'workout_yoga',
                'name': 'Morning Yoga',
                'description': 'Relaxing yoga session',
                'category': 'flexibility',
                'duration_minutes': 60,
                'calories_burned': 150,
                'difficulty': 'beginner'
            },
            {
                '_id': 'workout_hiit',
                'name': 'HIIT Session',
                'description': 'High-Intensity Interval Training',
                'category': 'cardio',
                'duration_minutes': 20,
                'calories_burned': 280,
                'difficulty': 'advanced'
            },
            {
                '_id': 'workout_run',
                'name': '5K Run',
                'description': 'Outdoor running session',
                'category': 'cardio',
                'duration_minutes': 35,
                'calories_burned': 350,
                'difficulty': 'intermediate'
            }
        ]
        db.workouts.insert_many(workouts_data)
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts_data)} workouts'))

        # Insert Activities
        self.stdout.write('Creating activities...')
        activities_data = []
        activity_types = ['cardio', 'strength', 'yoga', 'hiit', 'run']
        user_ids = [user['_id'] for user in users_data]
        
        activity_id = 1
        for i in range(50):  # Create 50 random activities
            user_id = random.choice(user_ids)
            activity_type = random.choice(activity_types)
            duration = random.randint(15, 60)
            calories = random.randint(100, 400)
            points = calories // 10
            
            # Random date within last 30 days
            days_ago = random.randint(0, 30)
            activity_date = datetime.now() - timedelta(days=days_ago)
            
            activities_data.append({
                '_id': f'activity_{activity_id}',
                'user_id': user_id,
                'workout_id': f'workout_{activity_type}',
                'activity_type': activity_type,
                'duration_minutes': duration,
                'calories_burned': calories,
                'points_earned': points,
                'date': activity_date,
                'notes': f'Great {activity_type} workout!'
            })
            
            # Update user total points
            db.users.update_one(
                {'_id': user_id},
                {'$inc': {'total_points': points}}
            )
            
            activity_id += 1
        
        db.activities.insert_many(activities_data)
        self.stdout.write(self.style.SUCCESS(f'Created {len(activities_data)} activities'))

        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard...')
        leaderboard_data = []
        
        # Individual leaderboard
        for user in users_data:
            user_doc = db.users.find_one({'_id': user['_id']})
            leaderboard_data.append({
                'user_id': user['_id'],
                'user_name': user['name'],
                'superhero_name': user['superhero_name'],
                'team_id': user['team_id'],
                'total_points': user_doc['total_points'],
                'rank': 0,  # Will be updated after sorting
                'type': 'individual'
            })
        
        # Sort by points and assign ranks
        leaderboard_data.sort(key=lambda x: x['total_points'], reverse=True)
        for idx, entry in enumerate(leaderboard_data):
            entry['rank'] = idx + 1
            entry['_id'] = f"leaderboard_individual_{entry['user_id']}"
        
        # Team leaderboard
        team_points = {}
        for team in teams_data:
            team_id = team['_id']
            # Calculate total points for team
            pipeline = [
                {'$match': {'team_id': team_id}},
                {'$group': {'_id': '$team_id', 'total_points': {'$sum': '$total_points'}}}
            ]
            result = list(db.users.aggregate(pipeline))
            points = result[0]['total_points'] if result else 0
            team_points[team_id] = points
            
            leaderboard_data.append({
                '_id': f'leaderboard_team_{team_id}',
                'team_id': team_id,
                'team_name': team['name'],
                'total_points': points,
                'member_count': team['member_count'],
                'rank': 0,
                'type': 'team'
            })
        
        # Sort team entries and assign ranks
        team_entries = [e for e in leaderboard_data if e['type'] == 'team']
        team_entries.sort(key=lambda x: x['total_points'], reverse=True)
        for idx, entry in enumerate(team_entries):
            entry['rank'] = idx + 1
        
        db.leaderboard.insert_many(leaderboard_data)
        self.stdout.write(self.style.SUCCESS(f'Created {len(leaderboard_data)} leaderboard entries'))

        # Display summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams: {db.teams.count_documents({})}')
        self.stdout.write(f'Users: {db.users.count_documents({})}')
        self.stdout.write(f'Workouts: {db.workouts.count_documents({})}')
        self.stdout.write(f'Activities: {db.activities.count_documents({})}')
        self.stdout.write(f'Leaderboard Entries: {db.leaderboard.count_documents({})}')
        self.stdout.write(self.style.SUCCESS('\nTop 3 on Individual Leaderboard:'))
        
        top_users = db.leaderboard.find({'type': 'individual'}).sort('rank', 1).limit(3)
        for user in top_users:
            self.stdout.write(f"  {user['rank']}. {user['superhero_name']} ({user['user_name']}) - {user['total_points']} points")
        
        self.stdout.write(self.style.SUCCESS('\nTeam Standings:'))
        team_standings = db.leaderboard.find({'type': 'team'}).sort('rank', 1)
        for team in team_standings:
            self.stdout.write(f"  {team['rank']}. {team['team_name']} - {team['total_points']} points")

        client.close()
