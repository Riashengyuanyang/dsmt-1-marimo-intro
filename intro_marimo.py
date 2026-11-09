import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import classification_report
    from datasets import load_dataset


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    **Notice our setup cell above. Having your imports in a setup cell makes the rest of the notebook easier to test**

    # Palmer Penguins

    The Palmer Archipelago penguin dataset is a popular alternative to the classic Iris dataset for practicing data analysis and machine learning techniques. It contains measurements for three species of penguins (Adelie, Chinstrap, and Gentoo) collected from three islands in the Palmer Archipelago, Antarctica.

    In this simplified demo, we:
    - Load the dataset
    - Drop null values
    - Encode categoricals
    - Fit a random forest
    - Check a prediction
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Loading

    Here we load...
    """)
    return


@app.function
def load_penguins() -> pd.DataFrame:
    """Load some penguins"""
    penguins = load_dataset("SIH/palmer-penguins")["train"].with_format("pandas")[:]
    return penguins


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    And inspect our data.
    """)
    return


@app.cell
def _():
    load_penguins()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Cleaning, Feature Engineering
    Then we clean and engineer some features.
    """)
    return


@app.function
def get_penguin_features_target() -> tuple[pd.DataFrame, pd.Series]:
    """Clean and return X and y"""
    # Data cleaning - drop NA, lowercase strings
    penguins_clean = load_penguins().dropna()
    penguins_clean = penguins_clean.apply(lambda col: col.str.lower() if pd.api.types.is_string_dtype(col) else col)

    # Dummy encode categoricals
    df = pd.get_dummies(penguins_clean)

    # Preview
    df.head()

    # sex_male becomes the target
    X = df.drop(
        "sex_male", axis=1
    )
    y = df["sex_male"]
    return X, y


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Split and Fit

    Then we split, fit and report back.
    """)
    return


@app.cell
def _():
    n_estimators = 3
    max_depth = 2
    return max_depth, n_estimators


@app.cell
def _(max_depth, n_estimators):
    X, y = get_penguin_features_target()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    rf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    rf.fit(X_train, y_train)

    preds = rf.predict(X_test)
    cr = classification_report(y_test, preds)
    return X, rf, y


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Predict

    Before finally running a prediction against the original dataset.
    """)
    return


@app.cell
def _(X, rf, y):
    example = X.iloc[[0]]
    true_value = y.iloc[0]
    pred_value = rf.predict(example)[0]

    print("True is_male (0=female,1=male):", true_value)
    print("Predicted is_male:", pred_value)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # The End
    """)
    return


if __name__ == "__main__":
    app.run()
