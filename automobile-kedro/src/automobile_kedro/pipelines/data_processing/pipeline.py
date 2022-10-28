"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""

from automobile_kedro.pipelines.data_processing.nodes import preprocess_encoding
from kedro.pipeline import Pipeline, node, pipeline

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func= preprocess_encoding,
            inputs = 'automobile',
            outputs = 'encoded_automobile',
            name = 'enconding_automobile_node',
        ),
    ])
