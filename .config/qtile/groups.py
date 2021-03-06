import re
from itertools import chain
from typing import List, Tuple, Union

from libqtile.config import Match, Group

_default_groups = [
    Group(name="1", label="dev", layout="max"),
    Group(name="2", label="www", layout="max"),
    Group(name="3", label="sys", layout="max"),
    Group(name="4", label="doc", layout="max"),
    Group(name="5", label="virt", layout="max"),
    Group(name="6", label="game", layout="max"),
    Group(name="7", label="chat", layout="max"),
]

dev_group, www_group, sys_group, doc_group, virt_group, game_group, chat_group = _default_groups


class _WindowMatch:

    def __init__(self,
                 group: Union[str, int],
                 match_rule: Match):
        self.group = group
        self.match_rule = match_rule


_games_staff: List[str] = [
    "lutris",
    "genshinimpact.exe",
    r"steam_app*",
    "Steam",
    "Paradox Launcher",
    "Cities.x64",
    "mb_warband_linux",
    "hl2_linux",
    r"^([Mm]inecraft)(.+)",
    "Shogun2",
    "openttd",
    r"War Thunder*"
]

_web_browsers: List[str] = [
    "Chromium",
    "qutebrowser",
    r"[fF]irefox*",
    r"[Nn]avigator",
    r"[tT]or*",
    r"Vivaldi-*",
]

_dev_staff: List[str] = [
    "Emacs",
    "Code",
    "jetbrains-*",
    "code-oss"
]

_terminals: List[str] = [
    r"[tT]erminator"
]

_science_staff: List[str] = [
    "Boincmgr",
    "Virt-manager",
    "VirtualBox Manager"
]

_music_staff: List[str] = [
    "Qmmp",
    "player",
    r"*Shortwave$",
    "Rhythmbox",
]

matches: List[_WindowMatch] = [
    _WindowMatch(group="7", match_rule=Match(wm_class="discord")),
    _WindowMatch(group="5", match_rule=Match(wm_class=re.compile(r"[tT]hunderbird"))),
    _WindowMatch(group="5", match_rule=Match(wm_class="Evince")),
    _WindowMatch(group="3", match_rule=Match(wm_class="Org.gnome.Nautilus")),
    _WindowMatch(group="1", match_rule=Match(wm_class="Postman")),
    _WindowMatch(group="7", match_rule=Match(wm_class=re.compile("[sS]ignal*"))),
    _WindowMatch(group="4", match_rule=Match(wm_class=re.compile("[kK]rita*"))),
]


def get_default_groups() -> List[Group]:
    for group in _default_groups:
        group.matches = _get_matches_list(group.name)

    return _default_groups


def _get_wm_name(wm_name: str) -> Union[str, re.Pattern]:
    """
    Get Window name or Window name regex

    :param wm_name:
    :return:
    """
    try:
        return re.compile(wm_name)
    except re.error:
        return wm_name


def _map_wm_names(group: Group, wm_names_list: List[str]):
    return map(lambda wm_name: _WindowMatch(group=group.name,
                                            match_rule=Match(wm_class=_get_wm_name(wm_name))), wm_names_list)


def _get_windows_matches() -> List[_WindowMatch]:
    """
    Create list of _WindowMatch object. WindowMatch object include group id and Match,
    that will be used to
    :return:
    """
    _group_matches: List[Tuple[Group, List[str]]] = [
        (dev_group, _dev_staff),
        (www_group, _web_browsers),
        (sys_group, _terminals),
        (game_group, _games_staff),
        (virt_group, _science_staff),
        (doc_group, _music_staff)
    ]

    window_matches_list = map(lambda group_match: _map_wm_names(group_match[0], group_match[1]), _group_matches)
    flatten_group_matches: List[_WindowMatch] = list(chain(*window_matches_list))

    return matches + flatten_group_matches


def _get_matches_list(group_name: str) -> List[Match]:
    windows_matches_list: List[_WindowMatch] = _get_windows_matches()
    filtered_windows_matches_list: filter[_WindowMatch] = filter(lambda window_match: window_match.group == group_name,
                                                                 windows_matches_list)

    return list(map(lambda window_match: window_match.match_rule, filtered_windows_matches_list))
