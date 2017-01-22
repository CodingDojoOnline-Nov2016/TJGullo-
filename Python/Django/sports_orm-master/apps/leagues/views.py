from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
	context = {
		# "leagues": League.objects.filter(teams__curr_players__first_name__icontains='Sophia'),
		# "teams": Team.objects.filter(curr_players__first_name__icontains='Sophia'),
		"players": Player.objects.filter(last_name__icontains='flores').exclude(curr_team__team_name__icontains='roughriders'),

	}
    teams =
    Team.objects.annotate(number_of_players=Count('all_players')).filter(number_of_players_gte=12).count()
    print teams
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
