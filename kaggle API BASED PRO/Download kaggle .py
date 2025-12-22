from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

api.dataset_download_files(
    "vivek468/superstore-dataset-final",
    path="data",
    unzip=True
)

print("Dataset downloaded successfully")
