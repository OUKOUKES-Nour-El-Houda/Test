from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app import actions, schemas
from app.utils.utils import get_db
from app.utils.pokeapi import get_pokemon_stats, get_pokemon_name
import random
from app import models 
from app.routers.trainers import get_trainer

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons
@router.get("/random-pokemons", response_model=List[schemas.Pokemon])
def random_pokemons(database: Session = Depends(get_db)):
    """
    Endpoint pour récupérer 3 pokémons aléatoires avec leurs stats.
    """
    all_pokemons = database.query(models.Pokemon).all()

    # Sélectionner 3 Pokémon aléatoires
    random_pokemons = random.sample(all_pokemons, 3)
    result=[]
    for pokemon in random_pokemons:
        stats = get_pokemon_stats(pokemon.api_id)  # Récupérer les stats via l'API
        result.append({
            "id": pokemon.id,
            "custom_name": pokemon.custom_name,
            "name": pokemon.name,
            "api_id": pokemon.api_id,
            "trainer_id": pokemon.trainer_id,  # Assurez-vous que trainer_id est renvoyé comme attendu
            "stats": stats
        })
    return result
    

    # pokemons = []

    # for pokemon_id in random_ids:
    #     # Fetch stats and name from external service or database
    #     name = get_pokemon_name(pokemon_id)
    #     stats = get_pokemon_stats(pokemon_id)
    #     trainer_id= get_trainer(trainer_id)

    #     # Create a Pokémon dictionary and append to the list
    #     pokemon = schemas.Pokemon(
    #         id=pokemon_id,
    #         name=name,
    #         trainer_id=trainer_id  # Ensure your schema includes this field
    #     )
    #     pokemons.append(pokemon)

    # return pokemons