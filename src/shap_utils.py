import shap
import numpy as np
import pandas as pd

def explain_model(model, X_sample):
    """
    Compute SHAP summary plot for global explainability.
    """
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_sample)

    if isinstance(shap_values, list):
        shap.summary_plot(shap_values[1], X_sample)
    else:
        shap.summary_plot(shap_values, X_sample)


def explain_single_observation(model, X_single):
    """
    Explain SHAP for a single observation.
    """
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_single)

    if isinstance(shap_values, list):
        shap_value_single = shap_values[1][0]
        expected_value = explainer.expected_value[1]
    else:
        shap_value_single = shap_values[0]
        expected_value = explainer.expected_value

    shap.force_plot(
        expected_value,
        shap_value_single,
        X_single,
        matplotlib=True
    )
