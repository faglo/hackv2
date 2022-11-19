#!/bin/bash

python3 -m alembic upgrade head
exec "$@"