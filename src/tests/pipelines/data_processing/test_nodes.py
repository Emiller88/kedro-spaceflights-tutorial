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