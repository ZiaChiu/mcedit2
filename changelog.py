import subprocess

def get_git_log():
    result = subprocess.run(
        ['git', 'log', '--pretty=format:__COMMIT__%h|%ad|%s|%b', '--name-only', '--date=short'],
        stdout=subprocess.PIPE, text=True
    )
    return result.stdout.splitlines()

def parse_git_log(log_lines):
    changelog = []
    entry = {}
    for line in log_lines:
        if line.startswith("__COMMIT__"):
            if entry:
                changelog.append(entry)
            parts = line[len("__COMMIT__"):].split("|", 3)
            entry = {
                "hash": parts[0],
                "date": parts[1],
                "subject": parts[2],
                "body": parts[3].strip() if len(parts) > 3 else "",
                "files": []
            }
        elif line.strip():
            entry["files"].append(line.strip())
    if entry:
        changelog.append(entry)
    return changelog

def format_markdown(changelog_entries):
    lines = []
    for entry in changelog_entries:
        lines.append(f"### {entry['date']}")
        lines.append(f"- **{entry['subject']}** [`{entry['hash']}`]")
        if entry["body"]:
            lines.append(f"  {entry['body']}")
        if entry["files"]:
            lines.append(f"  **Files changed:** {', '.join(entry['files'])}")
        lines.append("")  # Blank line between entries
    return "\n".join(lines)

def main():
    log_lines = get_git_log()
    parsed = parse_git_log(log_lines)
    md_output = format_markdown(parsed)
    with open("changelog.md", "w", encoding="utf-8") as f:
        f.write(md_output)
    print("✅ changelog.md generated.")

if __name__ == "__main__":
    main()
