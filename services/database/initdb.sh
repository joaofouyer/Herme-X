#!/bin/sh

set -e

export PGUSER="hermex"
"${psql[@]}" <<- 'EOSQL'
CREATE USER postgres SUPERUSER;
CREATE DATABASE postgres WITH OWNER postgres;
CREATE USER hermex WITH PASSWORD 'fe9941445a1e8a693e0335e8200417ec';
ALTER USER hermex WITH SUPERUSER;
CREATE DATABASE admin OWNER = hermex ;
CREATE DATABASE location OWNER =  hermex ;
GRANT ALL PRIVILEGES ON DATABASE admin TO hermex;
GRANT ALL PRIVILEGES ON DATABASE location TO hermex;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA PUBLIC TO hermex;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA PUBLIC TO hermex;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA PUBLIC TO hermex;

UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'admin';
UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'location';
EOSQL

# Load PostGIS into both template_database and $POSTGRES_DB
for DB in admin location; do
	echo "Loading PostGIS extensions into $DB"
	"${psql[@]}" --dbname="$DB" <<-'EOSQL'
		CREATE EXTENSION IF NOT EXISTS postgis;
		CREATE EXTENSION IF NOT EXISTS postgis_topology;
		CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;
		CREATE EXTENSION IF NOT EXISTS postgis_tiger_geocoder;
EOSQL
done
