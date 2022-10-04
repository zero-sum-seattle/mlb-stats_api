﻿from typing import List, Dict, Union, Any, Optional
from .attributes import PitchHand, PrimaryPosition, BatSide
from mlbstatsapi import MlbObject
from mlbstatsapi.models.stats import Stats
from dataclasses import dataclass, field


@dataclass
class Person(MlbObject):
    """
    A class to represent a Person.

    Attributes
    ----------
    id : int
        id number of the person
    full_name: str
        full_name of the person
    """

    id: int
    link: str
    fullName: str
    mlb_class: Optional[str] = "people"
    primaryPosition: Union[PrimaryPosition, Dict[str, Any]] = field(default_factory=dict)
    pitchHand: Union[PitchHand, Dict[str, Any]] = field(default_factory=dict)
    batSide: Union[BatSide, Dict[str, Any]] = field(default_factory=dict)
    stats: Union[Stats, list] = field(default_factory=list)
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    primaryNumber: Optional[str] = None
    birthDate: Optional[str] = None
    currentTeam: Optional[str] = None
    currentAge: Optional[str] = None
    birthCity: Optional[str] = None
    birthStateProvince: Optional[str] = None
    height: Optional[str] = None
    weight: Optional[int] = None
    active: Optional[bool] = None
    useName: Optional[str] = None
    middleName: Optional[str] = None
    boxscoreName: Optional[str] = None
    nickName: Optional[str] = None
    draftYear: Optional[int] = None
    mlbDebutDate: Optional[str] = None
    nameFirstLast: Optional[str] = None
    nameSlug: Optional[str] = None
    firstLastName: Optional[str] = None
    lastFirstName: Optional[str] = None
    lastInitName: Optional[str] = None
    initLastName: Optional[str] = None
    fullFMLName: Optional[str] = None
    fullLFMName: Optional[str] = None
    birthCountry: Optional[str] = None
    pronunciation: Optional[str] = None
    strikeZoneTop: Optional[float] = None
    strikeZoneBottom: Optional[float] = None
    nameTitle: Optional[str] = None
    gender: Optional[str] = None
    isPlayer: Optional[bool] = None
    isVerified: Optional[bool] = None
    nameMatrilineal: Optional[str] = None
    deathDate: Optional[str] = None
    deathCity: Optional[str] = None
    deathCountry: Optional[str] = None

    def __post_init__(self):
        self.primaryPosition = PrimaryPosition(**self.primaryPosition) if self.primaryPosition else self.primaryPosition
        self.pitchHand = PitchHand(**self.pitchHand) if self.pitchHand else self.pitchHand
        self.batSide = BatSide(**self.batSide) if self.batSide else self.batSide
        self.stats = [ Stats(**stat) for stat in self.stats] if self.stats else self.stats

     