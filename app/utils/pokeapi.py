import requests

base_url = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    data= get_pokemon_data(api_id)
    return data['name']

def get_pokemon_stats(api_id):
    """
        Get pokemon stats from the API pokeapi
    """
    data = get_pokemon_data(api_id)
    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    return stats

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{base_url}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """
    # premierPokemon = get_pokemon_data(first_api_id)
    # secondPokemon = get_pokemon_data(second_api_id)
    # battle_result = 0
    # return premierPokemon if battle_result > 0 else secondPokemon if battle_result < 0 else {'winner': 'draw'}
    first_stats = get_pokemon_stats(first_api_id)
    second_stats = get_pokemon_stats(second_api_id)
    battle_result = battle_compare_stats(first_stats, second_stats)

    if battle_result > 0:
        winner = get_pokemon_name(first_api_id)
    elif battle_result < 0:
        winner = get_pokemon_name(second_api_id)
    else:
        winner = "draw"

    return {
        "first_pokemon":{
            "name": get_pokemon_name(first_api_id),
            "stats":first_stats
        },
        
        "second_pokemon":{
            "name": get_pokemon_name(second_api_id),
            "stats":second_stats
        },
        "winner": winner
    }

def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
        Returns:
            - Positive value if first_pokemon_stats wins
            - Negative value if second_pokemon_stats wins
            - Zero if it's a draw
    """
    score = 0
    for stat in first_pokemon_stats:
        if first_pokemon_stats[stat] > second_pokemon_stats[stat]:
            score += 1
        elif first_pokemon_stats[stat] < second_pokemon_stats[stat]:
            score -= 1
    return score

