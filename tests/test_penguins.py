from intro_marimo import load_penguins


def test_load_penguins():
    """Test load penguins"""
    df = load_penguins()
    assert len(df) == 344  # Known number of rows in the dataset

    # Required columns in the dataset
    required_col_names = [
        "species",
        "island",
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
        "sex",
    ]
    assert all(col in df.columns for col in required_col_names)
