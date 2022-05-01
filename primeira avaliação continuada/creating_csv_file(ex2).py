import csv

fieldnames = ['Esporte', 'Freq. Abs.', 'Freq. Rel.', '%']

data = [
    {   'Esporte': 'Futebol',
        'Freq. Abs.': 108,
        'Freq. Rel.': '?',
        '%': '?'
    },
    {
        'Esporte': 'Vôlei',
        'Freq. Abs.': '?',
        'Freq. Rel.': 0.21,
        '%': '?'
    },
    {
        'Esporte': 'Basquete',
        'Freq. Abs.': '?',
        'Freq. Rel.': '?',
        '%': '?'
    },
    {
        'Esporte': 'Natação',
        'Freq. Abs.': 12,
        'Freq. Rel.': '?',
        '%': '?'
    },
    {
        'Esporte': 'Outros',
        'Freq. Abs.': '?',
        'Freq. Rel.': '?',
        '%': '8.5%'
    },
    {
        'Esporte': 'Total',
        'Freq. Abs.': 200,
        'Freq. Rel.': 1,
        '%': '100%'
    }
]



with open('dist_freq(ex2).csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)