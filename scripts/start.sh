#!/bin/bash

set -euo pipefail

alembic upgrade head

uvicorn app.core.api:create_app --host 0.0.0.0 --port 5001 --factory --reload
