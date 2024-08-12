#tox24 challenge data brick

**source**: https://ochem.eu/static/challenge-data.do

## Overview

The Tox24 BioBrick stores the training and test datasets for the Tox24 Challenge. This challenge aims to advance computational methods for predicting the in vitro activity of chemical compounds, particularly their interaction with Transthyretin (TTR). Participants use these datasets to develop models that predict how compounds interfere with biochemical pathways based solely on chemical structure data.

## Datasets

- **Training Set**: Contains 1,012 compounds tested for activity against TTR.
- **Leaderboard Set**: Includes 200 compounds.
- **Blind Test Set**: Comprises 300 compounds.

## Data Sources

The structural information (SMILES) was initially retrieved from the U.S. EPA’s CompTox Chemicals Dashboard for the ToxCast libraries. Missing structural data were supplemented using PubChem based on CAS RN and compound names.

## Usage

Participants can use this BioBrick to train and validate their models. The goal is to minimize the Root Mean Square Error (RMSE) between predicted and actual single point concentrations of the blind test set compounds.

## How to Contribute

1. **Register**: Each team must have a registered account on the OCHEM website.
2. **Submission**: Submit predictions for the test sets via the OCHEM website or by email.

## Validation

The winning model must be reproducible and may require open-source release or free licenses for model testing.

## Prize

The winning team will be awarded 1,000€ and invited to present their model at ICANN2024.