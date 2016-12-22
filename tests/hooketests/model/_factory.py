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
    session.commit()
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
    session.commit()
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
    session.commit()
    return

concept_palette_attribs = {
    'concept_id' : concept_attribs['id'],
    'palette_id' : palette_attribs['id'],
    'title'      : 'My Concept Palette',
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
    session.commit()
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
    session.commit()
    delete_ingredient( session )
    delete_palette( session )
    return

history_attribs = {
    'id'         : 'myhistory',
    'title'      : 'My History',
    'concept_id' : concept_attribs['id'],
    'palette_id' : palette_attribs['id'],
    'started_on' : datetime.datetime.now(),
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
    session.commit()
    delete_concept_palette( session )
    return

player_attribs = {
    'id'         : 'myplayer',
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
    session.commit()
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
    session.commit()
    delete_player( session )
    delete_history( session )
    return

period_attribs = {
    'id'          : 'mydetachedperiod',
    'history_id'  : history_attribs['id'],
    'placement'   : hooke.model.Placement.detached,
    'description' : 'This is my detached period description.',
    'tone'        : hooke.model.Tone.light,
}

def add_period( session ):
    add_history( session )
    period = hooke.model.Period( **period_attribs )
    session.add( period )
    return

def query_period( session ):
    period = session.query( hooke.model.Period ).filter( hooke.model.Period.id == period_attribs['id'] ).one()
    return period

def delete_period( session ):
    period = query_period( session )
    session.delete( period )
    session.commit()
    delete_history( session )
    return

initial_period_attribs = {
    'id'             : 'myinitialperiod',
    'history_id'     : history_attribs['id'],
    'placement'      : hooke.model.Placement.initial,
    'description'    : 'This is my initial period description.',
    'tone'           : hooke.model.Tone.light,
    'next_period_id' : 'mymedialperiod',
}

medial_period_attribs = {
    'id'             : 'mymedialperiod',
    'history_id'     : history_attribs['id'],
    'placement'      : hooke.model.Placement.medial,
    'description'    : 'This is my medial period description.',
    'tone'           : hooke.model.Tone.dark,
    'prev_period_id' : 'myinitialperiod',
    'next_period_id' : 'myfinalperiod',
}

final_period_attribs = {
    'id'             : 'myfinalperiod',
    'history_id'     : history_attribs['id'],
    'placement'      : hooke.model.Placement.final,
    'description'    : 'This is my final period description.',
    'tone'           : hooke.model.Tone.light,
    'prev_period_id' : 'mymedialperiod',
}

def add_initial_period( session, composed = False ):
    if composed:
        add_history( session )
    initial_period = hooke.model.InitialPeriod( **initial_period_attribs )
    session.add( initial_period )
    return

def query_initial_period( session ):
    period = session.query( hooke.model.InitialPeriod ).filter( hooke.model.InitialPeriod.id == initial_period_attribs['id'] ).one()
    return period

def delete_initial_period( session, composed = False ):
    initial_period = query_initial_period( session )
    session.delete( initial_period )
    session.commit()
    if composed:
        delete_history( session )
    return

def add_medial_period( session, composed = False ):
    if composed:
        add_history( session )
    medial_period = hooke.model.MedialPeriod( **medial_period_attribs )
    session.add( medial_period )
    return

def query_medial_period( session ):
    period = session.query( hooke.model.MedialPeriod ).filter( hooke.model.MedialPeriod.id == medial_period_attribs['id'] ).one()
    return period

def delete_medial_period( session, composed = False ):
    medial_period = query_medial_period( session )
    session.delete( medial_period )
    session.commit()
    if composed:
        delete_history( session )
    return

def add_final_period( session, composed = False ):
    if composed:
        add_history( session )
    final_period = hooke.model.FinalPeriod( **final_period_attribs )
    session.add( final_period )
    return

def query_final_period( session ):
    period = session.query( hooke.model.FinalPeriod ).filter( hooke.model.FinalPeriod.id == final_period_attribs['id'] ).one()
    return period

def delete_final_period( session, composed = False ):
    final_period = query_final_period( session )
    session.delete( final_period )
    session.commit()
    if composed:
        delete_history( session )
    return

