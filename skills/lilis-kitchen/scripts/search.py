#!/usr/bin/env python3
"""Search the Lili's Kitchen public catalog. Python 3 standard library only.

Examples:
  python3 search.py "browser automation"
  python3 search.py "mcp server database" --limit 5
  python3 search.py --category apis "postgres"
  python3 search.py --list-categories
  python3 search.py "vector db" --source ./catalog/catalog.json --json

--source accepts a local file path or an http(s) URL. Default: the catalog on the main
branch of github.com/Aceop-001/lilis-kitchen (raw.githubusercontent.com).
With --category and a URL source, only that category's small JSON file is downloaded.
"""
import argparse, json, math, re, sys, urllib.request

DEFAULT = "https://raw.githubusercontent.com/Aceop-001/lilis-kitchen/main/catalog/catalog.json"
STOP = set("a an the for to of in on and or with my me i find need want some any tool tools project "
           "projects github open source open-source that this is can which use using".split())
SYN = {  # small expansion table so capability words also match common phrasing
    "db": ["database"], "database": ["db", "sql", "postgres", "postgresql", "mysql", "sqlite"],
    "llm": ["language model", "model"], "browser": ["web browser", "playwright", "puppeteer", "selenium", "chrome"],
    "agent": ["agents", "agentic"], "agents": ["agent"], "mcp": ["model context protocol"],
    "inference": ["serving", "llm"], "test": ["testing", "tests"], "testing": ["test", "e2e"],
    "rag": ["retrieval"], "vector": ["embedding", "embeddings"], "scrape": ["scraping", "crawler", "crawl"],
    "skill": ["skills"], "skills": ["skill"], "framework": ["frameworks", "library", "sdk"],
}

def load(src):
    if re.match(r"^https?://", src):
        req = urllib.request.Request(src, headers={"User-Agent": "lilis-kitchen-skill/1"})
        with urllib.request.urlopen(req, timeout=30) as r: return json.loads(r.read().decode("utf-8"))
    with open(src, encoding="utf-8") as f: return json.load(f)

def sibling(src, rel):  # catalog/catalog.json -> catalog/<rel>
    return re.sub(r"catalog\.json$", rel, src)

def tokens(q):
    """Lower-cased search terms. Stopwords and one-letter ASCII tokens are dropped; non-ASCII
    (e.g. CJK) terms are kept and matched literally."""
    out = []
    for t in re.findall(r"[^\W_]+(?:[+#.][^\W_]*)*|[+#]+", q.lower()):
        t = t.strip(".")
        if not t or t in STOP: continue
        if t.isascii() and len(t) < 2: continue
        if t not in out: out.append(t)
    return out

def pattern(a):
    if a.isascii(): return re.compile(r"(?<![a-z0-9])" + re.escape(a))
    return re.compile(re.escape(a))  # literal match for non-ASCII terms

def term_matches(e, t):
    text = (e["name"] + " " + (e.get("description") or "") + " " + e["category"]).lower()
    return any(pattern(a).search(text) for a in [t] + SYN.get(t, []))

def idf_weights(repos, terms):
    """Rarer terms count more (e.g. 'mcp' outweighs 'server'). Terms that match nothing get 0."""
    n = len(repos) or 1; w = {}
    for t in terms:
        df = sum(1 for e in repos if term_matches(e, t))
        w[t] = 0.0 if df == 0 else 1.0 + math.log((n + 1) / (df + 1))
    return w

def score(e, terms, phrase, idf):
    name = e["name"].lower(); desc = (e.get("description") or "").lower(); cat = e["category"].lower()
    s, hits, got = 0.0, 0, 0.0
    for t in terms:
        alts = [t] + SYN.get(t, [])
        w = 0.0
        for i, a in enumerate(alts):
            k = 1.0 if i == 0 else 0.6
            pat = pattern(a)
            if pat.search(name): w = max(w, 3 * k)
            if pat.search(desc): w = max(w, 2 * k)
            if pat.search(cat): w = max(w, 1 * k)
        if w: hits += 1; s += w * idf[t]; got += idf[t]
    if phrase and len(terms) > 1 and phrase in (name + " " + desc): s += 3
    total = sum(idf[t] for t in terms)
    if total: s *= (got / total) ** 1.5  # prefer entries matching more (and rarer) query terms
    return s, hits

def unknown_category(cat, ids):
    print(f"error: no category matches {cat!r}. Valid category ids (a unique part of one also works):\n  "
          + "\n  ".join(ids), file=sys.stderr); sys.exit(2)

def main():
    ap = argparse.ArgumentParser(description="Search the Lili's Kitchen open-source catalog")
    ap.add_argument("query", nargs="*"); ap.add_argument("--source", default=DEFAULT)
    ap.add_argument("--category", help="category id or words, e.g. 'apis-mcp' or 'security'")
    ap.add_argument("--limit", type=int, default=8); ap.add_argument("--json", action="store_true")
    ap.add_argument("--include-archived", action="store_true", help="do not push archived repos to the bottom")
    ap.add_argument("--list-categories", action="store_true")
    a = ap.parse_args(); q = " ".join(a.query).strip()
    if a.limit < 1: ap.error("--limit must be 1 or more")
    try:
        if a.list_categories:
            idx = load(sibling(a.source, "index.json")) if a.source.endswith("catalog.json") else None
            cats = idx["categories"] if idx else None
            if not cats:
                c = load(a.source); seen = {}
                for e in c["repositories"]: seen[e["category_id"]] = seen.get(e["category_id"], 0) + 1
                cats = [{"id": k, "count": v, "title": k} for k, v in seen.items()]
            for c in cats: print(f"{c['id']}\t{c['count']}\t{c['title']}")
            return
        data, repos = None, None
        if a.category and a.source.endswith("catalog.json"):
            try:
                idx = load(sibling(a.source, "index.json"))
                m = [c for c in idx["categories"] if a.category.lower() in c["id"] or a.category.lower() in c["title"].lower()]
                if m: data = idx; repos = [r for c in m for r in load(sibling(a.source, c["file"].split("catalog/", 1)[1]))["repositories"]]
                else: unknown_category(a.category, [c["id"] for c in idx["categories"]])
            except SystemExit: raise
            except Exception: repos = None
        if repos is None:
            data = load(a.source); repos = data["repositories"]
            if a.category:
                ids = sorted({r["category_id"] for r in repos})
                repos = [r for r in repos if a.category.lower() in r["category_id"] or a.category.lower() in r["category"].lower()]
                if not repos: unknown_category(a.category, ids)
    except SystemExit: raise
    except Exception as ex:
        print(f"error: could not load catalog from {a.source}: {ex}", file=sys.stderr); sys.exit(2)
    if not q and not a.category: ap.error("give a query and/or --category")
    terms = tokens(q); phrase = " ".join(terms)
    if q and not terms and not a.category:
        msg = f"No searchable terms in {q!r} (only filler words or one-letter tokens). No matches returned; try capability words such as 'browser automation' or 'vector database'."
        if a.json: print(json.dumps({"query": q, "category": None, "source": a.source, "matched": 0, "results": [], "note": msg}, ensure_ascii=False, indent=1))
        else: print(msg)
        return
    idf = idf_weights(repos, terms)
    terms = [t for t in terms if idf[t] > 0] if any(idf.values()) else terms  # drop terms found nowhere
    phrase_all = phrase
    res = []
    for e in repos:
        s, hits = score(e, terms, phrase_all, idf) if terms else (1.0, 0)
        if s <= 0: continue
        res.append((s, hits, e))
    best = max((h for _, h, _ in res), default=0)
    # weak matches (only one of several terms) are kept only if nothing better exists
    if terms and len(terms) > 1 and best > 1: res = [r for r in res if r[1] >= 2]
    res.sort(key=lambda r: (bool(r[2].get("archived")) and not a.include_archived, -round(r[0], 1), -(r[2].get("stars") or 0)))
    res = res[:a.limit]
    meta = {"query": q, "category": a.category, "source": a.source,
            "metadata_refreshed": data.get("metadata_refreshed"), "matched": len(res)}
    if a.json:
        print(json.dumps({**meta, "results": [{**e, "score": round(s, 2)} for s, _, e in res]}, ensure_ascii=False, indent=1)); return
    print(f"Lili's Kitchen catalog search: {q!r}" + (f" in {a.category!r}" if a.category else "")
          + f" (metadata refreshed {meta['metadata_refreshed']})")
    if not res:
        print("No matches in the Lili's Kitchen catalog."); return
    if terms and len(terms) > 1 and best < 2:
        print("Note: only weak (single-word) matches found; treat these as loose alternatives.")
    spread = {}
    for _, _, e in res: spread[e["category"]] = spread.get(e["category"], 0) + 1
    if len(spread) > 1:
        print("Matches span categories: " + "; ".join(f"{k} ({v})" for k, v in spread.items()))
    for i, (s, _, e) in enumerate(res, 1):
        st = f"{e['stars']:,}" if e.get("stars") is not None else "unavailable"
        d = e.get("description") or "Description unavailable."
        if e.get("description_source") == "vault_note": d += " (vault note)"
        tag = " [ARCHIVED]" if e.get("archived") else ""
        print(f"\n{i}. {e['name']}{tag}  (score {s:.1f})\n   {e['url']}\n   {d}\n"
              f"   Stars: {st} · Language: {e.get('language') or 'Unknown'} · Category: {e['category']}")

if __name__ == "__main__": main()
