from pydantic_settings import SettingsConfigDict, BaseSettings

APP_NAME = '{{ cookiecutter.__package_name }}'


class ApplicationSettings(BaseSettings):
    # TODO: add class and class member doc strings
    model_config = SettingsConfigDict(
        env_prefix=f'{APP_NAME}_',
    )
