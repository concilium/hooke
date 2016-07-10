import datetime
import Hooke

concept_attribs = {
    'id'          : 'myconcept',
    'description' : 'This is my concept description.',
}

palette_attribs = {
    'id'          : 'mypalette',
    'description' : 'This is my palette description.',
}

ingredient_attribs = {
    'id'          : 'myingredient',
    'description' : 'This is my ingredient description.',
}

concept_palette_attribs = {
    'concept_id' : concept_attribs['id'],
    'palette_id' : palette_attribs['id'],
    'notes'      : 'These are my concept-palette notes.',
}

palette_ingredient_attribs = {
    'palette_id'    : palette_attribs['id'],
    'ingredient_id' : ingredient_attribs['id'],
    'flavor'        : Hooke.model.Flavor.include,
}

history_attribs = {
    'id'         : 'myhistory',
    'started_on' : datetime.datetime.now(),
    'concept_id' : concept_attribs['id'],
    'palette_id' : palette_attribs['id'],
    'state'      : Hooke.model.State.active,
}

player_attribs = {
    'id'         : 'myplayer',
    'password'   : 'mypassword',
    'first_name' : 'My',
    'last_name'  : 'Player',
    'email'      : 'myplayer@nowhere.com',
}

history_player_attribs = {
    'history_id' : history_attribs['id'],
    'player_id'  : player_attribs['id'],
}

period_attribs = {
    'id'          : 'myperiod',
    'history_id'  : history_attribs['id'],
    'position'    : Hooke.model.Position.medial,
    'description' : 'This is my period description.',
    'tone'        : Hooke.model.Tone.light,
}
