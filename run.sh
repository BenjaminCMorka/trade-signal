#!/bin/bash
set -e

# init db
psql -U postgres -f db/init.sql

# get deps
pip3 install -r requirements.txt

# load price data
python3 src/ingest.py

# create signals
python3 src/signal.py

# run backtest sim
python3 src/simulate.py
