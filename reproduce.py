#!/usr/bin/env python3
"""Recompute the figures in GSC's articles #1 and #5 from screening.csv and compare them with aggregates.csv.

Run in this folder: python3 reproduce.py   (Python 3, standard library only)
"""
import collections
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
TWO = {'two', 'three_four', 'five_plus'}
THREE = {'three_four', 'five_plus'}
AI = 'ai_training_or_evaluation'


def main():
    rows = list(csv.DictReader(open(HERE / 'screening.csv', encoding='utf-8')))
    agg = list(csv.DictReader(open(HERE / 'aggregates.csv', encoding='utf-8')))
    uniq = [r for r in rows if r['counts_in_unique_basis'] == 'yes']
    two = lambda r: r['experience_band'] in TWO
    three = lambda r: r['experience_band'] in THREE
    years = lambda r: float(r['minimum_professional_years']) if r['minimum_professional_years'] else 0
    mine = {}

    def put(claim, measure, population, basis, group, statistic, numerator, denominator):
        value = round(numerator / denominator, 2) if statistic == 'ratio' else (
            numerator if statistic == 'count' else round(100 * numerator / denominator, 1))
        mine[(claim, measure, population, basis, group, statistic)] = (numerator, denominator, value)

    S = 'screened_listings'
    put('F1', 'required 2+ years of professional experience', S, 'listings', 'all', 'share_pct', sum(map(two, rows)), len(rows))
    put('F1', 'required 2+ years of professional experience', S, 'unique_listings', 'all', 'share_pct', sum(map(two, uniq)), len(uniq))
    for basis, subset in (('listings', rows), ('unique_listings', uniq)):
        bands = collections.Counter(r['experience_band'] for r in subset)
        for band, k in bands.items():
            put('F1-dist', 'experience band', S, basis, band, 'share_pct', k, len(subset))
    no_ai = [r for r in rows if r['segment_group'] != AI]
    put('F2', 'required 2+ years', S + '_excluding_ai_training', 'listings', 'all', 'share_pct', sum(map(two, no_ai)), len(no_ai))
    scope = [r for r in rows if r['in_scope'] == 'yes']
    put('F2', 'required 2+ years', S + '_in_scope', 'listings', 'all', 'share_pct', sum(map(two, scope)), len(scope))
    soft = [r for r in rows if r['segment_group'] == 'software']
    put('F2', 'required 2+ years', S + '_software_segment', 'listings', 'all', 'share_pct', sum(map(two, soft)), len(soft))
    put('F3', 'required 3+ years', S, 'listings', 'all', 'share_pct', sum(map(three, rows)), len(rows))
    put('F3', 'required 5+ years', S, 'listings', 'all', 'share_pct', sum(r['experience_band'] == 'five_plus' for r in rows), len(rows))
    put('F3', 'required 8+ years', S, 'listings', 'all', 'share_pct', sum(years(r) >= 8 for r in rows), len(rows))
    put('F3', 'required 10+ years', S, 'listings', 'all', 'share_pct', sum(years(r) >= 10 for r in rows), len(rows))
    for key, k in collections.Counter(r['entry_evidence'] for r in rows).items():
        put('F5', 'entry-level evidence', S, 'listings', key, 'share_pct', k, len(rows))
    jt = [r for r in rows if r['junior_title_flag'] == 'yes']
    put('F6', 'junior-titled and required 2+ years', S, 'listings', 'junior_titled', 'count', sum(map(two, jt)), None)
    put('F6', 'junior-titled and required 2+ years', S, 'unique_listings', 'junior_titled', 'count',
        len({r['text_group_id'] for r in jt if two(r)}), None)
    put('F6', 'junior-titled and required 3+ years', S, 'listings', 'junior_titled', 'count', sum(map(three, jt)), None)
    put('F6', 'junior-titled and required 3+ years', S, 'unique_listings', 'junior_titled', 'count',
        len({r['text_group_id'] for r in jt if three(r)}), None)
    t3, u3 = [r for r in rows if three(r)], [r for r in uniq if three(r)]
    put('F9', 'AI-training listings among listings requiring 3+ years', S, 'listings', 'three_plus', 'share_pct',
        sum(r['segment_group'] == AI for r in t3), len(t3))
    put('F9', 'AI-training listings among listings requiring 3+ years', S, 'unique_listings', 'three_plus', 'share_pct',
        sum(r['segment_group'] == AI for r in u3), len(u3))
    put('F10', 'explicitly accepted no professional experience', S, 'listings', 'all', 'share_pct',
        sum(r['experience_band'] == 'zero' for r in rows), len(rows))
    for population, subset in ((S + '_in_scope', scope), (S, rows)):
        by_state = collections.defaultdict(list)
        for r in subset:
            if r['state']:
                by_state[r['state']].append(r)
        for st, xs in by_state.items():
            if len(xs) >= 100:
                put('F11', 'required 2+ years, by state', population, 'listings', st, 'share_pct', sum(map(two, xs)), len(xs))
    zero = lambda subset: sum(r['experience_band'] == 'zero' for r in subset)
    put('F12', 'ratio of listings requiring 2+ years to listings explicitly accepting none', S, 'listings', 'all', 'ratio',
        sum(map(two, rows)), zero(rows))
    put('F12', 'ratio of listings requiring 2+ years to listings explicitly accepting none', S, 'unique_listings', 'distinct',
        'ratio', sum(map(two, uniq)), zero(uniq))
    put('F12', 'ratio of listings requiring 2+ years to listings explicitly accepting none', S, 'listings', 'excluding_ai_gigs',
        'ratio', sum(map(two, no_ai)), zero(no_ai))
    put('F12', 'ratio of listings requiring 2+ years to listings explicitly accepting none', S, 'listings', 'segment_software_only',
        'ratio', sum(map(two, soft)), zero(soft))
    ai, ai_u = [r for r in rows if r['segment_group'] == AI], [r for r in uniq if r['segment_group'] == AI]
    put('5-1', 'AI-training or evaluation listings', S, 'listings', 'all', 'share_pct', len(ai), len(rows))
    # #5 counts distinct texts among AI-training listings (a text can first appear on a listing coded otherwise).
    put('5-1', 'AI-training or evaluation listings', S, 'unique_listings', 'all', 'share_pct',
        len({r['text_group_id'] for r in ai}), len(uniq))
    put('5-4', 'required 3+ years', S + '_ai_training', 'listings', 'all', 'share_pct', sum(map(three, ai)), len(ai))
    put('5-4', 'required 3+ years', S + '_ai_training', 'unique_listings', 'all', 'count',
        len({r['text_group_id'] for r in ai if three(r)}), None)

    published = {(a['claim_id'], a['measure'], a['population'], a['basis'], a['group'], a['statistic']): a for a in agg}
    ok = bad = 0
    for key, (num, den, value) in sorted(mine.items()):
        a = published.get(key)
        if a is None:
            continue
        same = str(num) == a['numerator'] and (den is None or str(den) == a['denominator']) and \
            abs(float(value) - float(a['value'])) < 0.051
        ok += same
        bad += not same
        label = f"{key[0]:<7} {key[1][:60]:<60} {key[3]:<15} {key[4]:<26}"
        print(f"{'OK      ' if same else 'MISMATCH'} {label} {num}/{den if den else '-'} = {value}  (published {a['value']})")
    print(f'\n{ok} figures reproduced, {bad} mismatches.')
    raise SystemExit(1 if bad else 0)


if __name__ == '__main__':
    main()
