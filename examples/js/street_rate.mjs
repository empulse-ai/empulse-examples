// EMpulse Street FX Index: latest street rate and 90-day history in Node.js (18+, no dependencies).
//
//     EMPULSE_API_KEY=emp_... node street_rate.mjs EGP
//
// A free key: https://empulse.ai/#key · docs: https://api.empulse.ai/docs

const API = "https://api.empulse.ai";
const headers = { "X-API-Key": process.env.EMPULSE_API_KEY };

async function get(path) {
  const r = await fetch(`${API}${path}`, { headers });
  const body = await r.json();
  if (!r.ok) throw new Error(`${r.status} ${body.error?.code}: ${body.error?.message}`);
  return body;
}

const cur = (process.argv[2] || "EGP").toUpperCase();
const latest = (await get("/v1/rates/latest")).data.find((row) => row.cur === cur);
if (!latest) {
  console.error(`${cur} is not covered by your key; see GET /v1/currencies`);
  process.exit(1);
}
console.log(`${cur} ${latest.day}: mid ${latest.mid} (buy ${latest.buy}, sell ${latest.sell}), ` +
  `confidence ${latest.confidence}, 7d ${latest.chg_7d_pct}%, 30d ${latest.chg_30d_pct}%`);

const history = (await get(`/v1/rates/${cur}`)).data;
const mids = history.filter((r) => r.mid !== null && r.flag !== "outlier").map((r) => r.mid);
console.log(`90 days: ${history.length} rows, min ${Math.min(...mids)}, max ${Math.max(...mids)}`);
