# CSC2034 Data Science

A data science project for my stage 2 university course at Newcastle University. The project involves exploratory data analysis and supervised learning (binary classification and regression) on both red and white wine datasets.

---

## File Structure

```text
CSC2034_DataScience/
├── datasets/         # Red and white wine datasets
├── docs/             # PDFs (notebook, report)
├── figures/          # All figures generated in my notebook (for excluded report dir)
├── notebook/         # Jupyter notebook
│   └── wine_analysis.ipynb
├── src/              # Rough draft files for different tasks
├── pyproject.toml    # Dependencies
└── README.md
```

## Setup

### 1. venv

Create and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Dependencies

```bash
pip install .
```

***or***

```bash
pip install -r requirements.txt
```

## Running the project

```bash
jupyter notebook notebook/wine_analysis.ipynb
```


