import random


jomle_ha = {
    "ehsasi": [
        "che havaye delneshini!",
        "Ah! , chegadr delam barayat tang shode ast!",
        "In lahze baraye man besyar khas ast!"
    ],
    "khabari": [
        "Emroz hava aftabi ast.", 
        "Ketabat roye miz ast.", 
        "Emshab mah kamel khahad bod." 
    ],
    "porseshi": [
        "Aya emroz be park miravi?", 
        "saat chand ast?",
        "In kar ra tamam kardi?"  
    ],
    "amri": [
        "Dar ra beband.", 
        "Aram sohbat konid saram dard gereft.", 
        "Hamin hala inja bia.!" 
    ],
    "eltemasi": [
        "Lotfan be man komak konid.", 
        "Khahesh mikonam mara bebakhsh.", 
        "Lotfan in forsat ra be man bedahid." 
    ],
    "enshai": [
        "Be nazar man in film besyar jaleb ast.", 
        "Man az in ghaza khosham nayamad.", 
        "Fekr mi konam in ketab besyar amozande ast." 
    ],
    "tosifi": [
        "Aseman abi va saf ast.", 
        "Oo mardi gad boland va laghar ast.", 
        "In gol ha besyar ziba va rangarang hastand." 
    ],
    "taajobi": [
        "Vai! , che ettefagi oftade ast!", 
        "An goshi chegadr ziba ast!",
        "Che suprize bozorgi! " 
    ]
}


def barrasi_noee_jomle(user_input):
    user_input = user_input.strip().lower()  
    for noee_jomle in jomle_ha.keys():
        if noee_jomle in user_input:  
            return noee_jomle
    return None


def generate_sentence(user_input):
    noee_jomle = barrasi_noee_jomle(user_input)
    if noee_jomle:  
        return random.choice(jomle_ha[noee_jomle])
    else:
        return "man az in noe jomle agahi nadaram. bebakhshid!"


print("che noe jomlei mikhahid barayetan dorost konam? (ehsasi,khabari,porseshi,amri,eltemasi,enshai,tosifi,taajobi)")
user_input = input(">>> ")


result = generate_sentence(user_input)
print("jomlei ke barayetan dorost kardam:")
print(result)
