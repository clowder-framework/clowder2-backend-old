from typing import List

from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    APP_NAME: str = "Clowder"
    API_V2_STR: str = "/api/v2"
    admin_email: str = "devnull@ncsa.illinois.edu"
    frontend_url: str = "http://localhost:3000"

    # openssl rand -hex 32
    local_auth_secret = (
        "47358d6ace318031e822d722c15d191ba0d3e2cc7594317514e553424ccf3e39"
    )

    # openssl rand -hex 32
    local_auth_secret = (
        "47358d6ace318031e822d722c15d191ba0d3e2cc7594317514e553424ccf3e39"
    )

    # exposing default ports for fronted
    CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:3002",
    ]

    MONGODB_URL: str = "mongodb://localhost:27017"
    MONGO_DATABASE: str = "clowder2"

    MINIO_SERVER_URL: str = "localhost:9000"
    MINIO_BUCKET_NAME: str = "clowder"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"
    MINIO_UPLOAD_CHUNK_SIZE: int = 10 * 1024 * 1024

    # keycloak server
    auth_base = "http://localhost:8080"
    auth_realm = "clowder"
    auth_client_id = "clowder2-backend"
    auth_url = f"{auth_base}/auth/realms/{auth_realm}/protocol/openid-connect/auth?client_id={auth_client_id}&response_type=code"
    auth_token_url = (
        f"{auth_base}/auth/realms/{auth_realm}/protocol/openid-connect/token"
    )
    auth_server_url = f"{auth_base}/auth/"
    auth_client_secret = ""

    # keycloak local config
    keycloak_username = "admin"
    keycloak_password = "admin"
    # user here means where the token will be requested from
    keycloak_user_realm_name = "master"
    # this is the realm in which the user will be created
    keycloak_realm_name = auth_realm
    keycloak_client_id = auth_client_id
    keycloak_base = "http://localhost:8000"
    keycloak_redirect_uris = [keycloak_base + "/api/v2/keycloak/auth"]
    keycloak_web_origins = [keycloak_base]
    # identity providers registered in keycloak, for example cilogon, globus, twitter
    keycloak_ipds = ["cilogon", "globus"]


settings = Settings()
