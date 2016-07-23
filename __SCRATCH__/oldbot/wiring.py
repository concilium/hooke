from enum import Enum

class Senders( Enum ):
    
    RELAY     = 'relay_sender'
    EXECUTIVE = 'executive_sender'
    SPOOLER   = 'spooler_sender'

class Signals( Enum ):

    POST_MESSAGE                    = 'post_message_signal'
    ECHO                            = 'echo_signal'

    MAKE_CONCEPT                    = 'make_concept_signal'
    LIST_CONCEPTS                   = 'list_concepts_signal'
    
    MAKE_PALETTE                    = 'make_palette_signal'
    LIST_PALETTES                   = 'list_palettes_signal'
    
    MAKE_INGREDIENT                 = 'make_ingredient_signal'
    LIST_INGREDIENTS                = 'list_ingredients_signal'
    
    INCLUDE_INGREDIENT_IN_PALETTE   = 'include_ingredient_in_palette_signal'
    EXCLUDE_INGREDIENT_IN_PALETTE   = 'exclude_ingredient_in_palette_signal'
    REMOVE_INGREDIENT_FROM_PALETTE  = 'remove_ingredient_from_palette_signal'
    
    CREATE_SEED                     = 'make_seed_signal'
    LIST_SEEDS                      = 'list_seeds_signal'
    SHOW_SEED                       = 'show_seed_signal'
    
    START_HISTORY                   = 'start_history_signal'
    LIST_HISTORIES                  = 'list_histories_signal'
    SHOW_HISTORY                    = 'show_history_signal'
    
    MAKE_PLAYER                     = 'make_player_signal'
    LIST_PLAYERS                    = 'list_players_signal'

    

