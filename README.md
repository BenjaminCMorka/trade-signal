# Trade Signal Pipeline

Trade Signal Pipeline is a Python-based project that simulates a trading signal system on minute-level price data. It generates buy and sell signals based on price movements, stores data and signals in a PostgreSQL database, and performs a portfolio simulation to evaluate strategy profitability. The project includes Data generation, Signal logic, Database integration, Reporting scripts, and Testing.

---

## Project Overview

This project demonstrates an end-to-end pipeline for financial trading signal simulation. It reads historical price data, applies a trading strategy to generate buy/sell signals, persists signals in a PostgreSQL database, and simulates portfolio value over time. The pipeline is designed to be simple yet extensible for further research or development.

---

## Dataset

- **Data Type:** Minute-level simulated price data or real market data (CSV format)  
- **Generated Dataset:** Synthetic random-walk price data created via a Python script  
- **Schema:** `ts` (timestamp), `price` (float)  
- **Database Tables:**  
  - `price_data` stores historical price points  
  - `signals` stores generated buy/sell signals with timestamp and price

---

## Core Components

```bash
data/
├── generate_price_data.py  # Creates synthetic minute-level price data CSV file
├── btc_usd.py # Price data CSV file
src/
├── ingest.py     # Loads historical price data from CSV files into the PostgreSQL database
├── signal.py        # Contains trading signal generation logic
├── simulate.py        # Holds the trading simulation and reports
db/
├── init.sql                   # SQL initialization scripts for PostgreSQL tables
tests/   
├── test_pipeline.py         # Unit tests for the overall pipeline flow
├── test_signal.py        # Unit tests for signal generation logic
run.sh                        # Bash script to initialize DB, load data, and run simulation

```
## Tech Stack

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)

