
import os
def GetDATABASES(DATABASE_TYPE, DATABASE_NAME, DATABASE_USER='', DATABASE_PWD='', DATABASE_HOST='', DATABASE_PORT=''):
    if DATABASE_TYPE == 'sqlite3':
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.sqlite3',
				'NAME': os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),DATABASE_NAME), 
			}
		}
		print "use sqlite3 %s" % os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), DATABASE_NAME) 
    elif DATABASE_TYPE == 'mysql':
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.mysql', 
				'NAME': DATABASE_NAME,
				'USER': DATABASE_USER,
				'PASSWORD': DATABASE_PWD,
				'HOST': DATABASE_HOST,
				'PORT': DATABASE_PORT,
			}
		}
		print "use mysql "
    else: #psycopg2
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2',
				'NAME': DATABASE_NAME,
				'USER': DATABASE_USER,
				'PASSWORD': DATABASE_PWD,
				'HOST': DATABASE_HOST,
				'PORT': DATABASE_PORT,
			}
		}
		print "use postgresql_psycopg2"
    print DATABASES
    return DATABASES

'''
DATABASE_TYPE = 'sqlite3'

print "len(DATABASES['default']) is : %s" % len(DATABASES['default'])

if len(DATABASES['default']) == 0: # local
    if DATABASE_TYPE == 'sqlite3':
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
				'NAME': os.path.join(os.path.dirname(os.path.dirname(__file__)),'lwc.db'),                      # Or path to database file if using sqlite3.
				#'NAME': '/app/lwc/lwc.db',
			}
		}

		print "use mysql local %s" % os.path.join(os.path.dirname(os.path.dirname(__file__)),'lwc.db') 
    elif DATABASE_TYPE == 'mysql':
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
				'NAME': 'lwc',                      # Or path to database file if using sqlite3.
				# The following settings are not used with sqlite3:
				'USER': 'root',
				'PASSWORD': ' 123',
				'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
				'PORT': '',                      # Set to empty string for default.
			}
		}
		print "use mysql local "
    else: #psycopg2
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
				'NAME': 'lwc',                      # Or path to database file if using sqlite3.
				# The following settings are not used with sqlite3:
				'USER': 'postgres',
				'PASSWORD': '123',
				'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
				'PORT': '',                      # Set to empty string for default.
			}
		}
		print "use postgresql_psycopg2 local "
else:
    if DATABASE_TYPE == 'sqlite3':
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
				'NAME': os.path.join(os.path.dirname(os.path.dirname(__file__)),'lwc.db'),                      # Or path to database file if using sqlite3.
				#'NAME': '/app/lwc/lwc.db',
			}
		}

		print "use mysql server %s" % os.path.join(os.path.dirname(os.path.dirname(__file__)),'lwc.db')	
    else: #psycopg2
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
				'NAME': 'dbv6n78stkmeqg',                      # Or path to database file if using sqlite3.
				# The following settings are not used with sqlite3:
				'USER': 'ntccscinrvwneo',
				'PASSWORD': ' TJG0ByhrZ5f412ZR6u4AnWUQoy',
				'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
				'PORT': '5432',                      # Set to empty string for default.
			}
		}
		print "use postgresql_psycopg2 server"
	
print "DATABASES:" + str(DATABASES)
'''