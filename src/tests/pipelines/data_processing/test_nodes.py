import pandas as pd
from kedro_tutorial.pipelines.data_processing.nodes import (
    _is_true,
    create_model_input_table,
    preprocess_companies,
    preprocess_shuttles,
)


def test_is_true():
    assert _is_true("t") == True
    assert _is_true("f") == False
    assert _is_true("a") == False


def test_preprocess_companies(basic_data):

    output = preprocess_companies(basic_data)

    print(output)
    assert output.equals(
        pd.DataFrame(
            {
                "id": [
                    35029,
                    30292,
                ],
                "company_rating": [1, 0.67],
                "iata_approved": [False, False],
            }
        )
    )
