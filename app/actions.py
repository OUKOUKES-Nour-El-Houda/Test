from sqlalchemy.orm import Session
from . import models, schemas
from .utils.pokeapi import get_pokemon_name

def get_trainer(database: Session, trainer_id: int):
    """
    Retrieve a trainer from the database using their unique identifier (ID).

    Parameters:
    - database (Session): The database session used for querying.
    - trainer_id (int): The unique ID of the trainer.

    Returns:
    - Trainer: The trainer object if found, else None.
    """
    return database.query(models.Trainer).filter(models.Trainer.id == trainer_id).first()


def get_trainer_by_name(database: Session, name: str):
    """
    Retrieve a list of trainers from the database based on their name.

    Parameters:
    - database (Session): The database session used for querying.
    - name (str): The name of the trainer to search for.

    Returns:
    - List[Trainer]: A list of trainer objects matching the name.
    """
    return database.query(models.Trainer).filter(models.Trainer.name == name).all()


def get_trainers(database: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of all trainers from the database with pagination support.

    Parameters:
    - database (Session): The database session used for querying.
    - skip (int, optional): The number of trainers to skip (default is 0).
    - limit (int, optional): The maximum number of trainers to retrieve (default is 100).

    Returns:
    - List[Trainer]: A list of trainer objects.
    """
    return database.query(models.Trainer).offset(skip).limit(limit).all()


def create_trainer(database: Session, trainer: schemas.TrainerCreate):
    """
    Create a new trainer and save it to the database.

    Parameters:
    - database (Session): The database session used for committing.
    - trainer (schemas.TrainerCreate): The trainer data to create a new trainer.

    Returns:
    - Trainer: The newly created trainer object.
    """
    db_trainer = models.Trainer(name=trainer.name, birthdate=trainer.birthdate)
    database.add(db_trainer)
    database.commit()
    database.refresh(db_trainer)
    return db_trainer


def add_trainer_pokemon(database: Session, pokemon: schemas.PokemonCreate, trainer_id: int):
    """
    Create a new pokemon, link it to a trainer, and save it to the database.

    Parameters:
    - database (Session): The database session used for committing.
    - pokemon (schemas.PokemonCreate): The pokemon data to create a new pokemon.
    - trainer_id (int): The ID of the trainer to associate the pokemon with.

    Returns:
    - Pokemon: The newly created pokemon object linked to the trainer.
    """
    db_item = models.Pokemon(
        **pokemon.dict(), name=get_pokemon_name(pokemon.api_id), trainer_id=trainer_id)
    database.add(db_item)
    database.commit()
    database.refresh(db_item)
    return db_item


def add_trainer_item(database: Session, item: schemas.ItemCreate, trainer_id: int):
    """
    Create a new item, link it to a trainer, and save it to the database.

    Parameters:
    - database (Session): The database session used for committing.
    - item (schemas.ItemCreate): The item data to create a new item.
    - trainer_id (int): The ID of the trainer to associate the item with.

    Returns:
    - Item: The newly created item object linked to the trainer.
    """
    db_item = models.Item(**item.dict(), trainer_id=trainer_id)
    database.add(db_item)
    database.commit()
    database.refresh(db_item)
    return db_item


def get_items(database: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of all items from the database with pagination support.

    Parameters:
    - database (Session): The database session used for querying.
    - skip (int, optional): The number of items to skip (default is 0).
    - limit (int, optional): The maximum number of items to retrieve (default is 100).

    Returns:
    - List[Item]: A list of item objects.
    """
    return database.query(models.Item).offset(skip).limit(limit).all()


def get_pokemon(database: Session, pokemon_id: int):
    """
    Retrieve a pokemon from the database using its unique identifier (ID).

    Parameters:
    - database (Session): The database session used for querying.
    - pokemon_id (int): The unique ID of the pokemon.

    Returns:
    - Pokemon: The pokemon object if found, else None.
    """
    return database.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()


def get_pokemons(database: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of all pokemons from the database with pagination support.

    Parameters:
    - database (Session): The database session used for querying.
    - skip (int, optional): The number of pokemons to skip (default is 0).
    - limit (int, optional): The maximum number of pokemons to retrieve (default is 100).

    Returns:
    - List[Pokemon]: A list of pokemon objects.
    """
    return database.query(models.Pokemon).offset(skip).limit(limit).all()
