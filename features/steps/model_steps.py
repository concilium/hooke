from behave import *
import hooke

@given( u'the data model has the "{class_name}" class' )
def step_impl( context, class_name ):
    raise NotImplementedError

@then( u'it has the {attribute_type} attribute "{attribute_name}"' )
def step_impl( context, attribute_type, attribute_name ):
    raise NotImplementedError
