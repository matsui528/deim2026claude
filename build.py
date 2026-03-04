import json

TEMPLATE = "template.html"
PAPERS   = "papers.json"
OUTPUT   = "index.html"
PLACEHOLDER = "<!-- PUBLICATIONS -->"


def render_paper(paper):
    lines = []
    lines.append("      <li>")
    lines.append(f'        <div class="pub-title">{paper["title"]}</div>')
    lines.append(f'        <div class="pub-authors">{paper["authors"]}</div>')
    lines.append(f'        <div class="pub-venue">{paper["conf"]}</div>')

    # optional links: "paper", "code", "project", "slides", "video"
    link_keys = ["paper", "code", "project", "slides", "video"]
    links = {k: paper[k] for k in link_keys if k in paper}
    if links:
        lines.append('        <div class="pub-links">')
        for label, url in links.items():
            lines.append(f'          <a href="{url}">{label.capitalize()}</a>')
        lines.append("        </div>")

    lines.append("      </li>")
    return "\n".join(lines)


def build():
    with open(PAPERS, encoding="utf-8") as f:
        papers = json.load(f)

    with open(TEMPLATE, encoding="utf-8") as f:
        template = f.read()

    pub_html = "\n".join(render_paper(p) for p in papers)
    output = template.replace(PLACEHOLDER, pub_html)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Generated {OUTPUT} with {len(papers)} paper(s).")


if __name__ == "__main__":
    build()
