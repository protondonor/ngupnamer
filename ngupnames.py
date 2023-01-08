import random
from dataclasses import dataclass
from typing import List


@dataclass
class Lang:
    name: str
    months: List[str]
    numbers: List[str]
    bynames: List[str]
    given_names: List[str]


def init_langs():
    kwang_names = [
        "A", "Ain", "Auq", "Bãi", "Bãichù", "Baq",
        "Bàw", "Boun", "Chauq", "Chì", "Dã", "Dai",
        "Dan", "Do", "Du", "Dwẽ", "Ein", "Gai",
        "Gain", "Gan", "Gi, Giq", "Goun", "Gu",
        "Gwa", "Hà", "Hã", "Hà'auq", "Hài", "Hàin",
        "Hi", "Ì", "Iq", "Ja", "Jan", "Jèin", "Ji",
        "Jwa", "Khã", "Khò", "Kõ", "Kouq", "Kũ",
        "Kyain", "Lhã", "Lhãw", "Lhè", "Lhòun",
        "Lhouq", "Li", "Loun", "Lu", "Lu", "Lwe",
        "Lwẽ", "Lya", "Lyeiq", "Lyĩ", "Mai", "Mein",
        "Meiq", "Mhain", "Mheiq", "Mi", "Na", "Nã",
        "Ne", "Nẽ", "Ngòun", "Nyãw", "Nyhu", "O",
        "Oun", "Pàn", "Pauq", "Phà", "Phàdwẽ",
        "Phauq", "Phiq", "Phõ", "Pi", "Puq", "Sãw",
        "Sein", "Sẽo", "Shã", "Shaiq", "Sheiq",
        "Shì", "Shĩ", "Shu", "Swã", "Swẽ", "Swu",
        "Thã", "Thãboun", "Thẽ", "Thì", "Tiq",
        "Toun", "Two", "Tyan", "Uq", "Waun", "Wẽ",
        "Whaiq", "Whoun", "Wo'nyi", "Ya", "Ya",
        "Yã", "Yauq", "Yèin", "Yèin Li", "Youq",
        "Zã", "Zaiq", "Ze", "Zẽ", "Zòun", "Zù",
        "Zũ", "Zũ"
    ]
    kwang = Lang(
        'kwang',
        [],
        [],
        kwang_names,
        kwang_names
    )

    chinh = Lang(
        'chinh',
        [
            'Xìng', 'Sang', 'Kwèį', 'Kang', 'Èng', 'Lhìng', 'Mùng',
            'Dèng', 'Chàįy', 'Blhįmh', 'Chung', 'Gàįng'
        ],
        [
            'Mwì', 'Įįmwì', 'Lhì', 'Įįlhì', 'Lhìa', 'Ngdį̀m', 'Ngdeà',
            'Ngdeì', 'Ngkį̀nb', 'Jąą̀mh'
        ],
        [
            'chą̀ąmhchą̀ąmh', 'ganh', 'líì', 'rįng', 'yįį́k', 'teók'
        ],
        []
    )

    for number in chinh.numbers[:-1]:
        chinh.numbers.append('Jąą̀mh ' + number)
        chinh.numbers.append('Į́įmwì Jąą̀mh ' + number)

    ndxiixun = Lang(
        'ndxiixun',
        [
            'Kwą¹rá²se²', 'Chi²¹xí²', 'Za²ñą¹³',
            'Ñą¹³mba³', 'Ru²¹qua²', 'Ti¹rú³',
            'Wá²ko¹xe²', 'Ñį²nda¹³', 'Ku¹su³hi¹',
            'Lli¹³ya³mba¹te¹xe²', 'Mbi²ché³la¹', 'Sa³¹ka¹',
            'Ŋų¹nį́²́'
        ],
        [
            'Mbi³', 'Rra³', 'Li³', 'Hé³xi²', 'Ha³',
            'Nį́³', 'Nde¹rra³', 'Nde¹li³', 'Ŋgo³kú³', 'Zį²ʼą¹zą²'
        ],
        [
            'Se²', 'I²chi²', 'Ŋą́²se²', 'Ñų²hų́²', 'Sį́²', 'Ru³',
            'Xą²', 'Á²xi²', 'Mį¹ŋą́²', 'Ya³ta³', 'Pi³', 'Yu³',
            'Ñdxu²', 'Ñdxé²', 'Rra²lli¹ʼi²', 'Ya³mą²sa¹nda²xi²'
        ],
        []
    )

    for number in ndxiixun.numbers[:-1]:
        ndxiixun.numbers.append('Zį²ʼą¹zą² ' + number)
        ndxiixun.numbers.append('Rra³ Zį²ʼą¹zą² ' + number)

    mañi = Lang(
        'mañi',
        [
            'Hàkmąŗał', 'Chiixichko', 'Zñąą̀', 'Ñąą̀nma',
            'Řuukwa', 'Tirùkkoxał', 'Waxkoxko', 'Ñįnnaàko',
            'Kułùhiko', 'Liìyàmatexe', 'Michèʼŗļani', 'Łàakani',
            'Ŋųnįŋ'
        ],
        [
            'Mwì', 'Rà', 'Ļì', 'Hèx', 'Hà', 'Ŋų̀nįm',
            'Ŋų̀nerà', 'Ŋų̀neļì', 'Ŋòkunm', 'Zįʼązą'
        ],
        [
            'Řù', 'Xą', 'Zą̀ą', 'Zįųñ', 'Mįŋąmb', 'Hàpin', 'Hàtambum', 'Chałŋo',
            'Ąndupokuŋo',  # beautiful
            'Ąndułįŋ',  # bright/light
            'Ąnduwiiwii',  # whisperer
            'Ąnduʼliʼli',  # kind
            'Nąnduŋawkaŋawka',  # I hear they're a liar
            'Nąndòinchiʼdaʼ',  # I hear they stole something
            'Nąnduapaà',  # rumored to be dangerous
            'Nąndotumąyek',  # accused murderer
            'Nąñą Kachaą̀ni'  # scarred
        ],
        [
            'Ząmřani', 'ʼAchùlani', 'Chułiko', 'Ŋàaze', 'Yawuu',
            'Iʼichułko', 'Emiknoʼoł', 'Ateche',
            'Mirèñą Zamřani', 'Į̀ŋuʼa ʼAchùlani', 'Rùchani Chułiko',
            'Mirèʼaa Iʼichułko', 'Chuunchoochhą Ateche',
            'Ŋòruyàļàaex', 'Ñi Kayà', 'Ŋųhŋąą', 'Hàłahu'
        ]
    )

    for number in mañi.numbers[:-1]:
        mañi.numbers.append('Zįʼązą ' + number)
        mañi.numbers.append('Rà Zįʼązą ' + number)

    hlung = Lang(
        'hlung',
        [
            'Jakwarał', 'Xiixixok', 'Sñaa', 'Ñạạnạ',
            'Luukwa', 'Tirukkoxał', 'Waxkoxok', 'Ñịlạạkọ',
            'Kułujiko', 'Liyihi', 'Michehelani', 'Łaakani',
            'Ŋụlịị'
        ],
        [
            'Muwi', 'Ra', 'Li', 'Jex', 'Ja', 'Ŋụlịw',
            'Ŋụlẹrạ', 'Ŋụlẹlị', 'Ŋokun', 'Sịyịhạạsạ'
        ],
        [
            'Tọnụldạh', 'Tohusalosek', 'Ŋoruyalayex', 'Ŋorukoyasehe', 'Tokwikwi',
            'Ñu', 'Yu', 'Ñet', 'Ñek', 'Rar', 'Mịị'
        ],
        [
            'Sạmlạnị', 'Nụhụnụpọk', 'Ñạwịlọlọk', 'Ŋułok', 'Kayani', 'Nụjạŋụ',
            'Lułiŋ', 'Jatawunii', 'Japetmañ', 'Lakahonix'
        ]
    )

    for number in hlung.numbers[:-1]:
        hlung.numbers.append('Sịyịhạạsạ ' + number)
        hlung.numbers.append('Ra Sịyịhạạsạ ' + number)

    nichoh = Lang(
        'nichoh',
        [
            'Jàcuą́uhtlà', 'Chístzi', 'Zñą̂', 'Ñą̂u',
            'Ácuú', 'Tírùj', 'Guascsó', 'Ñįndâ',
            'Cúsùjí', 'Llîmbátzé', 'Mbitzèꞌrguá', 'Tlǎcá',
            'Ŋų́nįuh'
        ],
        [
            'Mbguì', 'Rà', 'Guì', 'Jsè', 'Jà',
            'Nį̀u', 'Ndérà', 'Ndéguì', 'Ŋcòcùu', 'Zįꞌzą́'
        ],
        [],
        []
    )

    for number in nichoh.numbers[:-1]:
        nichoh.numbers.append('Zįꞌzą́ ' + number)
        nichoh.numbers.append('Rà Zįꞌzą́ ' + number)

    awatese = Lang(
        'awatese',
        [
            'Karał', 'Tixin', 'Zahang', 'Nayąnmanga',
            'Řuką', 'Tukoxąru', 'Wąxku', 'Ningną',
            'Kułi', 'Liyąmąte', 'Miteřą', 'Łak',
            'Nguning'
        ],
        [
            'Mwi', 'Řą', 'Łi', 'Exe', 'Ahą',
            'Ngunim', 'Ngunrą', 'Ngunłi', 'Ngukunum',
            'Ziya'
        ],
        [],
        []
    )

    for number in awatese.numbers[:-1]:
        awatese.numbers.append('Ziya ' + number)
        awatese.numbers.append('Řąziya ' + number)

    yashuhay = Lang(
        'yashuhay',
        [
            'Emáathashi', 'Shiishih', 'Kingyáh', 'Ngyaangma',
            'Thuuha', 'Kithu\'oshah', 'Ashihoshih', 'Ngyinggáa',
            'Hushuhi', 'Iyamákeshi', 'Míshe', 'Sháaha',
            'Húngih',
        ],
        [
            'Mya', 'Tho', 'U', 'Akúum', 'Tane',
            'Ngamya', 'Ngatho', 'Ngaw', 'Hommya', 'Taata'
        ],
        [],
        ['Eekak', 'Kutó', 'Hama']
    )

    karduvic = Lang(
        'karduvic',
        [
            'Yàr', 'Ngùkyung', 'Dàng', 'Lì Veng', 'Tyer', 'Tircùr'
        ],
        [
            'Ngè', 'Dè', 'Zì', 'Hòr', 'Hè', 'Dèzì', 'Hèngè', 'Hèdè', 'Hèzì', 'Sot', 'Zur', 'Sov', 'Yozhi', 'Jajū', 'Tong', 'Zuryet', 'Jūyar', 'Mì', 'Ngor', 'Chaurchaur', 'Nger', 'Vek', 'Yizi', 'Yo', 'Ù', 'Vàk', 'Pyo Cù', 'Kèng', 'Sēching', 'Zòr', 'Zheng', 'Tàr', 'Pyezing', 'Mùng'
        ],
        [],
        []
    )

    for number in karduvic.numbers[:-1]:
        karduvic.numbers.append('Sot ' + number)
        karduvic.numbers.append('Dè Sot ' + number)

    for number in karduvic.numbers[0:6]:
        karduvic.numbers.append('Zì Sot ' + number)

    karduvic_surnames = [
        'Jūmè', 'Ngan', 'Yìr', 'Ngyu', 'Lhèng', 'Vorng', 'Pyeng', 'Torzèp', 'Keng', 'Lè', 'Zi', 'Lhehòpep', 'Càurng',
        'Lhèrn', 'Ze', 'Tircù', 'Èngzà', 'Garnga', 'Tiyìnè', 'Sēng', 'Myu', 'Erng', 'Chorcho', 'Ngamo', 'Zhirshu',
        'Zhirhè', 'Vyaur', 'Caung', 'Varva', 'Vordùt', 'Deng', 'Tyiryir', 'Zoch', 'Yàur', 'Tìmè', 'Jē', 'Mve', 'Zhò',
        'Tyoyeng', 'Yarmè', 'Kàurng', 'Mer', 'Turchur', 'Vemu', 'Zukye', 'Shèrgù', 'Ngaumo', 'Pin', 'Gung', 'Pev', 'Tung', 'Sēgung', 'Ortè', 'Tiyaur', 'Dùrtē', 'Kuzavèng', 'Curlàr', 'Har', 'Tye', 'Shingshe', 'Tìdurve', 'Liyaur', 'Yùrn', 'Pekye', 'Pyè', 'Zizi', 'Dēngeng', 'Tyàrya', 'Vornorn', 'Chuchu', 'Myèye', 'Yengyung', 'Va', 'Ter'
    ]

    karduvic_given_names = [
        'Long', 'Tì', 'Tìmè', 'Pazhù', 'Chyo', 'Chup', 'Tyi', 'Kojyù', 'Bir', 'Yù', 'Ngun', 'Zorzor', 'Hèng', 'Hut',
        'Ta', 'Tyek', 'Herngu', 'Bung', 'Zon', 'Tyèng', 'Dùr tèn', 'Mòzev', 'Puvè', 'Urn', 'Zò', 'Pyìr', 'Char', 'Nga',
        'Zìrng', 'Dàng', 'Lhojàk', 'Hizup', 'Yàmizò', 'Sheng', 'Cu', 'Ming', 'Ner jartì', 'Yàrng', 'Cù', 'Yeyer', 'Hur',
        'Tizùk', 'Zavèng', 'Erng', 'Ku', 'Tà', 'Cur', 'Sor', 'Terve', 'Byaung'
    ]

    for surname in karduvic_surnames:
        for given in karduvic_given_names:
            karduvic.given_names.append(surname + ' ' + given)

    for number in yashuhay.numbers[:-1]:
        yashuhay.numbers.append('Taata ' + number)
        yashuhay.numbers.append('Hataha ' + number)

    return {
        'kwang': kwang,
        'chinh': chinh,
        'ndxiixun': ndxiixun,
        'hlung': hlung,
        'mañi': mañi,
        'nichoh': nichoh,
        'awatese': awatese,
        'yashuhay': yashuhay,
        'karduvic': karduvic
    }


def datename(lang):
    month = random.choice(lang.months)
    number = random.choice(lang.numbers)
    return number + ' ' + month


def byname(lang):
    if random.randint(1, 2) > 1:
        return ''
    if len(lang.bynames) == 0:
        return ''
    return random.choice(lang.bynames)


def given_name(lang):
    if lang.name == 'yashuhay' or lang.name == 'karduvic':
        # Always return given names (moiety names) for Yashuhay
        # Always return given names (surname + given name) for Karduvic
        return random.choice(lang.given_names)
    if random.randint(1, 3) > 1:
        return ''
    if len(lang.given_names) == 0:
        return ''
    return random.choice(lang.given_names)


def ngupname(lang):
    if lang.name == 'kwang':
        # Always return bynames (family names) and given names for Kwang
        return random.choice(lang.bynames) + ' ' + random.choice(lang.given_names)
    name = datename(lang)
    this_byname = byname(lang)
    this_given_name = given_name(lang)
    if this_given_name != '':
        name = this_given_name + ' ' + name
    if this_byname != '':
        name = name + ' ' + this_byname
    return name
