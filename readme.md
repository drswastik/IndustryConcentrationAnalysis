# Industry Concentration Analysis (2015-2024)

## Project Overview
This project analyzes the market structure and competitive intensity of three major Indian sectors: Cement, Automobile, and Power[cite: 25]. By evaluating ten years of consolidated revenue data (2015–2024), this analysis uncovers shifting market dynamics, entry barriers, and the trajectory of corporate dominance in India's industrial landscape.

## Key Metrics Calculated
* **Four-Firm Concentration Ratio (CR4):** The percentage of the total market held by the top four firms, indicating baseline market control[cite: 27].
* **Herfindahl-Hirschman Index (HHI):** The sum of the squared market shares of competing firms, providing a nuanced view of market inequality and concentration[cite: 27].

## Core Findings
* **Cement Industry:** Transitioning into a moderately concentrated oligopoly[cite: 34]. The CR4 reached nearly 70% by 2024, with the HHI spiking to 1,755 due to aggressive market capture by the leading firm[cite: 33, 34].
* **Automobile Industry:** Maintains a highly competitive, unconcentrated structure[cite: 36]. Despite massive overall market growth, the CR4 remains balanced at around 41%, with a consistently low HHI (486 in 2024), indicating low entry barriers and intense competition[cite: 35, 36].
* **Power Industry:** Experiencing a rapid structural shift. After years of stability, the CR4 jumped past 60% and the HHI reached 1,622 in 2024, driven by the dominance of state-run entities and the aggressive recovery of key private players[cite: 37, 38]. 

## Repository Structure
* `market_data_2015_2024.csv` - Raw revenue and market share dataset compiled from corporate annual reports, Screener, and SIAM[cite: 26].
* `concentration_metrics.py` - Python script utilizing Pandas and Matplotlib to programmatically calculate CR4/HHI and generate trend visualizations.
* `Industry_Analysis.pdf` - The comprehensive analytical report detailing macroeconomic interpretations and policy recommendations.

## Tech Stack
* **Language:** Python
* **Libraries:** Pandas (Data Manipulation), Matplotlib/Seaborn (Data Visualization)
* **Concepts:** Microeconomic Theory, Market Structures
