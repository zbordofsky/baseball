from mlbstatsapi import Mlb

with Mlb() as mlb:
    player = mlb.get_person(664034)
    team = mlb.get_team(136)

print(player.full_name)
print(team.name)