# Agarpyo

## Description

Agarpyo est un jeu solo inspiré d'Agar.io, où le joueur doit atteindre le score le plus élevé en consommant des cellules.

## Requirements

miniconda 23.11.0

## Installation

```sh
git clone https://github.com/B2-Info-23-24/agarpyo-b2-b-AlbaNagisa
cd agarpyo-b2-b-AlbaNagisa
```

## Import conda environment

```sh
touch environment.yml
cat << EOF > environment.yml
name: agarpyo
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.12.1
  - pygame=2.5.2
EOF

conda env create -f environment.yml
conda activate agarpyo
```

## How to run

```sh
python main.py
```
