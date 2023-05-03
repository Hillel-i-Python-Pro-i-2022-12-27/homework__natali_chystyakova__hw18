import string
from typing import NamedTuple

from pydantic import BaseSettings, Field


class RunConfig(NamedTuple):
    len_word: int
    amount_of_words: int
    continue_index: int
    alphabet: str


class Settings(BaseSettings):

    len_word: int = Field(2)
    amount_of_words: int = Field(100)
    continue_index: int = Field(0)
    alphabet: str = Field("".join([string.ascii_lowercase, string.digits]))

    class Config:
        env_file = ".env"


def from_env() -> RunConfig:
    settings = Settings()

    return RunConfig(
        len_word=settings.len_word,
        amount_of_words=settings.amount_of_words,
        continue_index=settings.continue_index,
        alphabet=settings.alphabet,
    )


def settings_main():

    run_config = from_env()

    print(run_config)
    return run_config
