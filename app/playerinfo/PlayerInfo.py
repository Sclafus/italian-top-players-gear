from dataclasses import astuple, dataclass

@dataclass
class PlayerInfo:
    rank: int
    pp: int
    username: str
    city: str
    play_style: str
    tap_style: str
    tablet_mouse: str
    area_filter_sensitivity: str
    grip: str
    keyboard: str
    switch: str
    osu_resolution: str
    skin: str


    def __iter__(self):
        return iter(astuple(self))   