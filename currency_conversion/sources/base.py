from abc import ABC, abstractmethod
from datetime import date
from pathlib import Path

from pydantic import BaseModel

from currency_conversion import DATA_DIR


class BaseExchangeRateSource(ABC, BaseModel):
    base_currency: str
    dest_currency: str
    date: date
    data_dir: Path = DATA_DIR

    @abstractmethod
    def get_rate(self, cache: bool = True) -> float:
        pass

    @property
    def date_str(self) -> str:
        return self.date.isoformat()
