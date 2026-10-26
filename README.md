# empulse-examples

Examples for the **EMpulse Street FX Index** API: daily street exchange rates of 20 emerging-market currencies against the US dollar (USDT), with a confidence class and the number of independent market sources on every figure. History since 2022-01-02, updated daily (UTC).

* Website: https://empulse.ai/?utm_source=github&utm_medium=marketplace&utm_campaign=listing
* API docs: https://api.empulse.ai/docs
* Methodology: https://empulse.ai/methodology?utm_source=github&utm_medium=marketplace&utm_campaign=listing
* Free key (one minute): https://empulse.ai/?utm_source=github&utm_medium=marketplace&utm_campaign=listing#key
* MCP server for AI agents: https://api.empulse.ai/mcp (repository: https://github.com/empulse-ai/empulse-mcp)
* Public dataset (30-day delay, CC BY-NC 4.0): Kaggle and Hugging Face, `empulse-street-fx-index`

## Quick start

```bash
curl -H "X-API-Key: $EMPULSE_API_KEY" https://api.empulse.ai/v1/rates/latest
```

| example | what it shows |
|---|---|
| `examples/python/street_rate.py` | latest rate, 90-day history and the official-vs-street premium |
| `examples/js/street_rate.mjs` | the same in Node.js (fetch, no dependencies) |
| `examples/sheets.md` | Google Sheets: `IMPORTDATA` on the CSV endpoint with a free key |
| `notebooks/official_vs_street_90d.ipynb` | notebook: official vs street over 90 days, one chart |

Set `EMPULSE_API_KEY` in the environment. A free key covers the free currencies and the active currency of your country with a 1-day delay; Pro covers all 20 active currencies, the current day and hourly rates (https://empulse.ai/pricing?utm_source=github&utm_medium=marketplace&utm_campaign=listing).

## Fields

| field | meaning |
|---|---|
| `cur` | ISO 4217 code of the currency |
| `day` | UTC calendar day (YYYY-MM-DD) |
| `buy` | weighted average rate at which a client buys US dollars (USDT) for local currency; empty when the side has too few data points |
| `sell` | the same for the side where the client sells US dollars |
| `mid` | (buy + sell) / 2; when only one side of the market exists, that side's rate (see `side`) |
| `side` | what `mid` is based on: both, buy or sell |
| `spread_pct` | (buy − sell) / mid × 100, only when side = both |
| `confidence` | high, medium or limited: the confidence class of the day |
| `flag` | `outlier` for a day whose rate deviates sharply from its neighbours with few data points; else empty |
| `in_progress` | true while the latest day is still being collected and will be revised |
| `mid_7d` | mean of the valid `mid` values over the last 7 calendar days |
| `chg_1d_pct` | change of `mid` against 1 calendar day earlier, % |
| `chg_7d_pct` | change of `mid` against 7 calendar days earlier, % |
| `chg_30d_pct` | change of `mid` against 30 calendar days earlier, % |

## Citing

Name the source as "EMpulse Street FX Index" and link the currency page (`https://empulse.ai/rates/<CUR>`). Terms: https://empulse.ai/terms. The data is not investment advice.
