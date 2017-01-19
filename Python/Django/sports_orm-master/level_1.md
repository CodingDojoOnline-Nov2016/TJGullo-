# Simple finds

1. Find all baseball leagues
"leagues": League.objects.filter(sport__icontains='baseball')

2. Find all womens' leagues
"leagues": League.objects.filter(name__icontains='women')

3. Find all leagues where sport is any type of hockey
"leagues": League.objects.filter(sport__icontains='hockey')

4. Find all leagues where sport is something OTHER THAN football
"leagues": League.objects.exclude(sport__icontains='football'),

5. Find all leagues that call themselves "conferences"
"leagues": League.objects.exclude(name__icontains='conference'),

6. Find all leagues in the Atlantic region
"leagues": League.objects.filter(name__icontains='atlantic'),

7. Find all teams based in Dallas
"teams": Team.objects.filter(location__icontains='dallas'),

8. Find all teams named the Raptors
"teams": Team.objects.filter(team_name__icontains='raptors'),

9. Find all teams whose location includes "City"
"teams": Team.objects.filter(location__icontains='city'),

10. Find all teams whose names begin with "T"
"teams": Team.objects.filter(team_name__istartswith='T'),

11. Return all teams, ordered alphabetically by location
"teams": Team.objects.order_by('location'),

12. Return all teams, ordered by team name in reverse alphabetical order
"teams": Team.objects.order_by('-team_name'),

13. Find every player with last name "Cooper"
"players": Player.objects.filter(last_name__icontains='cooper'),

14. Find every player with first name "Joshua"
"players": Player.objects.filter(first_name__icontains='joshua'),

15. Find every player with last name "Cooper" EXCEPT FOR Joshua
"players": Player.objects.filter(last_name__icontains='cooper').exclude(first_name__icontains='joshua'),

16. Find all players with first name "Alexander" OR first name "Wyatt"
"players": Player.objects.filter(first_name__icontains='alexander') | Player.objects.filter(first_name__icontains='wyatt'),
