'''
Кнопова Анна - 50
Балан Каролина - 45
Шилкова Ульяна - 40
'''

import ru_local as ru

s = 0

print(ru.hello)

r = input(ru.r)
if r.lower() == ru.yes:
    asset = input(ru.asset_q1)
    if asset.lower() == ru.yes:
        family = input(ru.asset_q2)
        exemption = input(ru.asset_q3)
        how_much = input(ru.asset_q4)
        how_long = input(ru.asset_q5)
        profit = input(ru.asset_q6)
        tax_base = int(input(ru.tax_base_asset))
        if family.lower() == ru.yes or exemption.lower() == ru.yes or how_much.lower() == ru.yes or \
                how_long.lower() == ru.yes or profit.lower() == ru.yes:
            asset = 0
        elif tax_base < 5000000:
            asset = tax_base * 0.13
    else:
        asset = 0

    labor = input(ru.labor_q1)
    if labor.lower() == ru.yes:
        tax_base = int(input(ru.tax_base_labor))
        if tax_base < 5000000:
            labor = tax_base * 0.13
        elif tax_base >= 5000000:
            labor = tax_base * 0.15
    else:
        labor = 0

    CLC = input(ru.CLC_q1)
    if CLC.lower() == ru.yes:
        tax_base = int(input(ru.tax_base_CLC))
        if tax_base < 5000000:
            CLC = tax_base * 0.13
        elif tax_base >= 5000000:
            CLC = tax_base * 0.15
    else:
        CLC = 0

    divident = input(ru.divident_q1)
    if divident.lower() == ru.yes:
        tax_base = int(input(ru.tax_base_divident))
        divident = tax_base * 0.13
    else:
        divident = 0

    others = input(ru.others_q1)
    if others.lower() == ru.yes:
        tax_base = int(input(ru.tax_base_other))
        others = tax_base * 0.30
    else:
        others = 0

    percentage = input(ru.percentage_n1)
    if percentage.lower() == ru.yes:
        percentage = int(input(ru.tax_base_percentage))
        percentage *= 0.09
    else:
        percentage = 0
    percentage_1 = input(ru.percentage_n2)
    if percentage_1.lower() == 'да':
        percentage = int(input(ru.tax_base_percentage2))
        percentage *= 0.09
    else:
        percentage = 0

    gain = input(ru.gain_n1)
    if gain.lower() == 'да':
        gain = int(input(ru.tax_base_gain))
        gain *= 0.35
    else:
        gain = 0

    coop = input(ru.coop_n1)
    if coop.lower() == 'да':
        coop = int(input(ru.tax_base_coop))
        coop *=0.35
    else:
        coop = 0

    deposit = input(ru.deposit_n1)
    if deposit.lower() == 'да':
        deposit = int(input(ru.tax_base_deposit))
        deposit *=0.35
    else:
        deposit = 0

    cooperative = input(ru.cooperative_n1)
    if cooperative.lower() == 'да':
        cooperative = int(input(ru.tax_base_cooperative))
        cooperative *=0.35
    else:
        cooperative = 0

    asset = int(asset)
    labor = int(labor)
    CLC = int(CLC)
    percentage = int(percentage)
    gain = int(gain)
    coop = int(coop)
    others = int(others)
    deposit = int(deposit)
    cooperative = int(cooperative)
    s = asset + labor + CLC + divident + percentage + gain + coop + others + deposit + cooperative
    print(s)

else:
    asset = input(ru.asset_q1)
    if asset.lower() == ru.yes:
        age = int(input(ru.asset_q7))
        if age < 5:
            asset = int(input(ru.asset_input))
            asset *= 0.3
        else:
            asset = 0
    else:
        asset = 0

    labor = input(ru.labor_q1)
    if labor.lower() == ru.yes:
        labor = int(input(ru.labor_input))
        q1 = input(ru.labor_q2)
        q2 = input(ru.labor_q3)
        q3 = input(ru.labor_q4)
        q4 = input(ru.labor_q5)
        q5 = input(ru.labor_q6)
        q6 = input(ru.labor_q7)
        if q1.lower() == ru.yes or q2.lower() == ru.yes or q3.lower() == ru.yes or q4.lower() == ru.yes \
                or q5.lower() == ru.yes or q6.lower() == ru.yes:
            if labor <= 5000000:
                labor *= 0.13
            else:
                labor *= 0.15
        else:
            labor *= 0.3
    else:
        labor = 0

    divident = input(ru.divident_q1)
    if divident.lower() == ru.yes:
        divident_cnt = input(ru.divident_q2)
        if divident_cnt.lower() == ru.yes:
            divident_cnt = int(input(ru.divident_input1))
            divident_cnt *= 0.15
        divident_abr = input(ru.divident_q3)
        if divident_abr.lower() == ru.yes:
            divident_abr = int(input(ru.divident_input2))
            divident_abr *= 0.05
        divident = divident_abr+divident_cnt
    else:
        divident = 0

    others = input(ru.others_q1)
    if others.lower() == ru.yes:
        others = int(input(ru.others_input))
        others *= 0.3
    else:
        others = 0
    s = asset+labor+divident+others
    print(ru.tax, s)
