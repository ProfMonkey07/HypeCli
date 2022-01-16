#!/usr/bin/python3
import requests, sys, time
import pytermgui as gui
from pytermgui import WindowManager, Window
# this program will be used to gather data on players from the Hypixel minecraft server via command line
# keep in mind I have no affiliation with the Hypixel server
#you will need to add you api key here
apikey = ""
username = ""
manager = WindowManager()
#setting up windows that will be opened later
#these here are all of the games for the leaderboards

UHC = (
    Window(min_width=50)
    +"Here are the leaderboard options for UHC"
    )
SURVIVAL_GAMES = (
    Window(min_width=50)
    +"Here are the leaderboard options for Survival Games")
QUAKECRAFT = (
    Window(min_width=50)
    +"Here are the leaderboard options for QuakeCraft")
TNTGAMES = (
    Window(min_width=50)
    +"Here are the leaderboard options for TNT Games")
WALLS = (
    Window(min_width=50)
    +"Here are the leaderboard options for Walls")
MURDER_MYSTERY = (
    Window(min_width=50)
    +"Here are the leaderboard options for Murder Mystery")
BUILD_BATTLE = (
    Window(min_width=50)
    +"Here are the leaderboard options for Build Battle")
ARCADE = (
    Window(min_width=50)
    +"Here are the leaderboard options for Arcade")
BEDWARS = (
    Window(min_width=50)
    +"Here are the leaderboard options for BedWars")
DUELS = (
    Window(min_width=50)
    +"Here are the leaderboard options for Duels")
ARENA = (
    Window(min_width=50)
    +"Here are the leaderboard options for Arena")
SPEED_UHC = (
    Window(min_width=50)
    +"Here are the leaderboard options for Speed UHC")
SKYWARS = (
    Window(min_width=50)
    +"Here are the leaderboard options for SkyWars")
#sorry for the length but I couldn't think of a better way to do this part
LeaderboardMenu = (
    Window(min_width=50)
    +"Use this menu to navigate Leaderboards"
    + ["UHC", lambda *_: manager.add(UHC.copy().center())]
    + ["SURVIVAL_GAMES", lambda *_: manager.add(UHC.copy().center())] 
    + ["QUAKECRAFT", lambda *_: manager.add(SURVIVAL_GAMES.copy().center())]
    + ["TNTGAMES", lambda *_: manager.add(TNTGAMES.copy().center())]
    + ["WALLS", lambda *_: manager.add(WALLS.copy().center())]
    + ["MURDER_MYSTERY", lambda *_: manager.add(MURDER_MYSTERY.copy().center())]
    + ["BUILD_BATTLE", lambda *_: manager.add(BUILD_BATTLE.copy().center())]
    + ["ARCADE", lambda *_: manager.add(ARCADE.copy().center())]
    + ["BEDWARS", lambda *_: manager.add(BEDWARS.copy().center())]
    + ["DUELS", lambda *_: manager.add(DUELS.copy().center())]
    + ["ARENA", lambda *_: manager.add(ARENA.copy().center())]
    + ["SPEED_UHC", lambda *_: manager.add(SPEED_UHC.copy().center())]
    + ["SKYWARS", lambda *_: manager.add(SKYWARS.copy().center())]
    + ["exit", lambda *_: sys.exit(0)]
)

BedWars = (Window(min_width=50))
SkyWars = (Window(min_width=50))
Duels = (Window(min_width=50))
Build_Battle = (Window(min_width=50))
uhc = (Window(min_width=50))

ProfileMenu = (
    Window(min_width=50)
    +"Use this menu to navigate various stats"
    + ["BedWars", lambda *_: manager.add(BedWars.copy().center())]
    + ["SkyWars", lambda *_: manager.add(SkyWars.copy().center())]
    + ["Duels", lambda *_: manager.add(Duels.copy().center())]
    + ["Build Battle", lambda *_: manager.add(Build_Battle.copy().center())]
    + ["UHC", lambda *_: manager.add(uhc.copy().center())]
    + ["exit", lambda *_: sys.exit(0)]
)

pets = (Window(min_width=50))

coins = (Window(min_width=50))

FarmingS = (Window(min_width=50))
MiningS = (Window(min_width=50))
CombatS = (Window(min_width=50))
ForagingS = (Window(min_width=50))
FishingS= (Window(min_width=50))
EnchantingS= (Window(min_width=50))
AlchemyS= (Window(min_width=50))
TamingS= (Window(min_width=50))
DungeonS = (Window(min_width=50))

skills = (
    Window(min_width=50)
    + ["UHC", lambda *_: manager.add(uhc.copy().center())]
    + ["UHC", lambda *_: manager.add(uhc.copy().center())]
    + ["UHC", lambda *_: manager.add(uhc.copy().center())]
    + ["UHC", lambda *_: manager.add(uhc.copy().center())]
    + ["UHC", lambda *_: manager.add(uhc.copy().center())]

)
FarmingC = (Window(min_width=50))
MiningC = (Window(min_width=50))
CombatC = (Window(min_width=50))
ForagingC = (Window(min_width=50))
FishingC = (Window(min_width=50))
BossC = (Window(min_width=50))

collections = (Window(min_width=50))

SkyblockMenu = (
    Window(min_width=50)
    +"Use this menu to navigate Skyblock Profiles"
    +gui.InputField(prompt="What profile do you wish to view")
    + ["exit", lambda *_: sys.exit(0)]
)
Mainmenu = (
    Window(min_width=50)
    + "welcome to HyConsole"
    + "use the gui to navigate player stats and leaderboards"
    + ["Profile", lambda *_: manager.add(ProfileMenu.copy().center())]
    + ["Leaderboard", lambda *_: manager.add(LeaderboardMenu.copy().center())]
    + ["Skyblock", lambda *_: manager.add(SkyblockMenu.copy().center())]
    + ["exit", lambda *_: sys.exit(0)]
)
#starting the window
args = []
for arg in sys.argv:
    args.append(arg)
print(args)
username = args[2]
print(username)
playerdata = requests.get(
    url = "https://api.hypixel.net/player", params = {
        "key": apikey,
        "name": username}).json()
uuid = requests.get(url = "https://api.mojang.com/users/profiles/minecraft/" + username + "?").json()
uuid = str(uuid["id"])
skyblockdata = requests.get(
    url = "https://api.hypixel.net/skyblock", params = {
        "key": apikey,
        "uuid": uuid}).json()
leaderboarddata = requests.get(
                        url = "https://api.hypixel.net/leaderboards", params = {
                                "key": apikey
                        }
                ).json()

        
manager.add(Mainmenu)
manager.run()