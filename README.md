# Computational Analysis (Undergraduate Level)

A complete, self-contained course for undergraduate **Computational Analysis** using Python.
Designed to run seamlessly in **GitHub Codespaces**, locally, or via Binder.

## 🔰 Audience & Prereqs
- Undergraduates in engineering / data science / applied math.
- Comfortable with calculus, linear algebra, and basic Python (variables, loops, functions).

## 🎯 Learning Outcomes
By the end of this course, you will be able to:
- Use Python (NumPy, Pandas) for numerical computation and data analysis.
- Implement and analyze simple numerical methods (root-finding, linear algebra, ODE/PDE basics).
- Build and evaluate basic ML models (linear regression) for empirical modeling.
- Create clear visualizations with Matplotlib.
- Practice reproducible, documented, version-controlled computational workflows (Jupyter Book).

## 🗂 Repository Layout
```
.
├─ book/                      # Jupyter Book source
│  ├─ _config.yml
│  ├─ _toc.yml
│  └─ content/                # Markdown pages & notebook references
├─ notebooks/                 # Jupyter notebooks (hands-on labs)
│  ├─ 01_python_basics.ipynb
│  ├─ 02_numpy_linear_algebra.ipynb
│  ├─ 03_pandas_data_analysis.ipynb
│  ├─ 04_matplotlib_visualization.ipynb
│  ├─ 05_optimization_gradient_descent.ipynb
│  ├─ 06_cfd_1d_heat_equation.ipynb
│  └─ 07_ml_linear_regression_sklearn.ipynb
├─ data/
│  └─ air_quality_sample.csv
├─ courseutils/               # Small helper package used by notebooks
│  ├─ __init__.py
│  └─ plotting.py
├─ .devcontainer/
│  └─ devcontainer.json       # Codespaces config
├─ .github/workflows/
│  └─ deploy-book.yml         # Build & publish Jupyter Book to GitHub Pages
├─ .vscode/settings.json
├─ .binder/environment.yml    # Binder/Hub environment (optional)
├─ environment.yml            # Conda-style env (optional)
├─ requirements.txt           # pip deps
├─ syllabus.md                # Detailed syllabus & weekly plan
├─ LICENSE
└─ Makefile                   # Quality-of-life commands
```

## 🚀 Quickstart (Codespaces)
1. Click **Code → Create codespace on main**.
2. After the container builds, the post-create step installs dependencies.
3. Open any notebook in `notebooks/` and run.
4. To build the Jupyter Book site locally:
   ```bash
   make book
   ```

## 📦 Local Install
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

## 🌐 Build & Publish the Course Website
- Push to GitHub; the **deploy-book** workflow builds & deploys the book to **gh-pages**.
- Enable GitHub Pages in repo settings: Source = `Deploy from a branch` → Branch = `gh-pages`.

## 🧑‍🏫 Instructor Notes
- The course is modular; assign notebooks as labs or homework.
- Use `syllabus.md` for a week-by-week plan with outcomes and assessments.
- Keep datasets small in-repo; link to larger data if needed.

## 🔗 License
MIT — see `LICENSE`.
