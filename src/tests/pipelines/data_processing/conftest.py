import pandas as pd
import pytest


@pytest.fixture(scope="module")
def basic_data():
    return pd.DataFrame(
        {
            "id": [
                35029,
                30292,
            ],
            "company_rating": ["100%", "67%"],
            "iata_approved": ["f", "f"],
        }
    )
