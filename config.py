from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    proxmox_host: str
    proxmox_user: str
    proxmox_token_secret: str
    proxmox_port: int
    database_url: str
    redis_url: str
    secret_key: str

    class Config:
        env_file = ".env"
        

settings = Settings()
