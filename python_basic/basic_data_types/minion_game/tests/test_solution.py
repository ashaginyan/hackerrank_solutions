from solution import minion_game

def test_minion_game():
    assert minion_game('BANANA') == 'Stuart 12'
    assert minion_game('ANA') == 'Kevin 4'
    assert minion_game('CHUPAKABRA') == 'Stuart 36'


def test_minion_game_constr():
    assert minion_game('B') == 'Stuart 1'
    assert minion_game('A') == 'Kevin 1'