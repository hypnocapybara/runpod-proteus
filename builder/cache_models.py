import os
from huggingface_hub import snapshot_download


def fetch_pretrained_model(model_name, hf_token=None):
    """
    Fetches a pretrained model from the HuggingFace model hub.
    """
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return snapshot_download(repo_id=model_name, repo_type="model", token=hf_token)
        except OSError as err:
            if attempt < max_retries - 1:
                print(
                    f"Error encountered: {err}. Retrying attempt {attempt + 1} of {max_retries}...")
            else:
                raise


def warm_up_pipeline():
    """
    Fetches the pipelines from the HuggingFace model hub.
    """

    hf_token = os.environ.get("HF_TOKEN", None)
    fetch_pretrained_model("madebyollin/sdxl-vae-fp16-fix", hf_token)
    fetch_pretrained_model("dataautogpt3/ProteusV0.4", hf_token)


if __name__ == "__main__":
    warm_up_pipeline()
