import os

# bot token
BOT_TOKEN: str = ""

# telegram user id
admins: list = []

allCommands = dict()

volumeCommands = {
    "-10%": "nircmd.exe changesysvolume -6553",
    "+10%": "nircmd.exe changesysvolume 6553",
    "Mute / UnMute": "nircmd.exe mutesysvolume 2",
    "0%": "nircmd.exe setsysvolume 0",
    "50%": "nircmd.exe setsysvolume 32767",
    "100%": "nircmd.exe setsysvolume 65535"
}

allCommands.update(volumeCommands)

powerCommands = {
    "Shutdown": "shutdown -s -t 0",
    "Hibernation": "psshutdown.exe -d -t 0 -accepteula",
    "Timer to shutdown": "shutdown -s -t",
    "Don't shutdown": "shutdown -a"
}

allCommands.update(powerCommands)

appsCommands = {
    "Spotify": "C:\\Users\\farneser\\AppData\\Roaming\\Spotify\\Spotify.exe"
}

allCommands.update(appsCommands)
