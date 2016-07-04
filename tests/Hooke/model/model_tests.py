import datetime
import nose

import Hooke

def test_model():
    '''verify existence of "model" package in Hooke module'''
    _check_attr( Hooke, 'model' )

def test_ingredient_model():
    '''verify existence and attributes of "Ingredient" model class'''

    _check_attr( Hooke.model, 'Ingredient' )
    
    i_attribs = {
        'id'          : 'myingredient',
        'description' : 'This is my ingredient description.',
    }
    
    i = Hooke.model.Ingredient( **i_attribs )
    _compare_attrs( i, i_attribs )
    _check_repr( i, i.id )

def test_palette_model():
    '''verify existence and attributes of "Palette" model class'''

    _check_attr( Hooke.model, 'Palette' )
    
    p_attribs = {
        'id'          : 'mypalette',
        'description' : 'This is my palette description.',
    }
    
    p = Hooke.model.Palette( **p_attribs )
    _compare_attrs( p, p_attribs )
    _check_repr( p, p.id )

def test_palette_ingredient_model():
    '''verify existence and attributes of "PaletteIngredient" model class'''

    _check_attr( Hooke.model, 'PaletteIngredient' )
    
    p_attribs = {
        'id'          : 'mypalette',
        'description' : 'This is my palette description.',
    }
    p = Hooke.model.Palette( **p_attribs )
    i_attribs = {
        'id'          : 'myingredient',
        'description' : 'This is my ingredient description.',
    }
    i = Hooke.model.Ingredient( **i_attribs )
    
    pi_attribs = {
        'palette_id'    : p.id,
        'ingredient_id' : i.id,
        'flavor'        : Hooke.model.Flavor.include,
    }
    
    pi = Hooke.model.PaletteIngredient( **pi_attribs )
    _compare_attrs( pi, pi_attribs )
    _check_assoc_repr( pi, pi.palette_id, pi.ingredient_id )

def test_palette_ingredient_association():
    '''verify behavior of palette-to-ingredient association'''
    
    # setup 
    
    from sqlalchemy import create_engine
    engine = create_engine( 'sqlite:///:memory:' )
    Hooke.model.HookeModelBase.metadata.create_all( engine )

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker( bind = engine )
    ses = Session()
        
    p_attribs = {
        'id'          : 'mypalette',
        'description' : 'This is my palette description.',
    }
    p = Hooke.model.Palette( **p_attribs )
    ses.add( p )
    
    i_attribs = {
        'id'          : 'myingredient',
        'description' : 'This is my ingredient description.',
    }
    i = Hooke.model.Ingredient( **i_attribs )
    ses.add( i )
    
    pi_attribs = {
        'palette_id'    : p.id,
        'ingredient_id' : i.id,
        'flavor'        : Hooke.model.Flavor.include,
    }
    pi = Hooke.model.PaletteIngredient( **pi_attribs )
    ses.add( pi )
    
    ses.commit()
    
    # tests
    
    assert len( p.palette_ingredients ) == 1
    assert p.palette_ingredients[0] == pi
    assert len( p.ingredients ) == 1
    assert p.ingredients[0] == i

    assert len( i.palette_ingredients ) == 1
    assert i.palette_ingredients[0] == pi
    assert len( i.palettes ) == 1
    assert i.palettes[0] == p
    
def test_concept_model():
    '''verify existence and attributes of "Concept" model class'''

    _check_attr( Hooke.model, 'Concept' )
    
    c_attribs = {
        'id'          : 'myconcept',
        'description' : 'This is my concept description.',
    }
    
    c = Hooke.model.Concept( **c_attribs )
    _compare_attrs( c, c_attribs )
    _check_repr( c, c.id )

def test_concept_palette_model():
    '''verify existence and attributes of "ConceptPalette" model class'''

    _check_attr( Hooke.model, 'ConceptPalette' )
    
    c_attribs = {
        'id'          : 'myconcept',
        'description' : 'This is my concept description.',
    }    
    c = Hooke.model.Concept( **c_attribs )
    p_attribs = {
        'id'          : 'mypalette',
        'description' : 'This is my palette description.',
    }
    p = Hooke.model.Palette( **p_attribs )
    
    cp_attribs = {
        'concept_id' : c.id,
        'palette_id' : p.id,
        'notes'      : 'These are my concept/palette notes.',
    }
    
    cp = Hooke.model.ConceptPalette( **cp_attribs )
    _compare_attrs( cp, cp_attribs )
    _check_assoc_repr( cp, cp.concept_id, cp.palette_id )

def test_concept_palette_association():
    '''verify behavior of concept-to-palette association'''
    
    # setup 
    
    from sqlalchemy import create_engine
    engine = create_engine( 'sqlite:///:memory:' )
    Hooke.model.HookeModelBase.metadata.create_all( engine )

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker( bind = engine )
    ses = Session()
        
    c_attribs = {
        'id'          : 'myconcept',
        'description' : 'This is my concept description.',
    }    
    c = Hooke.model.Concept( **c_attribs )
    ses.add( c )
    
    p_attribs = {
        'id'          : 'mypalette',
        'description' : 'This is my palette description.',
    }
    p = Hooke.model.Palette( **p_attribs )
    ses.add( p )
    
    cp_attribs = {
        'concept_id' : c.id,
        'palette_id' : p.id,
        'notes'      : 'These are my concept/palette notes.',
    }    
    cp = Hooke.model.ConceptPalette( **cp_attribs )
    ses.add( cp )
    
    ses.commit()
    
    # tests
    
    assert len( c.concept_palettes ) == 1
    assert c.concept_palettes[0] == cp
    assert len( c.palettes ) == 1
    assert c.palettes[0] == p

    assert len( p.concept_palettes ) == 1
    assert p.concept_palettes[0] == cp
    assert len( p.concepts ) == 1
    assert p.concepts[0] == c
    
def test_player_model():
    '''verify existence and attributes of "Player" model class'''

    _check_attr( Hooke.model, 'Player' )
    
    p_attribs = {
        'id'         : 'myplayer',
        'password'   : 'mypassword',
        'first_name' : 'My',
        'last_name'  : 'Player',
        'email'      : 'myplayer@nowhere.com',
    }
    
    p = Hooke.model.Player( **p_attribs )
    _compare_attrs( p, p_attribs )
    _check_repr( p, p.id )

def test_history_model():
    '''verify existence and attributes of "History" model class'''
    
    _check_attr( Hooke.model, 'History' )
    
    h_attribs = {
        'id'         : 'myhistory',
        'started_on' : datetime.datetime.now(),
        'concept_id' : 'myconcept',
        'palette_id' : 'mypalette',
        'state'        : Hooke.model.State.active,
    }
    
    h = Hooke.model.History( **h_attribs )
    _compare_attrs( h, h_attribs )
    _check_repr( h, h.id )

#def test_player_model():
#    '''verify existence and attributes of "Player" model class'''
#    
#    _check_attr( Hooke.model, 'Player' )
#
#    p_attribs = {
#        'id'         : 'joetester',
#        'password'   : 'testpassword',
#        'first_name' : 'Joe',
#        'last_name'  : 'Tester',
#        'email'      : 'joetester@nowhere.com',
#    }
#    
#    p = Hooke.model.Player( **p_attribs )
#    _compare_attrs( p, p_attribs )
#    _check_repr( p )
    
#def test_seed_model():
#    '''verify existence and attributes of "Seed" model class'''
#
#    _check_attr( Hooke.model, 'Seed' )
#    
#    s_attribs = {
#        'id'      : 'myseed',
#        'concept' : 'This is my seed concept.',
#    }
#    
#    s = Hooke.model.Seed( **s_attribs )
#    _compare_attrs( s, s_attribs )
#    _check_repr( s )

#def test_history_model():
#    '''verify existence and attributes of "History" model class'''
#
#    _check_attr( Hooke.model, 'History' )
#    
#    h_attribs = {
#        'id' : 'foo',
#        'started_on' : datetime.date.today(),
#        'seed_id' : 'myseed',
#    }
#
#    h = Hooke.model.History( **h_attribs )
#    _compare_attrs( h, h_attribs )
#    _check_repr( h )

#def test_period_model():
#    assert hasattr( hooke.model, 'Period' ), 'hooke.model module has no "Period" attribute'
#    
#    p = hooke.model.Period()
#    assert hasattr( p, 'id' ), 'hooke.model.Period class has no "id" attribute'
#    assert hasattr( p, 'tone' ), 'hooke.model.Period class has no "tone" attribute'
#    assert hasattr( p, 'description' ), 'hooke.model.Period class has no "description" attribute'
#
#def test_event_model():
#    assert hasattr( hooke.model, 'Event' ), 'hooke.model module has no "Event" attribute'
#    
#    p = hooke.model.Event()
#    assert hasattr( p, 'id' ), 'hooke.model.Event class has no "id" attribute'
#    assert hasattr( p, 'tone' ), 'hooke.model.Event class has no "tone" attribute'
#    assert hasattr( p, 'description' ), 'hooke.model.Event class has no "description" attribute'
#
#def test_scene_model():
#    assert hasattr( hooke.model, 'Scene' ), 'hooke.model module has no "Scene" attribute'
#    
#    s = hooke.model.Scene()
#    assert hasattr( s, 'id' ), 'hooke.model.Scene class has no "id" attribute'
#    assert hasattr( s, 'tone' ), 'hooke.model.Scene class has no "tone" attribute'
#    assert hasattr( s, 'question' ), 'hooke.model.Scene class has no "question" attribute'
#    assert hasattr( s, 'narrative' ), 'hooke.model.Scene class has no "narrative" attribute'
#    assert hasattr( s, 'answer' ), 'hooke.model.Scene class has no "answer" attribute'
#

def _check_attr( thing, attribute ):
    assert hasattr( thing, attribute ), '%s has no "%s" attribute' % ( thing, attribute )

def _compare_attrs( thing, attributes ):
    for a in attributes.keys():
        expected = attributes[a]
        found = getattr( thing, a )
        assert ( expected == found ), 'expected attribute "%s" of %s to be "%s", found "%s"' % ( a, thing, expected, found )

def _check_repr( thing, pkey ):
    expected = '<%s[%s]>' % ( type( thing ).__name__, pkey )
    found = thing.__repr__()
    assert ( expected == found ), 'expected representation "%s", found "%s"' % ( expected, found )

def _check_assoc_repr( thing, left_pkey, right_pkey ):
    expected = '<%s[%s,%s]>' % ( type( thing ).__name__, left_pkey, right_pkey )
    found = thing.__repr__()
    assert ( expected == found ), 'expected representation "%s", found "%s"' % ( expected, found )
