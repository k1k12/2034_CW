# vinho-verde-quality-prediction

A data science project analysing and predicting the quality of Vinho Verde wines using provided properties. Includes EDA, feature engineering, and machine learning models for classification and regression.


CSC2034/
├── docs/ # Generated PDF of notebook
├── figures/ # For generated figures referenced in my report
├── notebook/ # Jupyter notebook
│ └── wine_analysis.ipynb 
├── datasets/ # Contains wine datasets
│ └── README.md
├── src/ # Rough drafts of code
├── README.md # Project description & details to run
├── requirements.txt # Python dependencies

---

### Requirements

- **LaTeX** (e.g. MacTeX)
- `latexmk`
- `make`

### Folder structure

vinho-verde-quality-prediction/
├── bin/            # Auxillary LaTeX files
├── data/           # Input datasets (.csv)
├── docs/           # Final PDF outputs
├── figures/        # Plots used in LaTeX docs
├── latex/          # LaTeX source files (report, task1A, etc.)
├── src/            # Python code and notebooks
├── Makefile
└── README.md

## Setup Instructions

1. Download datasets (if you have not already) and place in the datasets/ folder.
- winequality-red.csv
- winequality-white.csv
- winequality.names

2. Setup venv

- For linux:
```bash
python3 -m venv venv
source venv/bin/activate  
```
- For windows:
```bash
python3 -m venv venv
'venv\Scripts\activate'
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the notebook

```bash 
make notebook
```
OR, if you prefer to test with your own command:
```bash
jupyter notebook notebooks/wine_analysis.ipynb
```

5. (optional) Use make commands
To view progress, run different files and get the feel of my project, everything has been abstracted into make commands.
Below is the full lists of commands you can run.

**Task 1A**

```bash 
make task1A
```

## Generating the PDF Reports

Separate from the project submission, converts all latex files (e.g. for task notes, report drafts and can be found in /latex) and the notebook to PDF and stores in docs. 

* Docs are written in LaTeX or .ipynb and built using:
```bash 
make pdf
```
* To empty bin/ after generation, run:
```bash 
make empty
```
* In the case that you, as examiner, do not have LaTex installed, PDFs of latex files bar my final report
 have been pre-generated so you can view in docs/.
-> Note to self, when finalised, edit make command to generated everything and remove version.tex

## Task 1A

The first task involved visualising and comparing the quality distributions of red and white wine samples.

### What was done

- Reviewed winequality-red.csv and winequality-white.csv
- Plotted quality score distributions for:
    * Red wines
    * White wines
    * Both combined for comparison
- Saved plots as .pngs to figures/
- Plots and analysis are documented and reviewed in task1A.pdf (found in docs/)

### Key Observations

- Red wines are highly focused/clustered around quality scores of 5 and 6
- White wines show broader distribution (higher range), with more samples in the 7–8 range
- Overall, white wines exhibit a slightly higher average quality


