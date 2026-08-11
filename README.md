# Symulation

This repository contains a Monte Carlo war simulation script designed to estimate who may win a war, based on force levels and support multipliers. The current scenario models a Ukraine vs. Russia outcome estimate by repeatedly sampling combat variability. The approach follows the Monte Carlo method, originally designed by Stanisław Ulam.

## Usage

1. Install dependencies:
   ```bash
   pip install numpy
   ```
2. Run the simulation:
   ```bash
   python montecarlo.py
   ```

The script prints results to the console and writes them to `wyniki_symulacji.txt`.

## What the simulation does

- Uses fixed baseline force arrays for both sides.
- Sweeps a support multiplier range for Ukraine.
- Runs 10,000 randomized trials per support level.
- Reports win percentages for both sides at each support level.
