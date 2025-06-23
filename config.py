from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    # 加载环境变量
    load_dotenv(find_dotenv(), override=True)
    
settings = Config()