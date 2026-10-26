# Google Sheets

The CSV endpoint accepts the key as a query parameter for formulas that cannot send headers. Keep such a sheet
private: the key is personal.

```
=IMPORTDATA("https://api.empulse.ai/v1/rates/EGP/csv?key=emp_YOUR_KEY")
```

Columns: `day, buy, sell, mid, side, spread_pct, confidence, flag, in_progress, mid_7d, chg_1d_pct, chg_7d_pct,
chg_30d_pct` (the last 90 days by default; add `&from=2026-01-01&to=2026-03-31` for a range, `&fields=mid,confidence`
for a subset).

The latest day of every currency your key covers:

```
=IMPORTDATA("https://api.empulse.ai/v1/rates/latest?key=emp_YOUR_KEY&format=csv")
```

Google refreshes `IMPORTDATA` about once an hour; the index is updated daily (UTC), free keys with a 1-day delay.
Excel: *Data → From Web* with the same URL. A free key: https://empulse.ai/#key
