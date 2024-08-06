def evaluate_pytorch_model(model_path, data):
    pass


def evaluate_onnx_model(model_path, data):
    pass


def evaluate_quant_onnx_model(model_path, data):
    pass


if __name__ == "__main__":

    import pandas as pd

    data = pd.read_csv("data/ai-vs-human-text.csv")
    sampled_data = "data/ai-vs-human"
    evaluate_pytorch_model("models/pytorch_model.pt", data)
