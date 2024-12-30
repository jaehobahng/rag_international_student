import openai
import yaml
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from typing import List, Tuple
from utils.load_config import LoadConfig

# For loading openai credentials
APPCFG = LoadConfig()

with open("configs/app_config.yml") as cfg:
    app_config = yaml.load(cfg, Loader=yaml.FullLoader)