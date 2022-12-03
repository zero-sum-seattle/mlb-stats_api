# Python MLB Stats API - Unofficial MLB Stats API

![MLB Stats API](https://user-images.githubusercontent.com/2068393/203456246-dfdbdf0f-1e43-4329-aaa9-1c4008f9800d.jpg)


*Python-mlb-statsapi* is an unffocial MLB Stats API written in python 3.7+. It provides developers access to the MLB Stats API endpoint to pull information related to MLB Rosters, Teams, Players, and stats. 

This is a educational project so no commercial use. 

*Copyright Notice*
This package and its authors are not affiliated with MLB or any MLB team. This API wrapper interfaces with MLB's Stats API. Use of MLB data is subject to the notice posted at http://gdx.mlb.com/components/copyright.txt.

## Installation
```
python3 -m pip install -i https://test.pypi.org/simple/ python-mlb-statsapi
```
## Usage
```
python3
>>> mlb = mlbstatsapi.Mlb()
>>> mlb.get_people_id("Ty France")
[664034]
>>> stats = ['season', 'seasonAdvanced']
>>> groups = ['hitting']
>>> mlb.get_player_stats(664034, stats=stats, groups=groups)
{'hitting': {'season': [HittingSeason], 'seasonadvanced': [HittingSeasonAdvanced] }}

>>> mlb.get_team_id("Oakland Athletics")
[133]

>>> stats = ['season', 'seasonAdvanced']
>>> groups = ['pitching']
>>> mlb.get_team_stats(133, stats, groups)
{'pitching': {'season': [PitchingSeason], 'seasonadvanced': [PitchingSeasonAdvanced] }}
```


## Documentation

### People, Person, Players, Coaches
* `Mlb.get_people_id()` - Return Person Id(s) from fullname
* `Mlb.get_person()` - Return Person Object from Id
* `Mlb.get_people()` - Return all Players from Sport
### Draft
* `Mlb.get_draft()` - Return a draft for a given year
### Teams
* `Mlb.get_team_id()` - Return Team Id(s) from name
* `Mlb.get_team()` - Return Team Object from Team Id
* `Mlb.get_teams()` - Return all Teams for Sport
* `Mlb.get_team_coaches()` - Return coaching roster for team for current or specified season
* `Mlb.get_team_roster()` - Return player roster for team for current or specified season
### Stats
* `Mlb.get_player_stats()` - Return stats by player id, stat type and groups
* `Mlb.get_team_stats()` - Return stats by team id, stat types and groups
* `Mlb.get_stats()` - Return stats by stat type and group args
* `Mlb.get_players_stats_for_game()` - Return player stats for a game
### Venues
* `Mlb.get_venue_id()` - Return Venue Id(s)
* `Mlb.get_venue()` - Return Venue Object from venue Id
* `Mlb.get_venues()` - Return all Venues
### Sports
* `Mlb.get_sport()` - Return a Sport object from Id
* `Mlb.get_sports()` - Return all teams for Sport Id
* `Mlb.get_sport_id()`- Return Sport Id from name
### Divisions
* `Mlb.get_division()` - Return a Divison 
* `Mlb.get_divisions()` - Return all Divisions
* `Mlb.get_division_id()` - Return Division Id(s) from name
### Leagues
* `Mlb.get_league()` - Return a League from Id
* `Mlb.get_leagues()` - Return all Leagues
* `Mlb.get_league_id()` - Return League Id(s)
### Schedules
* `Mlb.get_schedule()` - Return a Schedule from dates
### Games
* `Mlb.get_game()` - Return the Game for a specific Game Id
* `Mlb.get_game_play_by_play()` - Return Play by play data for a game
* `Mlb.get_game_line_score()` - Return a Linescore for a game
* `Mlb.get_game_box_score()` - Return a Boxscore for a game

## Examples

Let's show some examples of getting stat objects from the API. What is baseball with out stats right?

NOTE: Stat types and groups are case sensitive
### Stats

#### Player Stats
Get the Id(s) of the players you want stats for and set stat types and groups.
```
>>> mlb = mlbstatsapi.Mlb()
>>> player = mlb.get_player_id("Ty France")
>>> types = ['season`, `career` ]
>>> groups = ['hitting', 'pitching]
```
Use player.id and stat types and groups to return a stats dictionary
```
>>> stat_dict = mlb.get_player_stats(player.id, stats=types, groups=groups )
>>> season_hitting_stat = stat_dict['hitting']['season']
>>> career_pitching_stat = stat_dict['pitching']['career']
```
Print season hitting stats
```
>>> for attribute, value in season_hitting_stat.stat.__dict__.items():
...     print(attribute, value)
>>>
```
#### Team stats
Get the Team Id(s)
```
python3
>>> mlb = mlbstatsapi.Mlb()
>>> team = mlb.get_team_id('Seattle Mariners')
>>> print(team.id)
[136]
```
Set the stat types and groups.
```
>>> types = ['season', 'seasonAdvanced']
>>> groups = ['hitting']
```
Use team.id and the stat types and groups to return season hitting stats
```
stats = mlb.get_team_stats(team.id, stats=types, groups=groups)
season_hitting = stats['hitting']['season']
advanced_hitting = stats['hitting']['seasonadvanced']
```
Print season and seasonadvanced stats
```
>>> for attribute, value in season_hitting.stat.__dict__.items():
...     print(attribute, value)
>>>
... for attribute, value in advanced_hitting.stat.__dict__.items():
>>>     print(attribute, value)
```

### More stats examples
#### Expected Stats
Get player Id's
```
>>> player = mlb.get_player_id('Ty France')
```
Set the stat type and group
```
>>> stats = ['expectedStatistics']
>>> group = ['hitting']
```
Get Stats
```
stats = mlb.get_player_stats(player, stats=stats, groups=group)
expectedstats = stats['hitting']['expectedstatistics']
#### hotColdZones
Get player Id's
```
>>> hitter = mlb.get_player_id('Ty France')
>>> pitcher = mlb.get_player_id('Shoei Ohtani')
```
Set the stat types and groups
```
>>> type = ['hotColdZones']
>>> hitting_group = ['hitting']
>>> pitching_group = ['pitching']
```
The stat groups pitching and hitting both return hotColdZones for a pitcher and hitter. hotColdZones are not assigned to a
stat group because of issues related to the REST API. So hotColdZones will be assigned to the stat key in stats return dict.
```
>>> hitting_hotcoldzones = mlb.get_player_stats(hitter.id, stats=type, groups=hitting_group)
>>> pitching_hotcoldzones = mlb.get_player_stats(pitcher.id, stats=type, groups=pitching_group)
```
hotColdZones returns a list of the HotColdZones
```
>>> ty_france_hotcoldzones = hitting_hotcoldzones['stats']['hotcoldzones'][0]
>>> shoei_ohtani_hotcoldzones = pitching_hotcoldzones['stats']['hotcoldzones'][0]
```
Loop through the hotColdZone objects for Ty France
```
>>> for zone in ty_france_hotcoldzones:
>>>     print(zone.zone)
>>>     print(zone.value)
>>>             
```
Loop through the hotColdZone objects for Shoei Ohtani
```
>>> for zone in shoei_ohtani_hotcoldzones:
>>>     print(zonecodes.zone)
>>>     print(zonecodes.value)
>>>
```
#### Passing params
Get Team Ids
```
python3
>>> mlb = mlbstatsapi.Mlb()
>>> team = mlb.get_team_id('Seattle Mariners')
```
Set the stat types and groups.
```
>>> types = ['season', 'seasonAdvanced']
>>> groups = ['hitting']
```
Pass season to get_team_stats()
```
stats = mlb.get_team_stats(team.id, stats=types, groups=groups, season=2018)

season_hitting = stats['hitting']['season']
advanced_hitting = stats['hitting']['seasonadvanced']
```
season should be 2018
```
assertEqual(stats[season_hitting.season == 2018)
assertEqual(stats[advanced_hitting.season == 2018)
```
### Schedule Examples
Get a schedule for given date
```
>>> mlb = mlbstatsapi.Mlb()
>>> schedule = mlb.get_schedule_date('2022-10-13')
```
Get ScheduleDates from Schedule
```
dates = schedule.dates
```
Print Game status and Home and Away Teams
```
>>> for date in dates:
...     for game in date.games:
...             print(game.status)
...             print(game.teams.home)
...             print(game.teams.away)
```
### Game Examples

### People Examples
Get all Players for a given sport id
```
>>> mlb = mlbstatsapi.Mlb()
>>> sport_id = mlb.get_sport_id()
>>> players = mlb.get_players(sport_id=sport_id)
>>> for player in players:
...     print(player.id)
```
Get a player id
```
>>> player_id = mlb.get_player_id("Ty France")
>>> print(player_id[0])
```

### Team Examples
Get a Team
```
>>> mlb = mlbstatsapi.Mlb()
>>> team_ids = mlb.get_team_id("Seattle Mariners")
>>> team_id = team_ids[0]
>>> team = mlb.get_team(team_id.id)
>>> print(team.id)
>>> print(team.name)
```
Get a Player Roster
```
>>> mlb = mlbstatsapi.Mlb()
>>> team_id = 133
>>> players = mlb.get_team_roster(team_id)
>>> for player in players:
        print(player.jerseynumber)
```
Get a Coach Roster
```
>>> mlb = mlbstatsapi.Mlb()
>>> team_id = 133
>>> coaches = mlb.get_team_coaches(team_id)
>>> for coach in coaches:
        print(coach.title)
```
### Draft Examples
Get a draft for a year
```
>>> mlb = mlbstatsapi.Mlb()
>>> draft_year = '2019'
>>> draft = mlb.get_draft(draft_year)
```
Get Players from Draft
```
>>> draftpicks = draft[0].picks
>>> for draftpick in draftpicks:
...     print(draftpick.id)
...     print(draftpick.pickround)
```

### Venue Examples
Get a Venue
```
>>> mlb = mlbstatsapi.Mlb()
>>> vevue_ids = mlb.get_venue_id('PNC Park')
>>> venue_id = venue_ids[0]
>>> venue = mlb.get_team(venue.id)
>>> print(venue.id)
>>> print(venue.name)
```

### Sport Examples
Get a Sport
```
>>> mlb = mlbstatsapi.Mlb()
>>> sport_ids = mlb.get_sport_id('Major League Baseball')
>>> sport_id = sport_ids[0]
>>> sport = mlb.get_sport(sport_id)
```

