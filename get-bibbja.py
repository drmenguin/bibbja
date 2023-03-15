# Fetches bible in plain text from https://malti.global.bible/
import requests
import json
from tqdm import tqdm

api_key = 'GB1Q1dMAKtlkzggBkGecmZE'

book_names = ['Ġenesi', 'Eżodu', 'Levitiku', 'Numri', 'Dewteronomju', 'Ġożwè', 'Mħallfin', 'Rut', '1 Samwel', '2 Samwel', '1 Slaten', '2 Slaten', '1 Kronaki', '2 Kronaki', 'Esdra', 'Neħemija', 'Tobit', 'Ġuditta', 'Ester', 'Ġob', 'Salmi', 'Proverbji', 'Koħèlet', 'L-Għanja tal-Għanjiet', 'Il-Ktieb tal-Għerf', 'Bin Sirak', 'Isaija', 'Ġeremija', 'Lamentazzjonijiet', 'Bàruk', 'Eżekjel', 'Danjel', 'Hosegħa', 'Ġoel', 'Għamos', 'Għabdija', 'Ġona', 'Mikea', 'Naħum', 'Ħabakkuk', 'Sofonija', 'Ħaggaj', 'Żakkarija', 'Malakija', '1 Makkabin', '2 Makkabin', 'Mattew', 'Mark', 'Luqa', 'Ġwanni', 'Atti tal-Appostli', 'Rumani', '1 Korintin', '2 Korintin', 'Galatin', 'Efesin', 'Filippin', 'Kolossin', '1 Tessalonikin', '2 Tessalonikin', '1 Timotju', '2 Timotju', 'Titu', 'Filemon', 'Lhud', 'Ġakbu', '1 Pietru', '2 Pietru', '1 Ġwanni', '2 Ġwanni', '3 Ġwanni', 'Ġuda', 'Apokalissi']

book_abbrevs = ['Gn', 'Ex', 'Lv', 'Nm', 'Dt', 'Jos', 'Jgs', 'Ru', '1Sm', '2Sm', '1Kgs', '2Kgs', '1Chr', '2Chr', 'Ezr', 'Neh', 'Tb', 'Jdt', 'Est', 'Jb', 'Ps', 'Prv', 'Eccl', 'Sg', 'Wis', 'Sir', 'Is', 'Jer', 'Lam', 'Bar', 'Ez', 'Dn', 'Hos', 'Jl', 'Am', 'Ob', 'Jon', 'Mi', 'Na', 'Hb', 'Zep', 'Hg', 'Zec', 'Mal','1Mc', '2Mc', 'Mt', 'Mk', 'Lk', 'Jn', 'Acts', 'Rom', '1Cor', '2Cor', 'Gal', 'Eph', 'Phil', 'Col', '1Thes', '2Thes', '1Tm', '2Tm', 'Ti', 'Phlm', 'Heb', 'Jas', '1Pt', '2Pt', '1Jn', '2Jn', '3Jn', 'Jude', 'Rev']

book_api_abbrevs = ['GEN', 'EXO', 'LEV', 'NUM', 'DEU', 'JOS', 'JDG', 'RUT', '1SA', '2SA', '1KI', '2KI', '1CH', '2CH', 'EZR', 'NEH', 'TOB', 'JDT', 'ESG', 'JOB', 'PSA', 'PRO', 'ECC', 'SNG', 'WIS', 'SIR', 'ISA', 'JER', 'LAM', 'BAR', 'EZK', 'DAG', 'HOS', 'JOL', 'AMO', 'OBA', 'JON', 'MIC', 'NAM', 'HAB', 'ZEP', 'HAG', 'ZEC', 'MAL', '1MA', '2MA', 'MAT', 'MRK', 'LUK', 'JHN', 'ACT', 'ROM', '1CO', '2CO', 'GAL', 'EPH', 'PHP', 'COL', '1TH', '2TH', '1TI', '2TI', 'TIT', 'PHM', 'HEB', 'JAS', '1PE', '2PE', '1JN', '2JN', '3JN', 'JUD', 'REV']

book_lengths = [50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 14, 16, 10, 42, 150, 31, 12, 8, 19, 51, 66, 52, 5, 6, 48, 14, 14, 4, 9, 1, 4, 7, 3, 3, 3, 2, 14, 3, 16, 15, 28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22]

def get_chapter(book, chapter):
    result = ''
    chapter_content = requests.get('https://v2.api.bible/bibles/2cd26dfc051b0283-01/chapters/' + book_api_abbrevs[book] + '.' + str(chapter),
                          params={'content-type': 'json',
                                  'include-verse-spans': 'false',
                                  'include-notes': 'false'},
                          headers={'api-key': api_key,
                                   'sec-gpc': '1'}).text
    chapter_content = json.loads(chapter_content)['data']['content']
    verse = '0'
    for thing in chapter_content:
        thing = denest_items(thing)
        for item in thing['items']:
            if 'name' in item and item['name'] in 'verse':
                line_start = '\n' if verse != '0' else ''
                verse = item['attrs']['number']
                line_start += book_names[book] + '\t'
                line_start += book_abbrevs[book] + '\t'
                line_start += str(book+1) + '\t'
                line_start += str(chapter) + '\t'
                result += line_start + verse + '\t'
            elif 'text' in item and verse != '0':
                if thing['attrs']['style'] in ['d','m','p','q']:
                    if item['text'].strip() == '' or item['text'].strip()[0] in [',','.',':',';','!','?']:
                        result = result.strip(' ')
                    result += item['text'].strip() + ' '
    return result + '\n'

def denest_items(d):
    if 'items' in d and ('name' not in d or d['name'] != 'verse'):
        d_items = [denest_items(item) for item in d['items']]
        d['items'] = []
        for item in d_items:
            if 'items' in item and ('name' not in item or item['name'] != 'verse'):
                d['items'] += item['items']
                item['items'] = []
            d['items'].append(item)
    return d

with open('bibbja.tsv', 'w') as f:
    for b in (bar := tqdm(range(73), position=0)):
        bar.set_description("Downloading (%s)" % book_names[b])
        for ch in tqdm(range(1,book_lengths[b]+1), position=1, leave=False):
            f.write(get_chapter(b,ch))
