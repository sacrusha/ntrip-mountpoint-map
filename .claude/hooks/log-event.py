"""Lifecycle hook logger. Reads JSON from stdin, appends TSV row to .tmp/hook_log.tsv.
For sparse events also emits hookSpecificOutput.additionalContext so the marker
appears in Claude's own context — letting us observe ordering vs CLAUDE.md etc.
"""
import sys, json, datetime, pathlib

try:
    raw = sys.stdin.read()
    d = json.loads(raw) if raw.strip() else {}
except Exception as e:
    d = {"_parse_error": str(e)}

ts = datetime.datetime.now().astimezone().isoformat()
event = str(d.get("hook_event_name", ""))
row = [
    ts,
    event,
    str(d.get("agent_id", "")),
    str(d.get("agent_type", "")),
    str(d.get("cwd", "")),
    str(d.get("tool_name", "")),
    str(d.get("source", "")),
]

repo_root = pathlib.Path(__file__).resolve().parent.parent.parent
log_path = repo_root / ".tmp" / "hook_log.tsv"
log_path.parent.mkdir(parents=True, exist_ok=True)
with log_path.open("a", encoding="utf-8") as f:
    f.write("\t".join(c.replace("\t", " ").replace("\n", " ") for c in row) + "\n")

SPARSE = {"SessionStart", "InstructionsLoaded", "SessionEnd", "SubagentStart", "SubagentStop"}
if event in SPARSE:
    marker = f"[hook-marker {ts}] {event}"
    if d.get("source"):
        marker += f" source={d['source']}"
    if d.get("agent_id"):
        marker += f" agent_id={d['agent_id']} agent_type={d.get('agent_type','')}"
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": event,
            "additionalContext": marker,
        }
    }))
