from fastapi import APIRouter
from app.utils.pokeapi import battle_pokemon
router= APIRouter()

@router.get("/")
def get_battle(first_id:int, second_id: int):
    """
        Endpoint to battle two pokemons by their API IDs
    """
    result = battle_pokemon(first_id, second_id)
    return result