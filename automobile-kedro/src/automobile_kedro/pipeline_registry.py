"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from automobile_kedro.pipelines import data_processing as dpp


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pre_processing_pipeline = dpp.create_pipeline()

    return {
        "dpp":pre_processing_pipeline,
        "__default__": pre_processing_pipeline 
    }
