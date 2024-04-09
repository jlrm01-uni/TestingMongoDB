import os
from mongoengine import *
from dotenv import load_dotenv

load_dotenv()

# Esto es para demostrar git
# Esto es en el otro branch

PASSWORD = os.getenv("PASSWORD")
url = f"mongodb+srv://jlrm01_creatures:{PASSWORD}@cluster0.irk6d.mongodb.net/CreatureDen?retryWrites=true&w=majority&appName=Cluster0"

connect(host=url)


class Creature(Document):
    name = StringField(required=True)
    image = StringField()

    hp = IntField(default=100)
    attack = IntField()
    defense = IntField()

    special_ability = StringField()
    description = StringField()
    lore = StringField()

    meta = {'strict': False}

def create_creatures():
    Creature.drop_collection()
    c = Creature(name="Don Ramon",
                 image="76",
                 hp=40,
                 attack=30,
                 defense=20,
                 special_ability="blah",
                 description="very cute",
                 lore="looking for One Piece")
    c.save()

    c = Creature(name="Freiren",
                 image="76",
                 hp=140,
                 attack=30,
                 defense=20,
                 special_ability="blah",
                 description="very cute",
                 lore="walking far far away")
    c.save()

    c = Creature(name="Luffy",
                 image="76",
                 hp=140,
                 attack=30,
                 defense=20,
                 special_ability="blah",
                 description="straw hat",
                 lore="king of the pirates")
    c.save()


if __name__ == "__main__":
    create_creatures()
