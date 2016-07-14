import datetime
import hooke

concept_attribs = {
    'id'          : 'myconcept',
    'description' : 'This is my concept description.',
}

def add_concept( session ):
    concept = hooke.model.Concept( **concept_attribs )
    session.add( concept )
    return

def query_concept( session ):
    concept = session.query( hooke.model.Concept ).filter( hooke.model.Concept.id == concept_attribs['id'] ).one()
    return concept

def delete_concept( session ):
    concept = query_concept( session )
    session.delete( concept )
    return

palette_attribs = {
    'id'          : 'mypalette',
    'description' : 'This is my palette description.',
}

def add_palette( session ):
    palette = hooke.model.Palette( **palette_attribs )
    session.add( palette )
    return

def query_palette( session ):
    palette = session.query( hooke.model.Palette ).filter( hooke.model.Palette.id == palette_attribs['id'] ).one()
    return palette

def delete_palette( session ):
    palette = query_palette( session )
    session.delete( palette )
    return

ingredient_attribs = {
    'id'          : 'myingredient',
    'description' : 'This is my ingredient description.',
}

def add_ingredient( session ):
    ingredient = hooke.model.Ingredient( **ingredient_attribs )
    session.add( ingredient )
    return

def query_ingredient( session ):
    ingredient = session.query( hooke.model.Ingredient ).filter( hooke.model.Ingredient.id == ingredient_attribs['id'] ).one()
    return ingredient

def delete_ingredient( session ):
    ingredient = query_ingredient( session )
    session.delete( ingredient )
    return

concept_palette_attribs = {
    'concept_id' : concept_attribs['id'],
    'palette_id' : palette_attribs['id'],
    'notes'      : 'These are my concept-palette notes.',
}

def add_concept_palette( session ):
    add_concept( session )
    add_palette( session )
    concept_palette = hooke.model.ConceptPalette( **concept_palette_attribs )
    session.add( concept_palette )
    return

def query_concept_palette( session ):
    concept_palette = session.query( hooke.model.ConceptPalette ).filter(
        hooke.model.ConceptPalette.concept_id == concept_palette_attribs['concept_id'],
        hooke.model.ConceptPalette.palette_id == concept_palette_attribs['palette_id']
    ).one()
    return concept_palette

def delete_concept_palette( session ):
    concept_palette = query_concept_palette( session )
    session.delete( concept_palette )
    delete_palette( session )
    delete_concept( session )
    return

palette_ingredient_attribs = {
    'palette_id'    : palette_attribs['id'],
    'ingredient_id' : ingredient_attribs['id'],
    'flavor'        : hooke.model.Flavor.include,
}

def add_palette_ingredient( session ):
    add_palette( session )
    add_ingredient( session )
    palette_ingredient = hooke.model.PaletteIngredient( **palette_ingredient_attribs )
    session.add( palette_ingredient )
    return

def query_palette_ingredient( session ):
    palette_ingredient = session.query( hooke.model.PaletteIngredient ).filter(
        hooke.model.PaletteIngredient.palette_id == palette_ingredient_attribs['palette_id'],
        hooke.model.PaletteIngredient.ingredient_id == palette_ingredient_attribs['ingredient_id']
    ).one()
    return palette_ingredient

def delete_palette_ingredient( session ):
    palette_ingredient = query_palette_ingredient( session )
    session.delete( palette_ingredient )
    delete_ingredient( session )
    delete_palette( session )
    return

history_attribs = {
    'id'         : 'myhistory',
    'started_on' : datetime.datetime.now(),
    'concept_id' : concept_attribs['id'],
    'palette_id' : palette_attribs['id'],
    'state'      : hooke.model.State.active,
}

def add_history( session ):
    add_concept_palette( session )
    history = hooke.model.History( **history_attribs )
    session.add( history )
    return

def query_history( session ):
    history = session.query( hooke.model.History ).filter( hooke.model.History.id == history_attribs['id'] ).one()
    return history

def delete_history( session ):
    history = query_history( session )
    session.delete( history )
    delete_concept_palette( session )
    return

player_attribs = {
    'id'         : 'myplayer',
    'password'   : 'mypassword',
    'first_name' : 'My',
    'last_name'  : 'Player',
    'email'      : 'myplayer@nowhere.com',
}

def add_player( session ):
    player = hooke.model.Player( **player_attribs )
    session.add( player )
    return

def query_player( session ):
    player = session.query( hooke.model.Player ).filter( hooke.model.Player.id == player_attribs['id'] ).one()
    return player

def delete_player( session ):
    player = query_player( session )
    session.delete( player )
    return

history_player_attribs = {
    'history_id' : history_attribs['id'],
    'player_id'  : player_attribs['id'],
}

def add_history_player( session ):
    add_history( session )
    add_player( session )
    history_player = hooke.model.HistoryPlayer( **history_player_attribs )
    session.add( history_player )
    return

def query_history_player( session ):
    history_player = session.query( hooke.model.HistoryPlayer ).filter(
        hooke.model.HistoryPlayer.history_id == history_player_attribs['history_id'],
        hooke.model.HistoryPlayer.player_id == history_player_attribs['player_id']
    ).one()
    return history_player

def delete_history_player( session ):
    history_player = query_history_player( session )
    session.delete( history_player )
    delete_player( session )
    delete_history( session )
    return
