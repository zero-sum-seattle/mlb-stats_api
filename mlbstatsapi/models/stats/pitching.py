﻿from dataclasses import InitVar, dataclass, field
from typing import Optional, Union, List

from mlbstatsapi.models.people import Person
from mlbstatsapi.models.teams import Team
from mlbstatsapi.models.game import Game

from .stats import Stats, CodeDesc, Count

@dataclass
class SimplePitching:
    """
    A class to represent a advanced pitching statistics

    attributes are all optional as there is no documentation for the stats endpoint
    """
    gamesplayed: Optional[int] = None
    gamesstarted: Optional[int] = None
    groundouts: Optional[int] = None
    airouts: Optional[int] = None
    runs: Optional[int] = None
    doubles: Optional[int] = None
    triples: Optional[int] = None
    homeruns: Optional[int] = None
    strikeouts: Optional[int] = None
    baseonballs: Optional[int] = None
    intentionalwalks: Optional[int] = None
    hits: Optional[int] = None
    hitbypitch: Optional[int] = None
    avg: Optional[str] = None
    atbats: Optional[int] = None
    obp: Optional[str] = None
    slg: Optional[str] = None
    ops: Optional[str] = None
    caughtstealing: Optional[int] = None
    stolenbases: Optional[int] = None
    stolenbasepercentage: Optional[str] = None
    groundintodoubleplay: Optional[int] = None
    numberofpitches: Optional[int] = None
    era: Optional[str] = None
    inningspitched: Optional[str] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    saves: Optional[int] = None
    saveopportunities: Optional[int] = None
    holds: Optional[int] = None
    blownsaves: Optional[int] = None
    earnedruns: Optional[int] = None
    whip: Optional[str] = None
    outs: Optional[int] = None
    gamespitched: Optional[int] = None
    completegames: Optional[int] = None
    shutouts: Optional[int] = None
    strikes: Optional[int] = None
    strikepercentage: Optional[str] = None
    hitbatsmen: Optional[int] = None
    balks: Optional[int] = None
    wildpitches: Optional[int] = None
    pickoffs: Optional[int] = None
    totalbases: Optional[int] = None
    groundoutstoairouts: Optional[str] = None
    winpercentage: Optional[str] = None
    pitchesperinning: Optional[str] = None
    gamesfinished: Optional[int] = None
    strikeoutwalkratio: Optional[str] = None
    strikeoutsper9inn: Optional[str] = None
    walksper9inn: Optional[str] = None
    hitsper9inn: Optional[str] = None
    runsscoredper9: Optional[str] = None
    homerunsper9: Optional[str] = None
    catchersinterference: Optional[int] = None
    sacbunts: Optional[int] = None
    sacflies: Optional[int] = None
    battersfaced: Optional[int] = None
    inheritedrunners: Optional[int] = None
    inheritedrunnersscored: Optional[int] = None

@dataclass
class AdvancedPitching:
    """
    A class to represent a advanced pitching statistics

    attributes are all optional as there is no documentation for the stats endpoint
    """
    winningpercentage: Optional[str] = None
    runsscoredper9: Optional[str] = None
    battersfaced: Optional[int] = None
    babip: Optional[str] = None
    obp: Optional[str] = None
    slg: Optional[str] = None
    ops: Optional[str] = None
    strikeoutsper9: Optional[str] = None
    baseonballsper9: Optional[str] = None
    homerunsper9: Optional[str] = None
    hitsper9: Optional[str] = None
    strikesoutstowalks: Optional[str] = None
    stolenbases: Optional[int] = None
    caughtstealing: Optional[int] = None
    qualitystarts: Optional[int] = None
    gamesfinished: Optional[int] = None
    doubles: Optional[int] = None
    triples: Optional[int] = None
    gidp: Optional[int] = None
    gidpopp: Optional[int] = None
    wildpitches: Optional[int] = None
    balks: Optional[int] = None
    pickoffs: Optional[int] = None
    totalswings: Optional[int] = None
    swingandmisses: Optional[int] = None
    ballsinplay: Optional[int] = None
    runsupport: Optional[int] = None
    strikepercentage: Optional[str] = None
    pitchesperinning: Optional[str] = None
    pitchesperplateappearance: Optional[str] = None
    walksperplateappearance: Optional[str] = None
    strikeoutsperplateappearance: Optional[str] = None
    homerunsperplateappearance: Optional[str] = None
    walksperstrikeout: Optional[str] = None
    iso: Optional[str] = None
    flyouts: Optional[int] = None
    popouts: Optional[int] = None
    lineouts: Optional[int] = None
    groundouts: Optional[int] = None
    flyhits: Optional[int] = None
    pophits: Optional[int] = None
    linehits: Optional[int] = None
    groundhits: Optional[int] = None
    inheritedrunners: Optional[int] = None
    inheritedrunnersscored: Optional[int] = None
    bequeathedrunners: Optional[int] = None
    bequeathedrunnersscored: Optional[int] = None

@dataclass(kw_only=True)
class PitchingSabermetrics(Stats):
    """
    A class to represent a pitching sabermetric statistics

    Attributes
    ----------
    fip : float
        Fielding Independent Pitching
    fipminus : float
        Fielding Independent Pitching Minus
    ra9war : float
        Runs Allowed 9 innings Wins Above Replacement
    rar : float 
        Runs Above Replacement
    war : float
        Wins Above Replacement
    gametype : str
        the gametype code of the pitching season 
    numteams : str
        the number of teams for the pitching season
    """
    type_ = ['sabermetrics']
    fip: float
    fipminus: float
    ra9war: float
    rar: float
    war: float

@dataclass(kw_only=True)
class PitchingSeason(Stats, SimplePitching):
    """
    A class to represent a pitching season statistic

    Attributes
    ----------
    gametype : str
        the gametype code of the pitching season 
    numteams : str
        the number of teams for the pitching season
    """
    type_ = [ 'season' ]

@dataclass(kw_only=True)
class PitchingSingleSeason(Stats, SimplePitching):
    """
    A class to represent a pitching season statistic

    Attributes
    ----------
    gametype : str
        the gametype code of the pitching season 
    numteams : str
        the number of teams for the pitching season
    """
    type_ = [ 'statsSingleSeason' ]

@dataclass(kw_only=True)
class PitchingCareer(Stats, SimplePitching):
    """
    A class to represent a pitching season statistic

    Attributes
    ----------
    gametype : Team
        the gametype code of the pitching yearByYear 
    numteams : str
        the number of teams for the pitching season
    """
    type_ = [ 'career']

@dataclass(kw_only=True)
class PitchingCareerAdvanced(Stats, AdvancedPitching):
    """
    A class to represent a pitching season statistic

    Attributes
    ----------
    gametype : Team
        the gametype code of the pitching yearByYear 
    numteams : str
        the number of teams for the pitching season
    """
    type_ = [ 'careerAdvanced' ]

@dataclass(kw_only=True)
class PitchingYearByYear(Stats, SimplePitching):
    """
    A class to represent a yearByYear season statistic

    Attributes
    ----------
    gametype : Team
        the gametype code of the pitching yearByYear 
    numteams : str
        the number of teams for the pitching yearByYear
    """
    type_ = [ 'yearByYear' ]

@dataclass(kw_only=True)
class PitchingYearByYearPlayoffs(Stats, SimplePitching):
    """
    A class to represent a yearByYear season statistic

    Attributes
    ----------
    gametype : Team
        the gametype code of the pitching yearByYear 
    numteams : str
        the number of teams for the pitching yearByYear
    """
    type_ = [ 'yearByYearPlayoffs' ]

@dataclass(kw_only=True)
class PitchingYearByYearAdvanced(Stats, AdvancedPitching):
    """
    A class to represent a pitching yearByYear statistic

    Attributes
    ----------
    gametype : Team
        the gametype code of the pitching yearByYear 
    numteams : str
        the number of teams for the pitching yearByYear
    """
    type_ = [ 'yearByYearAdvanced' ]

@dataclass(kw_only=True)
class PitchingSeasonAdvanced(Stats, AdvancedPitching):
    """
    A class to represent a pitching seasonAdvanced statistic

    Attributes
    ----------
    gametype : Team
        the gametype code of the pitching season 
    numteams : str
        the number of teams for the pitching season
    """
    type_ = [ 'seasonAdvanced' ]

@dataclass(kw_only=True)
class PitchingSingleSeasonAdvanced(Stats, AdvancedPitching):
    """
    A class to represent a pitching seasonAdvanced statistic

    Attributes
    ----------
    gametype : Team
        the gametype code of the pitching season 
    numteams : str
        the number of teams for the pitching season
    """
    type_ = [ 'statsSingleSeasonAdvanced' ]

@dataclass(kw_only=True)
class PitchingGameLog(Stats, SimplePitching):
    """
    A class to represent a gamelog stat for a pitcher

    Attributes
    ----------
    ishome : bool
        bool to hold ishome
    iswin : bool
        bool to hold iswin
    game : Game
        Game of the log
    date : str
        date of the log
    gametype : str
        type of game
    opponent : Team
        Team of the opponent
    """
    ishome: bool
    iswin: bool
    game: Union[Game, dict]
    date: str
    opponent: Union[Team, dict]
    type_ = [ 'gameLog' ]

@dataclass
class PlayDetails:
    """
    A class to represent a gamelog stat for a hitter

    Attributes
    ----------
    call : dict
        play call code and description
    description : str
        description of the play
    event : str
        type of event
    eventtype : str
        type of event
    isinplay : bool
        is the ball in play true or false
    isstrike : bool
        is the ball a strike true or false
    isball : bool
        is it a ball true or false
    isbasehit : bool
        is the event a base hit true or false
    isatbat : bool
        is the event at bat true or false
    isplateappearance : bool
        is the event a at play appears true or false
    type : dict
        type of pitch code and description
    batside : dict
        bat side code and description
    pitchhand : dict
        pitch hand code and description
    """
    call: Union[CodeDesc, dict]
    event: str
    eventtype: str
    isinplay: bool
    isstrike: bool
    isball: bool
    isbasehit: bool
    isatbat: bool
    isplateappearance: bool
    type: Union[CodeDesc, dict]
    batside: Union[CodeDesc, dict]
    pitchhand: Union[CodeDesc, dict]
    description: Optional[str] = None

@dataclass(kw_only=True)
class PitchingLog(Stats):
    """
    A class to represent a pitchLog stat for a pitcher

    Attributes
    ----------
    season : str
        season for the stat
    stat : PlayLog
        information regarding the play for the stat
    team : Team
        team of the stat
    player : Person
        player of the stat
    opponent : Team
        opponent
    date : str
        date of log
    gametype : str
        game type code
    ishome : bool
        is the game at home bool
    pitcher : Person
        pitcher of the log
    batter : Person
        batter of the log
    game : Game
        the game of the log

    """
    type_ = [ 'pitchLog' ]
    season: str
    opponent: Union[Team, dict]
    date: str
    ishome: bool
    pitcher: Union[Person, dict]
    batter: Union[Person, dict]
    game: Union[Game, dict]
    details: Union[PlayDetails, dict]
    count: Union[Count, dict]
    playid: str
    pitchnumber: int
    atbatnumber: int
    ispitch: bool

    def __post_init__(self):
        self.details = PlayDetails(**self.details)
        self.count = Count(**self.count)

@dataclass(kw_only=True)
class PitchingPlayLog(Stats):
    """
    A class to represent a playLog stat for a pitcher

    Attributes
    ----------
    season : str
        season for the stat
    stat : PlayLog
        information regarding the play for the stat
    team : Team
        team of the stat
    player : Person
        player of the stat
    opponent : Team
        opponent
    date : str
        date of log
    gametype : str
        game type code
    ishome : bool
        is the game at home bool
    pitcher : Person
        pitcher of the log
    batter : Person
        batter of the log
    game : Game
        the game of the log

    """
    type_ = [ 'playLog' ]
    season: str
    opponent: Union[Team, dict]
    date: str
    ishome: bool
    pitcher: Union[Person, dict]
    batter: Union[Person, dict]
    game: Union[Game, dict]
    details: Union[PlayDetails, dict]
    count: Union[Count, dict]
    playid: str
    pitchnumber: int
    atbatnumber: int
    ispitch: bool

    def __post_init__(self):
        self.details = PlayDetails(**self.details)
        self.count = Count(**self.count)


@dataclass(kw_only=True)
class PitchingByDateRange(Stats, SimplePitching):
    """
    A class to represent a byDateRange stat for a pitcher

    Attributes
    ----------
    daysofweek : int
    numteams : int
    daysofweek : int

    """
    type_ = [ 'byDateRange' ]
    dayofweek: Optional[int] = None

@dataclass(kw_only=True)
class PitchingByDateRangeAdvanced(Stats, AdvancedPitching):
    """
    A class to represent a byDateRangeAdvanced stat for a pitcher

    Attributes
    ----------
    numteams : int
    daysofweek : int
    """
    type_ = [ 'byDateRangeAdvanced' ]
    dayofweek: Optional[int] = None

@dataclass(kw_only=True)
class PitchingByMonth(Stats, SimplePitching):
    """
    A class to represent a byMonthPlayoffs stat for a pitcher

    Attributes
    ----------
    month : int
    numteams : int

    """
    type_ = [ 'byMonth']
    month: int

@dataclass(kw_only=True)
class PitchingByMonthPlayoffs(Stats, SimplePitching):
    """
    A class to represent a byMonthPlayoffs stat for a pitcher

    Attributes
    ----------
    month : int
    numteams : int
    """
    type_ = [ 'byMonthPlayoffs' ]
    month: int

@dataclass(kw_only=True)
class PitchingByDayOfWeek(Stats, SimplePitching):
    """
    A class to represent a byDayOfWeek stat for a pitcher

    Attributes
    ----------
    dayofweek : int
    daysofweek : int
    numteams: int

    """
    type_ = [ 'byDayOfWeek' ]
    dayofweek: Optional[int] = None

@dataclass(kw_only=True)
class PitchingByDayOfWeekPlayOffs(Stats, SimplePitching):
    """
    A class to represent a byDayOfWeekPlayoffs stat for a pitcher

    Attributes
    ----------
    daysofweek : int
    daysofweek : int
    numteams : int

    """
    type_ = [ 'byDayOfWeekPlayoffs' ]
    dayofweek: Optional[int] = None

@dataclass(kw_only=True)
class PitchingHomeAndAway(Stats, SimplePitching):
    """
    A class to represent a homeAndAway stat for a pitcher

    Attributes
    ----------
    ishome : bool

    """
    type_ = [ 'homeAndAway' ]
    ishome: bool

@dataclass(kw_only=True)
class PitchingHomeAndAwayPlayoffs(Stats, SimplePitching):
    """
    A class to represent a homeAndAwayPlayoffs stat for a pitcher

    Attributes
    ----------
    ishome : bool
    """
    type_ = [ 'homeAndAwayPlayoffs' ]
    ishome: bool

@dataclass(kw_only=True)
class PitchingWinLoss(Stats, SimplePitching):
    """
    A class to represent a winLoss stat for a pitcher

    Attributes
    ----------
    iswin : bool
    """
    type_ = [ 'winLoss' ]
    iswin: bool

@dataclass(kw_only=True)
class PitchingWinLossPlayoffs(Stats, SimplePitching):
    """
    A class to represent a winLossPlayoffs stat for a pitcher

    Attributes
    ----------
    iswin : bool
    """
    type_ = [ 'winLossPlayoffs' ]
    iswin: bool

@dataclass(kw_only=True)
class PitchingRankings(Stats, SimplePitching):
    """
    A class to represent a rankings stat for a pitcher

    Attributes
    ----------
    gametype : str
    """
    type_ = [ 'rankings' ]

@dataclass(kw_only=True)
class PitchingRankings(Stats, SimplePitching):
    """
    A class to represent a rankings stat for a pitcher

    Attributes
    ----------
    gametype : str
    """
    type_ = [ 'rankingsByYear' ]

@dataclass(kw_only=True)
class PitchingOpponentsFaced(Stats):
    """
    A class to represent a opponentsFaced stat for a pitcher

    Attributes
    ----------
    gametype : str
    group : str
    pitch : Person
    batter : Person
    battingteam : Team
    """
    type_ = [ 'opponentsFaced' ]
    group: str
    pitcher: Union[Person, dict]
    batter: Union[Person, dict]
    battingteam: Union[Team, dict]

@dataclass(kw_only=True)
class PitchingExpectedStatistics(Stats):
    """
    A class to represent a excepted statistics statType: expectedStatistics.
    """
    """
    Attributes
    ----------
    avg : str
    slg : str
    woba : str
    wobaCon : str
    rank : int
    """
    type_ = [ 'expectedStatistics' ]
    avg : str
    slg : str
    woba : str
    wobacon : str
    rank : Optional[int] = None

#https://statsapi.mlb.com/api/v1/people?personIds=543243,622608,594965,571927,548389,571945,656427,500779&season=2019&hydrate=stats(group=[pitching],type=[vsTeam],opposingTeamId=158,season=2019)
#https://statsapi.mlb.com/api/v1/people?personIds=543243,622608,594965,571927,548389,571945,656427,500779&season=2019&hydrate=stats(group=[pitching],type=[vsTeamTotal],opposingTeamId=158,season=2019)