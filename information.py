from browser.html import *
from translations_de import info_de, static_text_de

def translate(text, language):
    if language == 'de':
        return info_de.get(text, text)
    return text

def translate_ship_stat(stat, value, language):
    if language == 'de':
        if 'slots' in value:
            value = value.replace('slots', info_de.get('slots', 'slots'))
        if 'per side(player)' in value:
            value = value.replace('per side(player)', info_de.get('per side(player)', 'per side(player)'))
        if 'per side(captain)' in value:
            value = value.replace('per side(captain)', info_de.get('per side(captain)', 'per side(captain)'))
        if value.endswith('s'):
            value = value[:-1] + info_de.get('s', 's')
    return value

def gen_info(language='en'):
    shipstats = {
        "Epheria Sailboat": {
            "HP": "1,000,000",
            "Rations": "1,000,000",
            "Base LT": "5,000",
            "Speed": "100%",
            "Accel": "100%",
            "Turn": "110%",
            "Brake": "110%",
            "Inventory": "25 slots",
            "Cabins": "10",
            "Cannon Count": "1 per side(player)",
            "Reload": "17s"
        },
        "Improved Sailboat": {
            "HP": "1,000,000",
            "Rations": "1,000,000",
            "Base LT": "5,000",
            "Speed": "100%",
            "Accel": "100%",
            "Turn": "110%",
            "Brake": "110%",
            "Inventory": "25 slots",
            "Cabins": "10",
            "Cannon Count": "2 per side(captain)",
            "Reload": "15s"
        },
        "Epheria Caravel": {
            "HP": "1,000,000",
            "Rations": "1,100,000",
            "Base LT": "10,000",
            "Speed": "100%",
            "Accel": "100%",
            "Turn": "110%",
            "Brake": "110%",
            "Inventory": "30 slots",
            "Cabins": "30",
            "Cannon Count": "2 per side(captain)",
            "Reload": "15s"
        },
        "Carrack (Advance)": {
            "HP": "1,350,000",
            "Rations": "1,300,000",
            "Base LT": "16,500",
            "Speed": "110%",
            "Accel": "100%",
            "Turn": "115%",
            "Brake": "115%",
            "Inventory": "40 slots",
            "Cabins": "100",
            "Cannon Reload": "13s"
        },
        "Carrack (Balance)": {
            "HP": "1,300,000",
            "Rations": "1,400,000",
            "Base LT": "15,000",
            "Speed": "115%",
            "Accel": "100%",
            "Turn": "115%",
            "Brake": "115%",
            "Inventory": "35 slots",
            "Cabins": "100",
            "Cannon Reload": "12s"
        },
        "Epheria Frigate": {
            "HP": "1,200,000",
            "Rations": "1,000,000",
            "Base LT": "4,000",
            "Speed": "110%",
            "Accel": "110%",
            "Turn": "120%",
            "Brake": "120%",
            "Inventory": "12 slots",
            "Cabins": "10",
            "Cannon Count": "2 per side(player)",
            "Reload": "17s"
        },
        "Improved Frigate": {
            "HP": "1,200,000",
            "Rations": "1,000,000",
            "Base LT": "4,000",
            "Speed": "110%",
            "Accel": "110%",
            "Turn": "120%",
            "Brake": "120%",
            "Inventory": "12 slots",
            "Cabins": "10",
            "Cannon Count": "4 per side(captain)",
            "Reload": "15s"
        },
        "Epheria Galleass": {
            "HP": "1,200,000",
            "Rations": "1,200,000",
            "Base LT": "8,000",
            "Speed": "110%",
            "Accel": "110%",
            "Turn": "120%",
            "Brake": "120%",
            "Inventory": "15 slots",
            "Cabins": "30",
            "Cannon Count": "4 per side(captain)",
            "Reload": "15s"
        },
        "Carrack (Volante)": {
            "HP": "1,250,000",
            "Rations": "1,400,000",
            "Base LT": "13,500",
            "Speed": "120%",
            "Accel": "110%",
            "Turn": "125%",
            "Brake": "125%",
            "Inventory": "20 slots",
            "Cabins": "100",
            "Cannon Reload": "12s"
        },
        "Carrack (Valor)": {
            "HP": "1,300,000",
            "Rations": "1,500,000",
            "Base LT": "13,500",
            "Speed": "115%",
            "Accel": "110%",
            "Turn": "125%",
            "Brake": "125%",
            "Inventory": "20 slots",
            "Cabins": "100",
            "Cannon Reload": "11s"
        },
        "Panokseon": {
            "HP": "2,000,000",
            "Rations": "1,300,000",
            "Base LT": "12,500",
            "Speed": "105%",
            "Accel": "100%",
            "Turn": "110%",
            "Brake": "115%",
            "Inventory": "20 slots",
            "Cabins": "150",
            "Cannon Reload": "13s"
        },
    }
    order = [
        ["Epheria Sailboat", "Improved Sailboat", "Epheria Frigate", "Improved Frigate"],
        ["Epheria Caravel", "Epheria Galleass"],
        ["Carrack (Advance)", "Carrack (Balance)", "Carrack (Volante)", "Carrack (Valor)"],
        ["Panokseon"]
    ]
    ret = P(translate("There is more than 1 way to get an Epheria Sailboat/Frigate. This page shows the upgrade route but you can also purchase it from the CM, craft it directly, or exchange [Event] Radiant Shakatu's Seal x20 for it.", language))
    ret += P(translate("More information can be found", language) + " " + A(translate("at this spreadsheet", language), href="https://docs.google.com/document/d/1basknMfrfcH6AzJD9PkzeUunqrIGTuS6SfXPf3a7pso/preview", target="_blank") + ".")
    ret += P(translate("Barter items that you can trade for ship parts unlock as you finish more trades. You can always trade t1 barter items for verdant stone coupon though.", language))
    ret += P(translate("Ship parts used for upgrade need to be full durability.", language))
    ret += P(translate("All sea monsters can drop parts for upgrading ships. There is no list of which drops are where yet. (Nov-6)", language))
    ret += P(translate("Old Moon Guild daily quests are mutually exclusive(pick 1). EG Nineshark and Young Sea Monster Hunter.", language))
    ret += H2(translate("Upgrade Paths", language)) + BR() + CANVAS(id='shipchart', width=820, height=400) + BR()
    ret += H2(translate("Base Ship Stats", language))
    for table in order:
        t = TABLE()
        tr = TR(TH(translate("Stat", language)))
        for ship in table:
            tr <= TH(translate(ship, language))
        t <= tr

        for key in shipstats[table[0]]:
            tr = TR(TD(translate(key, language)))
            for ship in table:
                translated_value = translate_ship_stat(key, shipstats[ship][key], language)
                tr <= TD(translated_value)
            t <= tr

        ret += t + BR()
    return ret
