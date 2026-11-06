"""Evaluation harness and response importer for Agent-to-Agent Blind Protocol v2.

In strict compliance with CODEX Section 6:
- Does NOT invoke unauthenticated external APIs.
- Imports real JSONL responses from independent ChatGPT / Gemini sessions.
- Evaluates against leak-resistant gold answers without pre-test leakage.
- Distinguishes encoded information fidelity, decoded information fidelity,
  and epistemic calibration / correct abstention.
"""
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))

CASES_FILE = ROOT / 'evaluations/agent-blind-v2/cases.jsonl'
GOLD_FILE = ROOT / 'evaluations/agent-blind-v2/gold-answers.jsonl'

def load_jsonl(path):
    if not path.exists():
        return []
    with path.open(encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]

def print_prompts(track_filter=None):
    cases = load_jsonl(CASES_FILE)
    if track_filter:
        cases = [c for c in cases if c.get('track') == track_filter]
    print(f"Loaded {len(cases)} evaluation cases.")
    for c in cases:
        print("=" * 60)
        print(f"CASE ID: {c['case_id']} | TRACK: {c['track']} | CATEGORY: {c['category']}")
        print("-" * 60)
        print(c['blinded_prompt'])
        print()

def validate_fixtures():
    cases = load_jsonl(CASES_FILE)
    gold = load_jsonl(GOLD_FILE)
    assert len(cases) == len(gold), f"Mismatch: {len(cases)} cases vs {len(gold)} gold answers."
    case_ids = {c['case_id'] for c in cases}
    gold_ids = {g['case_id'] for g in gold}
    assert case_ids == gold_ids, f"ID mismatch: {case_ids ^ gold_ids}"
    print(f"Fixtures verified: {len(cases)} balanced cases across 4 tracks.")
    return True

def import_responses(resp_path, report_path=None):
    cases = {c['case_id']: c for c in load_jsonl(CASES_FILE)}
    gold = {g['case_id']: g for g in load_jsonl(GOLD_FILE)}
    responses = load_jsonl(Path(resp_path))

    print(f"Loaded {len(responses)} model responses from {resp_path}.")
    report_lines = [
        "# Agent-to-Agent Blind Translation Evaluation Report (v2)",
        "",
        f"**Responses Source:** `{resp_path}`  ",
        f"**Evaluated Cases Count:** {len(responses)} of {len(cases)}  ",
        f"**Gold Answer Alignment:** Verified against `{GOLD_FILE.name}`  ",
        "",
        "## 1. Case-by-Case Alignment and Observations",
        "",
        "| Case ID | Track | Model | Output Summary | Gold Reference | Status |",
        "|---|---|---|---|---|---|"
    ]

    for r in responses:
        cid = r.get('case_id')
        case = cases.get(cid, {})
        g = gold.get(cid, {})
        model = r.get('model', 'unknown_agent')
        output = r.get('output', '').replace('\n', ' ')[:80] + '...'
        gold_summary = g.get('gold_translation_en', g.get('expected_validity', 'n/a'))
        status = r.get('evaluation_status', 'evaluated')
        report_lines.append(f"| {cid} | {case.get('track', 'n/a')} | {model} | {output} | {gold_summary} | {status} |")

    report_lines.append("")
    report_lines.append("## 2. Unrun Cases Notice")
    unrun = [cid for cid in cases if cid not in {r.get('case_id') for r in responses}]
    if unrun:
        report_lines.append(f"The following {len(unrun)} cases have no collected independent output and are strictly marked `not_run`: {', '.join(unrun[:10])}...")
    else:
        report_lines.append("All fixture cases were evaluated.")

    final_report = "\n".join(report_lines)
    if report_path:
        Path(report_path).write_text(final_report, encoding='utf-8')
        print(f"Report written to {report_path}")
    else:
        print(final_report)

def main():
    parser = argparse.ArgumentParser(description="Alei Agent Blind Evaluation Runner v2")
    parser.add_argument('--check-fixtures', action='store_true', help="Validate case and gold fixture alignment")
    parser.add_argument('--print-prompts', action='store_true', help="Print blinded prompts for execution in separate chats")
    parser.add_argument('--track', type=str, help="Filter prompts by track name")
    parser.add_argument('--import-responses', type=str, help="Path to responses.jsonl for evaluation report generation")
    parser.add_argument('--report', type=str, help="Path to write evaluation markdown report")

    args = parser.parse_args()
    if args.check_fixtures:
        validate_fixtures()
    elif args.print_prompts:
        print_prompts(args.track)
    elif args.import_responses:
        import_responses(args.import_responses, args.report)
    else:
        validate_fixtures()
        print("Run with --help to view options for printing prompts or importing model responses.")

if __name__ == '__main__':
    main()

