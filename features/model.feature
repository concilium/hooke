Feature: hooke data model

  Scenario: verify player model
    Given the data model has the "Player" class
     then it has the string attribute "id"
     then it has the string attribute "password"
     then it has the string attribute "first_name"
     then it has the string attribute "last_name"
     then it has the string attribute "email"
