import json
from typing import Any, ClassVar

import requests
from pydantic import field_validator

from .base import BaseExchangeRateSource


class FawazAhmed0Source(BaseExchangeRateSource):
    ENDPOINT: ClassVar[str] = (
        "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/v1/currencies/{base_currency}.json"
    )

    @field_validator("base_currency", "dest_currency")
    def validate_currency(cls, currency: str) -> str:
        return currency.lower()

    def get_rate(self, cache: bool = True) -> float:
        rates = self._get_rates(cache=cache)

        return rates[self.dest_currency]

    def _get_rates(self, cache: bool = True) -> dict[str, float]:
        if cache:
            cache_dir = self.data_dir / self.date_str

            if (cache_dir / f"{self.base_currency}.json").exists():
                with open(cache_dir / f"{self.base_currency}.json", "r") as f:
                    return json.load(f)

        json_data = self._get_json()
        rates = json_data[self.base_currency]

        if cache:
            cache_dir = self.data_dir / json_data["date"]
            cache_dir.mkdir(parents=True, exist_ok=True)

            with open(
                self.data_dir / self.date_str / f"{self.base_currency}.json", "w"
            ) as f:
                json.dump(rates, f)

        return rates

    def _get_json(self) -> dict[str, Any]:
        data = requests.get(
            self.ENDPOINT.format(base_currency=self.base_currency, date=self.date_str)
        )

        if data.status_code == 404:
            data = requests.get(
                self.ENDPOINT.format(base_currency=self.base_currency, date="latest")
            )

        return data.json()
