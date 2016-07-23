# Slackification

At https://slack.com/

	Create a new team
	
		Email:		stendhal9@white-knight.org
		Team Name:	The Concilium
		
	Created a bot integration
	
		API Token:	xoxb-59631153974-CCMvWfuKsWkltl9gaY3zGLyb
		User name:	hooke
		Icon:		(microscope emoji)
		Full Name:	Hooke
		[...]
		
	Install client library
	
		pip install slackclient
		
And then

	Install dispatcher library
	
		pip install pydispatcher


# PostgreSQL setup

    export PATH=/Applications/Postgres.app/Contents/Versions/9.5/bin:$PATH
	pip install psycopg

create user hookeusr with password 'grundlekins';
create database hookedb with owner = hookeusr;

		
# Bot startup

import logging
logging.basicConfig( level = 'DEBUG' )

import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://hookeusr:grundlekins@localhost:5432/hookedb')

import hooke
hooke.model.HookeModelBase.metadata.create_all( engine )

c = hooke.bot.Chassis( 'xoxb-59631153974-CCMvWfuKsWkltl9gaY3zGLyb', 'hooke', 'microscope-testing', engine )
c.power_on()
