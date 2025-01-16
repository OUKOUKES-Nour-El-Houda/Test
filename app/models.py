from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from .sqlite import Base
from sqlalchemy.types import JSON  # Import de JSON

class Trainer(Base):
    """
    Class representing a Pokemon trainer.
    Attributes:
        id (int): The unique identifier of the trainer.
        name (str): The name of the trainer.
        birthdate (Date): The birthdate of the trainer.
    """
    __tablename__ = "trainers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birthdate = Column(Date)

    inventory = relationship("Item", back_populates="trainer")
    pokemons = relationship("Pokemon", back_populates="trainer")


class Pokemon(Base):
    """
    Class representing a Pokemon.
    Attributes:
        id (int): The unique identifier of the Pokemon.
        api_id (int): The Pokemon's ID in the PokeAPI.
        name (str): The name of the Pokemon.
        custom_name (str): The custom name given to the Pokemon by the trainer.
        trainer_id (int): The ID of the trainer who owns the Pokemon.
    """
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    api_id = Column(Integer, index=True)
    name = Column(String, index=True)
    custom_name = Column(String, index=True)
    trainer_id = Column(Integer, ForeignKey("trainers.id"))

    trainer = relationship("Trainer", back_populates="pokemons")


class Item(Base):
    """
    Class representing an item in a Pokemon trainer's inventory.
    Attributes:
        id (int): The unique identifier of the item.
        name (str): The name of the item.
        description (str): A description of the item.
        trainer_id (int): The ID of the trainer who owns the item.
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    trainer_id = Column(Integer, ForeignKey("trainers.id"))

    trainer = relationship("Trainer", back_populates="inventory")
