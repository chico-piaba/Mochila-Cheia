#!/bin/sh
# Na primeira subida do contêiner o banco ainda não existe: cria a partir de
# schema.sql + seed.sql. Nas seguintes (volume montado), preserva os dados.
set -e
if [ ! -f "$MOCHILA_DB" ]; then
    flask --app run init-db
fi
exec "$@"
