---
name: avoid-ai-writing
description: "Audit and rewrite content to remove 21 categories of AI writing patterns with a 43-entry replacement table."
risk: none
source: https://github.com/conorbronsdon/avoid-ai-writing
date_added: "2026-03-06"
---

# Avoid AI Writing — Audit & Rewrite

Detects and fixes AI writing patterns ("AI-isms") that make text sound machine-generated. Covers 21 pattern categories with a 43-entry word/phrase replacement table.

## When to Use This Skill
- When asked to "remove AI-isms," "clean up AI writing," or "make this sound human"
- After drafting content with AI and before publishing
- When editing any text that sounds generated rather than written

## What It Detects

**21 pattern categories:**
- Formatting issues (em dashes, bold overuse, emoji headers, bullet-heavy)
- Sentence structure (hedging, hollow intensifiers, rule of three)
- Template phrases and transition phrases
- Significance inflation, synonym cycling, filler phrases
- Promotional language, generic conclusions

## Key Replacements (43 entries)
| AI-ism | Replace with |
|--------|-------------|
| leverage | use |
| utilize | use |
| robust | reliable / strong |
| streamline | simplify |
| cutting-edge | newest / latest |
| foster | support / encourage |
| seamless | smooth / easy |
| pivotal | important |
| embark on | start / begin |
| landscape | field / area |
| delve into | look at / explore |
| spearhead | lead |
| harness | use |
| navigate | handle / manage |
| elevate | improve |
| Moreover / Furthermore | (remove or restructure) |
| In today's... | (remove entirely) |
| serves as a testament | shows / proves |

## Output Format
1. **Issues found** — every AI-ism quoted with location
2. **Rewritten version** — cleaned text
3. **What changed** — summary of edits
4. **Second-pass audit** — re-reads to catch surviving tells

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.
