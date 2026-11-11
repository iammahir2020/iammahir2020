"""Render the profile's contribution panel (dark + light SVG) from the GitHub GraphQL API.

Usage: GITHUB_TOKEN=... python activity.py <login> <out_dir>
Fonts are reused from assets/header-dark.svg so the panel matches the rest of the README.
"""
import datetime as dt
import json
import os
import re
import sys
import urllib.request

LOGIN, OUT = sys.argv[1], sys.argv[2]
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

QUERY = """query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{
totalContributions weeks{contributionDays{date contributionCount weekday}}}}}}"""

THEMES = {
    "dark": dict(surf="#12161b", border="#1f242c", tile="#0b0d10", empty="#1a1f26", text="#e8eaed", muted="#8b919c", amber="#f5b83d"),
    "light": dict(surf="#fffdf9", border="#e2ded4", tile="#f6f4ef", empty="#ebe7dd", text="#15171a", muted="#5f6570", amber="#8f5c0e"),
}
LEVEL_OPACITY = [0, .3, .5, .75, 1]


def fetch():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json",
                 "User-Agent": "profile-activity-panel"})
    data = json.load(urllib.request.urlopen(req, timeout=30))
    if "errors" in data:
        raise SystemExit(data["errors"])
    return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def fonts():
    src = open(os.path.join(ROOT, "assets", "header-dark.svg"), encoding="utf-8").read()
    rules = re.findall(r"@font-face\{font-family:'(?:Bricolage Grotesque|JetBrains Mono)'.*?\}", src)
    if len(rules) != 2:
        raise SystemExit("could not find embedded fonts in assets/header-dark.svg")
    return "".join(rules)


def stats(days):
    counts = [d["contributionCount"] for d in days]
    longest = run = 0
    for n in counts:
        run = run + 1 if n else 0
        longest = max(longest, run)
    current, i = 0, len(counts) - 1
    if counts and counts[-1] == 0:
        i -= 1  # today not counted yet
    while i >= 0 and counts[i]:
        current += 1
        i -= 1
    best = max(days, key=lambda d: d["contributionCount"])
    return longest, current, best


def level(n, cuts):
    if n == 0:
        return 0
    return 1 + sum(n > c for c in cuts)


def render(cal, t, css_fonts):
    c = THEMES[t]
    weeks = cal["weeks"]
    days = [d for w in weeks for d in w["contributionDays"]]
    longest, current, best = stats(days)
    nz = sorted(d["contributionCount"] for d in days if d["contributionCount"])
    cuts = [nz[int(len(nz) * q)] for q in (.25, .5, .75)] if nz else [1, 2, 3]

    W, CELL, GAP = 1200, 15, 4
    P = 28
    GX, GY = 96, 222
    grid_w = len(weeks) * (CELL + GAP) - GAP
    H = GY + 7 * (CELL + GAP) + 64
    best_date = dt.date.fromisoformat(best["date"]).strftime("%b %d").upper()
    updated = dt.datetime.now(dt.timezone.utc).strftime("%d %b %Y").upper()

    css = (css_fonts +
           ".d{font-family:'Bricolage Grotesque',sans-serif;font-weight:800}.m{font-family:'JetBrains Mono',monospace}"
           "@keyframes up{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}"
           "@keyframes fade{from{opacity:0}to{opacity:1}}"
           f"@keyframes beam{{0%{{transform:translateX(0);opacity:0}}6%{{opacity:1}}60%{{opacity:1}}66%,100%{{transform:translateX({grid_w + 40}px);opacity:0}}}}"
           ".up{animation:up .8s cubic-bezier(.2,.7,.2,1) both}.col{animation:fade .5s ease both}"
           ".beam{animation:beam 7s cubic-bezier(.45,0,.55,1) 1.6s infinite both}"
           "@media (prefers-reduced-motion:reduce){*{animation:none!important}}")
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
           f"<style>{css}</style>",
           f'<defs><linearGradient id="bm" x1="0" x2="1"><stop offset="0" stop-color="{c["amber"]}" stop-opacity="0"/>'
           f'<stop offset=".85" stop-color="{c["amber"]}" stop-opacity=".22"/><stop offset="1" stop-color="{c["amber"]}" stop-opacity=".9"/></linearGradient>'
           f'<clipPath id="gc"><rect x="{GX - 4}" y="{GY - 4}" width="{grid_w + 8}" height="{7 * (CELL + GAP) + 4}"/></clipPath></defs>',
           f'<rect x=".75" y=".75" width="{W - 1.5}" height="{H - 1.5}" rx="16" fill="{c["surf"]}" stroke="{c["border"]}" stroke-width="1.5"/>',
           f'<rect x="{P}" y="33" width="8" height="8" rx="2" fill="{c["amber"]}"/>',
           f'<text x="{P + 18}" y="42" class="m" font-size="13" fill="{c["muted"]}" letter-spacing="2.5">CONTRIBUTIONS · LAST 12 MONTHS</text>',
           f'<text x="{W - P}" y="42" class="m" font-size="12" fill="{c["muted"]}" letter-spacing="2" text-anchor="end">UPDATED {updated}</text>']

    tiles = [(f'{cal["totalContributions"]:,}', "CONTRIBUTIONS", True), (f"{longest}d", "LONGEST STREAK", False),
             (f"{current}d", "CURRENT STREAK", False), (str(best["contributionCount"]), f"BEST DAY · {best_date}", False)]
    tw = (W - 2 * P - 3 * 16) / 4
    for i, (big, lab, hl) in enumerate(tiles):
        x = P + i * (tw + 16)
        out.append(f'<g class="up" style="animation-delay:{.1 + i * .1:.2f}s">'
                   f'<rect x="{x:.1f}" y="64" width="{tw:.1f}" height="100" rx="14" fill="{c["tile"]}" stroke="{c["border"]}" stroke-width="1.3"/>'
                   f'<text x="{x + 22:.1f}" y="118" class="d" font-size="40" letter-spacing="-1" fill="{c["amber"] if hl else c["text"]}">{big}</text>'
                   f'<text x="{x + 23:.1f}" y="146" class="m" font-size="12" letter-spacing="1.5" fill="{c["muted"]}">{lab}</text></g>')

    last_month = None
    for wi, w in enumerate(weeks):
        first = dt.date.fromisoformat(w["contributionDays"][0]["date"])
        if first.month != last_month and first.day <= 7 and wi < len(weeks) - 2:
            out.append(f'<text x="{GX + wi * (CELL + GAP)}" y="{GY - 12}" class="m" font-size="11" letter-spacing="1" fill="{c["muted"]}">{first.strftime("%b").upper()}</text>')
            last_month = first.month
    for wd, name in ((1, "MON"), (3, "WED"), (5, "FRI")):
        out.append(f'<text x="{GX - 14}" y="{GY + wd * (CELL + GAP) + 11.5}" class="m" font-size="11" letter-spacing="1" fill="{c["muted"]}" text-anchor="end">{name}</text>')
    for wi, w in enumerate(weeks):
        cells = []
        for d in w["contributionDays"]:
            lv = level(d["contributionCount"], cuts)
            x, y = GX + wi * (CELL + GAP), GY + d["weekday"] * (CELL + GAP)
            fill = f'fill="{c["empty"]}"' if lv == 0 else f'fill="{c["amber"]}" fill-opacity="{LEVEL_OPACITY[lv]}"'
            cells.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3.5" {fill}>'
                         f'<title>{d["contributionCount"]} on {d["date"]}</title></rect>')
        out.append(f'<g class="col" style="animation-delay:{.4 + wi * .018:.3f}s">{"".join(cells)}</g>')
    out.append(f'<g clip-path="url(#gc)"><g class="beam"><rect x="{GX - 44}" y="{GY - 4}" width="40" height="{7 * (CELL + GAP) + 4}" fill="url(#bm)"/></g></g>')

    ly = GY + 7 * (CELL + GAP) + 30
    lx = GX + grid_w - 5 * (CELL + 4) - 40
    out.append(f'<text x="{lx - 10}" y="{ly + 11.5}" class="m" font-size="11" letter-spacing="1" fill="{c["muted"]}" text-anchor="end">LESS</text>')
    for i in range(5):
        fill = f'fill="{c["empty"]}"' if i == 0 else f'fill="{c["amber"]}" fill-opacity="{LEVEL_OPACITY[i]}"'
        out.append(f'<rect x="{lx + i * (CELL + 4)}" y="{ly}" width="{CELL}" height="{CELL}" rx="3.5" {fill}/>')
    out.append(f'<text x="{lx + 5 * (CELL + 4) + 6}" y="{ly + 11.5}" class="m" font-size="11" letter-spacing="1" fill="{c["muted"]}">MORE</text>')
    out.append(f'<text x="{GX}" y="{ly + 11.5}" class="m" font-size="11" letter-spacing="1.5" fill="{c["muted"]}">@{LOGIN.upper()}</text>')
    out.append("</svg>")
    return "".join(out)


def main():
    cal = fetch()
    css_fonts = fonts()
    os.makedirs(OUT, exist_ok=True)
    for t in THEMES:
        with open(os.path.join(OUT, f"activity-{t}.svg"), "w", encoding="utf-8", newline="") as f:
            f.write(render(cal, t, css_fonts))
    print(f"wrote activity-dark.svg and activity-light.svg ({cal['totalContributions']} contributions)")


if __name__ == "__main__":
    main()
