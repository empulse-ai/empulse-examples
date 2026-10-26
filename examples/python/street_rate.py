"""EMpulse Street FX Index: latest street rate, 90-day history and the official-vs-street premium.

    pip install requests
    EMPULSE_API_KEY=emp_... python street_rate.py EGP

A free key (https://empulse.ai/#key) covers the free currencies and the active currency of your country with a
1-day delay; a Pro key covers every active currency, the current day and hourly rates (https://empulse.ai/pricing).
"""

import os
import sys

import requests

API = "https://api.empulse.ai"
HEADERS = {"X-API-Key": os.environ["EMPULSE_API_KEY"]}


def get(path: str, **params) -> dict:
    r = requests.get(f"{API}{path}", headers=HEADERS, params=params, timeout=30)
    if r.status_code != 200:
        err = r.json().get("error", {})
        sys.exit(f"{r.status_code} {err.get('code')}: {err.get('message')}")
    return r.json()


def main(cur: str) -> None:
    latest = [row for row in get("/v1/rates/latest")["data"] if row["cur"] == cur]
    if not latest:
        sys.exit(f"{cur} is not covered by your key; see GET /v1/currencies")
    row = latest[0]
    print(f"{cur} {row['day']}: mid {row['mid']} (buy {row['buy']}, sell {row['sell']}), "
          f"confidence {row['confidence']}, 7d {row['chg_7d_pct']}%, 30d {row['chg_30d_pct']}%")

    history = get(f"/v1/rates/{cur}")["data"]            # the last 90 days by default
    mids = [r["mid"] for r in history if r["mid"] is not None and r["flag"] != "outlier"]
    print(f"90 days: {len(history)} rows, min {min(mids):.4f}, max {max(mids):.4f}")

    try:
        premium = get("/v1/official-vs-street/latest")["data"]
    except SystemExit as exc:                              # Pro product: a free key gets 403 tier_not_in_plan
        print(f"official vs street: {exc}")
        return
    for p in premium:
        if p["cur"] == cur:
            print(f"official {p['official']} vs street {p['street_mid']}: premium {p['premium_pct']}% "
                  f"(7-day average {p['premium_7d_avg']}%)")


if __name__ == "__main__":
    main((sys.argv[1] if len(sys.argv) > 1 else "EGP").upper())
