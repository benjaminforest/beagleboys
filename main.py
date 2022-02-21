from shared import shared

PROJECTS = {
    'ProjetTradingPythonPOO':{"path":('bot', 'Bot')},
}

shared.initialize_projects(PROJECTS)
shared.play_candle_file("candle_sample.txt", PROJECTS)
shared.display_gains(PROJECTS)
