agents = {
    '1SG.SUBJ': 'ŋe',
    '1E.SUBJ':  'ma',
    '1I.SUBJ':  'ŋo',
    '2S.SUBJ':  'ri',
    '2P.SUBJ':  'i',
    '3AN.SUBJ': 'to',
    '3IN.SUBJ': 'ñe',
    '3PL.SUBJ': 'je'
    }

patients = {
    '1SG': 'n',
    '1E':  'ñu',
    '1I':  'ma',
    '2S':  'rii',
    '2P':  'yi',
    '3AN': 'tu',
    '3IN': 'in',
    '3PL': 'ja'
    }

evidentials = {
    'HSY':  'nạ',
    'INFR': 'ñi',
    'NEG':  'pa'
    }

# applicatives = {
#     'PRIV':  'tahamuwi',
#     'LOC':   'nạ',
#     'INSTR': 'na',
#     'BEN':   'raha',
#     'DAT':   'raha',
#     'DUR':   'saña'
#     }
#
# applicative_objects = {
#     'time':  'nạr',
#     'thing': 'pe',
#     'place': 'xaa'
#     }

tenses = {
    'FUT': 'ruw',
    'REC': 'ye',
    'REM': 'dah'
    }

aspects = {
    'HAB':  'nawex',
    'PERF': 'law'
    }

moods = {
    'SUBJ': 'so',
    'COND': 'ław',
    'OPT':  'saŋ',
    'DESD': 'sek'
    }

coordinators = {
    'AND':  'rali',
    'OR':   'ạạn',
    'XOR':  'puun',
    'REL':  'se',
    'BECAUSE.SS': 'nạŋ',
    'BECAUSE.DS': 'tinaŋ',
    'BUT.SS': 'kati',
    'BUT.DS': 'peheku',
    'THEN.SS': 'peheta',
    'THEN.DS': 'pehetu'
    }


def get_atr_harmony(morpheme):
    if morpheme == '':
        return 0
    if 'a' in morpheme or 'e' in morpheme or 'i' in morpheme or 'u' in morpheme or 'o' in morpheme:
        return 1
    if 'ụ' in morpheme or 'ọ' in morpheme or 'ị' in morpheme or 'ẹ' in morpheme or 'ạ' in morpheme:
        return -1
    return 0


def atr_harmonize(morpheme, atr):
    # -ATR
    if atr < 0:
        return morpheme.replace('a', 'ạ').replace('e', 'ẹ').replace('i', 'ị').replace('o', 'ọ').replace('u', 'ụ')
    # +ATR
    if atr > 0:
        return morpheme.replace('ạ', 'a').replace('ẹ', 'e').replace('ị', 'i').replace('ọ', 'o').replace('ụ', 'u')
    return morpheme


def conjugate(verb, args):
    stem_harmony = get_atr_harmony(verb)
    agent = ''
    evidential_harmony = 0
    evidential = ''
    patient = ''
    tense = ''
    aspect = ''
    mood = ''
    coordinator = ''
    for arg in args:
        arg = arg.upper()
        if evidential == '' and arg in evidentials.keys():
            evidential = evidentials[arg]
            evidential_harmony = get_atr_harmony(evidential)
            continue
        if agent == '' and arg in agents.keys():
            agent = agents[arg]
            continue
        if patient == '' and arg in patients.keys():
            patient = atr_harmonize(patients[arg], stem_harmony)
            continue
        if tense == '' and arg in tenses.keys():
            tense = atr_harmonize(tenses[arg], stem_harmony)
            continue
        if aspect == '' and arg in aspects.keys():
            aspect = atr_harmonize(aspects[arg], stem_harmony)
            continue
        if arg in moods.keys():
            mood = atr_harmonize(moods[arg], stem_harmony)
            continue
        if coordinator == '' and arg in coordinators.keys():
            coordinator = atr_harmonize(coordinators[arg], stem_harmony)
    agent = atr_harmonize(agent, evidential_harmony)

    return agent + evidential + patient + tense + aspect + mood + verb + coordinator


