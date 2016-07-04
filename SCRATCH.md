from sqlalchemy import create_engine
engine = create_engine( 'sqlite:///:memory:', echo=True )

import Hooke
Hooke.model.HookeModelBase.metadata.create_all( engine )

from sqlalchemy.orm import sessionmaker
Session = sessionmaker( bind = engine )
session = Session()

p = Hooke.model.Palette( id = 'mypalette', description = 'This is my palette description.' )
session.add( p )
session.commit()

i = Hooke.model.Ingredient( id = 'myingredient', flavor = Hooke.model.Flavor.include, statement = 'This is my ingredient statement.' )
session.add( i )
session.commit()

pi = Hooke.model.PaletteIngredient( palette_id = p.id, ingredient_id = i.id )
session.add( pi )
session.commit()
