import ru_local as ru
s = 0

print('Здравствуйсте! Ответьте на следующие вопросы для расчёта НДФЛ.' )
r = input('Вы находились 183 дня в РФ за последние 12 месяцев или являютесь российским военным, служащим за границей,'
          'или сотрудником органов власти, командированным за рубеж.? ')
if r.lower()=='да':
    asset = input(ru.asset_q1)
    if asset.lower() == 'да':
        family = input(ru.asset_q2)
        exemption = input(ru.asset_q3)
        how_much = input(ru.asset_q4)
        how_long = input(ru.asset_q5)
        profit = input(ru.asset_q6)
        if family.lower() == 'да' or exemption.lower() == 'да' or how_much.lower() == 'да' or how_long.lower() == 'да' \
                or profit.lower() == 'да':
            asset = 0
        else:
            tax_base = int(input(ru.tax_base_asset))
            asset = tax_base * 0.13
    labor = input(ru.labor_q1)
    if labor.lower() == 'да':
        tax_base = int(input(ru.tax_base_labor))
        if tax_base < 5000000:
            labor = tax_base * 0.13
        else:
            labor = tax_base * 0.15
    CLC = input(ru.CLC_q1)
    if CLC.lower() == 'да':
        tax_base = int(input(ru.tax_base_CLC))
        if tax_base < 5000000:
            CLC = tax_base * 0.13
        else:
            CLC = tax_base * 0.15
    divident = input(ru.divident_q1)
    if divident.lower() == 'да':
        tax_base = int(input(ru.tax_base_divident))
        divident = tax_base * 0.13
    others = input(ru.others_q1)
    if others.lower() == 'да':
        tax_base = int(input(ru.tax_base_other))
        others = tax_base * 0.30
    percentage = input('Получали ли вы доход по облигациям с ипотечным покрытием, приобретенным до 1 января 2007 года?')
    if percentage.lower() == 'да':
        percentage = int(input('Введите ваш доход по облигациям с ипотечным покрытием.'))
        percentage *= 0.09
    else:
        percentage = 0
    percentage_1 = input('Получали ли вы доход как учредитель доверительного управления ипотечным покрытием по сертификатам,'
                'приобретенным до 1 января 2007 года? ')
    if percentage_1.lower() == 'да':
        percentage = int(input('Введите ваш доход как учредителя доверительного управления ипотечным покрытием.'))
        percentage *= 0.09
    else:
        percentage = 0
    gain = input('Получали ли вы выигрыши/призы в конкурсах, играх и других мероприятиях в целях рекламы, в части превышения установленных размеров?')
    if gain.lower() == 'да':
        gain = int(input('Введите стоимость выиграша/приза.'))
        gain *= 0.35
    else:
        gain = 0
    coop = input('Платили ли вы за использование денежных средств членов кредитного потребительского кооператива, в части превышения установленных размеров?')
    if coop.lower() == 'да':
        coop = int(input('Введите сумму за использование.'))
        coop *=0.35
    else:
        coop = 0
    deposit = input('Превышал ли ваш доход по вкладам в банках установленных размеров?')
    if deposit.lower() == 'да':
        deposit = int(input('Введите ваш доход по вкладам в банках.'))
        deposit *=0.35
    else:
        deposit = 0
    cooperative = input('Выплачивали ли вы проценты за использование сельскохозяйственным кредитным потребительским кооперативом средств, в части превышения установленных размеров?')
    if cooperative.lower() == 'да':
        cooperative = int(input('Введите сумму выплаченных процентов.'))
        cooperative *=0.35
    else:
        cooperative = 0
    s = asset + labor + CLC + divident + percentage + gain + coop + others + deposit + cooperative
    print(s)
else:
    asset = input('Получали ли вы доход от продажи имущества? ')
    if asset.lower() == 'да':
        age = int(input('Сколько полных лет находилось это имущество в собственности? '))
        if age < 5:
            asset = int(input('Введите полученную сумму. '))
            asset *= 0.3
        else:
            asset = 0
    else:
        asset = 0

    labor = input('Получали ли вы доход от осуществления трудовой деятельности? ')
    if labor.lower() == 'да':
        labor = int(input('Введите сумму дохода. '))
        q1 = input('Являетесь ли вы участником Государственной программы по оказанию содействия добровольному'
                   ' переселению в РФ соотечественников, проживающих за рубежом, а также членами их семей,'
                   ' совместно переселившимися на постоянное место жительства в Российскую Федерацию? ')
        q2 = input('Являетесь ли вы членом экипажей судов, плавающих под Государственным флагом Российской Федерации? ')
        q3 = input('Являетесь ли вы иностранным гражданином или лицом без гражданства, признанными беженцем'
                   ' или получившим временное убежище на территории Российской Федерации? ')
        q4 = input('Являетесь ли вы гражданином стран-членов ЕАЭС (Армения, Белоруссия, Казахстан, Киргизия)? ')
        q5 = input('Являетесь ли вы иностранным гражданином, работающим по патенту? ')
        q6 = input('Являетесь ли вы иностранным гражданином, имеющим статус ВКС (высококвалифицированные специалисты)? ')
        if q1.lower() =='да' or q2.lower() =='да' or q3.lower() =='да' or q4.lower() =='да' or q5.lower() =='да' or q6.lower() =='да':
            if labor <= 5000000:
                labor *= 0.13
            else:
                labor *= 0.15
        else:
            labor *= 0.3
    else:
        labor = 0

    divident = input('Получали ли вы дивиденды? ')
    if divident.lower() == 'да':
        divident_cnt = input('Получали ли вы дивиденты от российских организаций? ')
        if divident_cnt.lower() == 'да':
            divident_cnt = int(input('Введите ваш доход от российских ораганизаций. '))
            divident_cnt *= 0.15
        divident_abr = input('Получали ли вы дивиденды по акциям международных холдинговых компаний, которые являются публичными компаниями? ')
        if divident_abr.lower() == 'да':
            divident_abr = int(input('Введите ваш доход от международных холдинговых компаний. '))
            divident_abr *= 0.05
        divident = divident_abr+divident_cnt
    else:
        divident = 0

    others = input('У вас есть другие доходы? ')
    if others.lower() == 'да':
        others = int(input('Введите их сумму. '))
        others *= 0.3
    else:
        others = 0
    s = asset+labor+divident+others
    print(s)