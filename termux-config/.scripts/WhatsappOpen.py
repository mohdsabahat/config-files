import subprocess as sp
import json

TITLE="WhatsApp Opener"
URL="https://wa.me/{}"
C_CODES="+91-IN-India,+93-AF-Afghanistan,+358-AX-Aland Islands,+355-AL-Albania,+213-DZ-Algeria,+1684-AS-AmericanSamoa,+376-AD-Andorra,+244-AO-Angola,+1264-AI-Anguilla,+672-AQ-Antarctica,+1268-AG-Antigua and Barbuda,+54-AR-Argentina,+374-AM-Armenia,+297-AW-Aruba,+61-AU-Australia,+43-AT-Austria,+994-AZ-Azerbaijan,+1242-BS-Bahamas,+973-BH-Bahrain,+880-BD-Bangladesh,+1246-BB-Barbados,+375-BY-Belarus,+32-BE-Belgium,+501-BZ-Belize,+229-BJ-Benin,+1441-BM-Bermuda,+975-BT-Bhutan,+591-BO-Bolivia_ Plurinational State of,+387-BA-Bosnia and Herzegovina,+267-BW-Botswana,+55-BR-Brazil,+246-IO-British Indian Ocean Territory,+673-BN-Brunei Darussalam,+359-BG-Bulgaria,+226-BF-Burkina Faso,+257-BI-Burundi,+855-KH-Cambodia,+237-CM-Cameroon,+1-CA-Canada,+238-CV-Cape Verde,+ 345-KY-Cayman Islands,+236-CF-Central African Republic,+235-TD-Chad,+56-CL-Chile,+86-CN-China,+61-CX-Christmas Island,+61-CC-Cocos [Keeling] Islands,+57-CO-Colombia,+269-KM-Comoros,+242-CG-Congo,+243-CD-Congo_ The Democratic Republic of the Congo,+682-CK-Cook Islands,+506-CR-Costa Rica,+225-CI-Cote d'Ivoire,+385-HR-Croatia,+53-CU-Cuba,+357-CY-Cyprus,+420-CZ-Czech Republic,+45-DK-Denmark,+253-DJ-Djibouti,+1767-DM-Dominica,+1849-DO-Dominican Republic,+593-EC-Ecuador,+20-EG-Egypt,+503-SV-El Salvador,+240-GQ-Equatorial Guinea,+291-ER-Eritrea,+372-EE-Estonia,+251-ET-Ethiopia,+500-FK-Falkland Islands [Malvinas],+298-FO-Faroe Islands,+679-FJ-Fiji,+358-FI-Finland,+33-FR-France,+594-GF-French Guiana,+689-PF-French Polynesia,+241-GA-Gabon,+220-GM-Gambia,+995-GE-Georgia,+49-DE-Germany,+233-GH-Ghana,+350-GI-Gibraltar,+30-GR-Greece,+299-GL-Greenland,+1473-GD-Grenada,+590-GP-Guadeloupe,+1671-GU-Guam,+502-GT-Guatemala,+44-GG-Guernsey,+224-GN-Guinea,+245-GW-Guinea-Bissau,+595-GY-Guyana,+509-HT-Haiti,+379-VA-Holy See [Vatican City State],+504-HN-Honduras,+852-HK-Hong Kong,+36-HU-Hungary,+354-IS-Iceland,+62-ID-Indonesia,+98-IR-Iran_ Islamic Republic of Persian Gulf,+964-IQ-Iraq,+353-IE-Ireland,+44-IM-Isle of Man,+972-IL-Israel,+39-IT-Italy,+1876-JM-Jamaica,+81-JP-Japan,+44-JE-Jersey,+962-JO-Jordan,+77-KZ-Kazakhstan,+254-KE-Kenya,+686-KI-Kiribati,+850-KP-Korea_ Democratic People's Republic of Korea,+82-KR-Korea_ Republic of South Korea,+965-KW-Kuwait,+996-KG-Kyrgyzstan,+856-LA-Laos,+371-LV-Latvia,+961-LB-Lebanon,+266-LS-Lesotho,+231-LR-Liberia,+218-LY-Libyan Arab Jamahiriya,+423-LI-Liechtenstein,+370-LT-Lithuania,+352-LU-Luxembourg,+853-MO-Macao,+389-MK-Macedonia,+261-MG-Madagascar,+265-MW-Malawi,+60-MY-Malaysia,+960-MV-Maldives,+223-ML-Mali,+356-MT-Malta,+692-MH-Marshall Islands,+596-MQ-Martinique,+222-MR-Mauritania,+230-MU-Mauritius,+262-YT-Mayotte,+52-MX-Mexico,+691-FM-Micronesia_ Federated States of Micronesia,+373-MD-Moldova,+377-MC-Monaco,+976-MN-Mongolia,+382-ME-Montenegro,+1664-MS-Montserrat,+212-MA-Morocco,+258-MZ-Mozambique,+95-MM-Myanmar,+264-NA-Namibia,+674-NR-Nauru,+977-NP-Nepal,+31-NL-Netherlands,+599-AN-Netherlands Antilles,+687-NC-New Caledonia,+64-NZ-New Zealand,+505-NI-Nicaragua,+227-NE-Niger,+234-NG-Nigeria,+683-NU-Niue,+672-NF-Norfolk Island,+1670-MP-Northern Mariana Islands,+47-NO-Norway,+968-OM-Oman,+92-PK-Pakistan,+680-PW-Palau,+970-PS-Palestinian Territory_ Occupied,+507-PA-Panama,+675-PG-Papua New Guinea,+595-PY-Paraguay,+51-PE-Peru,+63-PH-Philippines,+872-PN-Pitcairn,+48-PL-Poland,+351-PT-Portugal,+1939-PR-Puerto Rico,+974-QA-Qatar,+40-RO-Romania,+7-RU-Russia,+250-RW-Rwanda,+262-RE-Reunion,+590-BL-Saint Barthelemy,+290-SH-Saint Helena_ Ascension and Tristan Da Cunha,+1869-KN-Saint Kitts and Nevis,+1758-LC-Saint Lucia,+590-MF-Saint Martin,+508-PM-Saint Pierre and Miquelon,+1784-VC-Saint Vincent and the Grenadines,+685-WS-Samoa,+378-SM-San Marino,+239-ST-Sao Tome and Principe,+966-SA-Saudi Arabia,+221-SN-Senegal,+381-RS-Serbia,+248-SC-Seychelles,+232-SL-Sierra Leone,+65-SG-Singapore,+421-SK-Slovakia,+386-SI-Slovenia,+677-SB-Solomon Islands,+252-SO-Somalia,+27-ZA-South Africa,+211-SS-South Sudan,+500-GS-South Georgia and the South Sandwich Islands,+34-ES-Spain,+94-LK-Sri Lanka,+249-SD-Sudan,+597-SR-Suriname,+47-SJ-Svalbard and Jan Mayen,+268-SZ-Swaziland,+46-SE-Sweden,+41-CH-Switzerland,+963-SY-Syrian Arab Republic,+886-TW-Taiwan,+992-TJ-Tajikistan,+255-TZ-Tanzania_ United Republic of Tanzania,+66-TH-Thailand,+670-TL-Timor-Leste,+228-TG-Togo,+690-TK-Tokelau,+676-TO-Tonga,+1868-TT-Trinidad and Tobago,+216-TN-Tunisia,+90-TR-Turkey,+993-TM-Turkmenistan,+1649-TC-Turks and Caicos Islands,+688-TV-Tuvalu,+256-UG-Uganda,+380-UA-Ukraine,+971-AE-United Arab Emirates,+44-GB-United Kingdom,+1-US-United States,+598-UY-Uruguay,+998-UZ-Uzbekistan,+678-VU-Vanuatu,+58-VE-Venezuela_ Bolivarian Republic of Venezuela,+84-VN-Vietnam,+1284-VG-Virgin Islands_ British,+1340-VI-Virgin Islands_ U.S.,+681-WF-Wallis and Futuna,+967-YE-Yemen,+260-ZM-Zambia,+263-ZW-Zimbabwe"

def run_cmd(cmd, shell=False):

    output = sp.Popen(cmd, stdout = sp.PIPE, stderr = sp.PIPE, shell = shell)
    ret_code = output.wait()
    op, er = output.communicate()
    print('Return code:', ret_code)
    if ret_code !=0:
        raise Exception(f'Return code of {cmd} is not 0' + er.decode())
    return op.decode()

def get_country_code():

    cmd = ['termux-dialog','text','-t',TITLE,'-i',
           'Country Code','-n']
    #cmd = ['termux-dialog','sheet','-t',f'\"{TITLE}\"','-i',
     #      'Country Code','-v',f'\"{C_CODES}\"']
    #cmd = f'termux-dialog sheet -t {TITLE} -i "Country code" -v "{C_CODES}"'
    raw = run_cmd(cmd)
    op = json.loads(raw)
    c_code = op['text'].split('-')[0]
    return c_code

def get_phone_number():
    cmd = ['termux-dialog','text','-n','-t',TITLE,
           '-i','Phone Number']
    raw = run_cmd(cmd)
    op = json.loads(raw)
    return op['text']

def open_whatsapp(no):
    cmd = ['termux-open', URL.format(no)]
    run_cmd(cmd)

if __name__ == '__main__':

    c_code = get_country_code()
    phone_no = get_phone_number()
    if c_code and phone_no:
        print('Full Phone : +',c_code,'-',phone_no)
        full_phone = c_code + phone_no
        open_whatsapp(full_phone)
    else:
        print('Please enter Country code/Phone Number')
