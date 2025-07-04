from datetime import date
from pathlib import Path

from cyclopts import App

from currency_conversion import CACHE_DIR
from currency_conversion.sources import FawazAhmed0Source

app = App()


@app.default
def fetch_exchange_rate(
    base_currency: str,
    dest_currency: str,
    date: str = date.today().isoformat(),
    data_dir: Path = CACHE_DIR,
    cache: bool = True,
) -> float:
    """
    Converts currencies on a given date

    Parameters
    ----------
    base_currency :
        The symbol of the base currency.
    dest_currency :
        The symbol of the destination currency.
    date :
        The date of the conversion.
    data_dir :
        The directory where the data is cached.
    cache :
        Whether to use cached data if available.

    Returns
    -------
    The conversion rate.

    """
    source = FawazAhmed0Source(
        base_currency=base_currency,
        dest_currency=dest_currency,
        date=date,
        data_dir=data_dir,
    )

    return source.get_rate(cache=cache)


if __name__ == "__main__":
    app()
