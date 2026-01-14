# Currency Conversion

Finds the currency exchange rates between two currencies on a given date.


```bash
uv sync
```

Install globally by running:

```bash
uv tool install .
```

Then, run with:

```bash
$ fetch-exchange-rate eur usd
1.1700657
```

Usage:

```text
Usage: fetch-exchange-rate [ARGS] [OPTIONS]

Converts currencies on a given date

╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────╮
│ --help -h  Display this message and exit.                                                        │
│ --version  Display application version.                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Parameters ─────────────────────────────────────────────────────────────────────────────────────╮
│ *  BASE-CURRENCY --base-currency  The symbol of the base currency. [required]                    │
│ *  DEST-CURRENCY --dest-currency  The symbol of the destination currency. [required]             │
│    DATE --date                    The date of the conversion. [default: 2025-06-27]              │
│    DATA-DIR --data-dir            The directory where the data is cached. [default:              │
│                                   ~/.local/share/currency-conversion]                   │
│    CACHE --cache --no-cache       Whether to use cached data if available. [default: True]       │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
```
