"""Validate this instruction-only skill repository using Python's standard library."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'yta-production-playbook'


def validate():
    errors = []
    entry = SKILL / 'SKILL.md'
    if not entry.is_file():
        return ['Missing skill entrypoint']
    text = entry.read_text(encoding='utf-8')
    front = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not front:
        errors.append('Missing YAML frontmatter')
    else:
        fields = dict(re.findall(r'^(name|description):\s*(.+)$', front[1], re.M))
        if fields.get('name') != SKILL.name:
            errors.append('Skill name must match folder name')
        if not fields.get('description', '').strip():
            errors.append('Missing description')
    required = ['project-brief.md', 'prompt-1-content-ideas.md', 'prompt-2-video-script.md',
                'prompt-3-scenes.md', 'prompt-4-thumbnails.md', 'prompt-5-titles.md',
                'research.md', 'worked-pilot.md', 'operations-sources.md']
    for name in required:
        if not (SKILL / 'references' / name).is_file():
            errors.append(f'Missing reference: {name}')
    for file in ROOT.rglob('*.md'):
        if '.git' in file.relative_to(ROOT).parts:
            continue
        body = file.read_text(encoding='utf-8')
        if re.search(r'[A-Z]:[/\\](?:Users|Program Files)[/\\]', body):
            errors.append(f'Host-specific path: {file.relative_to(ROOT)}')
        for target in re.findall(r'\]\(([^)]+)\)', body):
            if re.match(r'^(?:https?://|mailto:|#)', target):
                continue
            destination = (file.parent / target.split('#')[0]).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                errors.append(f'Broken local link in {file.relative_to(ROOT)}: {target}')
    for file in list((SKILL / 'templates').glob('*.json')) + list((SKILL / 'examples').glob('*.json')):
        try:
            brief = json.loads(file.read_text(encoding='utf-8'))
            for key in ['channel_id', 'episode_id', 'evidence_mode', 'output_mode']:
                if key not in brief:
                    errors.append(f'{file.name}: missing {key}')
            for key in ['target_seconds', 'fps', 'max_clip_seconds']:
                if not isinstance(brief.get(key), (int, float)) or brief[key] <= 0:
                    errors.append(f'{file.name}: invalid {key}')
            if not 0 <= brief['planned_silence_seconds'] < brief['target_seconds']:
                errors.append(f'{file.name}: silence must fit runtime')
        except (ValueError, KeyError, TypeError) as exc:
            errors.append(f'{file.name}: {exc}')
    metadata = SKILL / 'agents' / 'openai.yaml'
    if not metadata.is_file():
        errors.append('Missing Codex interface metadata')
    return errors


if __name__ == '__main__':
    problems = validate()
    if problems:
        print('\n'.join('ERROR: ' + p for p in problems))
        sys.exit(1)
    print('PASS: metadata, references, local links, portability, and JSON briefs')
