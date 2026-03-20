import shap
import matplotlib.pyplot as plt

def plot_shap_summary(explainer, X, class_index=1, max_display=10, sample_size=1000):
    X_safe = X.sample(n=sample_size, random_state=42) if len(X) > sample_size else X
    
    shap_values = explainer.shap_values(X_safe)
    
    vals = shap_values[class_index] if isinstance(shap_values, list) else shap_values[:, :, class_index]
    
    plt.figure(figsize=(10, 6))
    shap.summary_plot(vals, X_safe, plot_type="dot", max_display=max_display)


def plot_shap_waterfall(explainer, X_sample, class_index=1):
    if len(X_sample) != 1:
        raise ValueError("Error: X_sample must contain exactly one row.")
        
    shap_exp = explainer(X_sample)
    
    plt.figure(figsize=(8, 5))
    
    try:
        shap.plots.waterfall(shap_exp[0, :, class_index])
    except Exception:
        # Fallback
        shap.plots.waterfall(shap_exp[0])
