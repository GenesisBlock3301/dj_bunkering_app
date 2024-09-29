from typing import List
from django.utils.safestring import mark_safe


def get_bunker_fuels():
    return [
        {"name": "LSMGO 0.1%", "description": "Low Sulphur Marine Gas Oil with sulphur level max 0.1%"},
        {"name": "LSMGO – 0.5 %", "description": "Low Sulphur Marine Gas Oil with sulphur level max 0.5%"},
        {"name": "VLSFO – 0.1/0.5 %", "description": "Low Sulphur Fuel Oil with sulphur level max 0.5%"},
        {"name": "HSD", "description": "High Speed Diesel for local barges and vessels"}
    ]


def get_services() -> List[dict]:
    return [
        {
            "name": "Physical Bunker Supply",
            "detail": "Physical bunker supply is the core of our operations, ensuring vessels are efficiently "
                      "fueled for their journeys. With our robust network and strategic partnerships, "
                      "we guarantee timely delivery and top-quality fuel, providing peace of mind to maritime "
                      "operators worldwide.", "icon": '<i class="bx bx-gas-pump"></i>'
        },
        {
            "name": "Lubricant Supply",
            "detail": "Our Lubricant Supply service ensures that your machinery and equipment run smoothly and "
                      "efficiently. With a focus on quality products and timely delivery, we provide the "
                      "lubricants you need to maintain optimal performance and minimize downtime.",
            "icon": '<i class="bx bx-cog"></i>'
        },
        {
            "name": "Exporter & Importer",
            "detail": "Our Exporter & Importer service facilitates seamless international trade, connecting "
                      "businesses with global markets. With expertise in logistics, customs regulations, "
                      "and market trends, we streamline the import and export process, ensuring efficient and "
                      "reliable transportation of goods worldwide.",
            "icon": '<i class="bx bx-transfer-alt"></i>'
        },
        {
            "name": "Ship Chandelling",
            "detail": "Ship Chandelling involves the provision of essential supplies and services to ships during "
                      "their stay in port. From supplying provisions and spare parts to offering repair and "
                      "maintenance services, Ship Chandelling ensures smooth operations for vessels, catering to "
                      "their needs efficiently while they're docked.",
            "icon": '<i class="bx bx-import"></i>'
        },
        {
            "name": "Provision & Repair",
            "detail": "Provision & Repair services offered by our company encompass meticulous attention to "
                      "detail and swift, effective solutions. With a focus on reliability and efficiency, "
                      "we ensure that your vessels are equipped and maintained to the highest standards, "
                      "minimizing downtime and optimizing performance on the seas. Trust us to handle your "
                      "provisioning and repair needs with expertise and dedication, keeping your operations "
                      "smooth sailing at all times.",
            "icon": '<i class="bx bx-wrench"></i>'
        },
        {
            "name": "Oil Carrying",
            "detail": "Our Oil Carrying services are executed with utmost precision and adherence to industry "
                      "regulations. From transportation logistics to safe handling procedures, we ensure the "
                      "secure and efficient delivery of oil products, providing peace of mind to our clients "
                      "while meeting their distribution needs seamlessly.",
            "icon": '<i class="bx bxs-truck"></i>'
        },
        {
            "name": "Real estate",
            "detail": "In the realm of real estate, our company stands as a beacon of integrity and innovation. "
                      "With a steadfast commitment to excellence, we offer tailored solutions and unparalleled "
                      "expertise to guide you through every step of your property journey, ensuring your "
                      "investments yield optimal returns and lasting satisfaction.",
            "icon": '<i class="bx bx-home"></i>'
        },
        {
            "name": "Bricks Manufacturing",
            "detail": "Our Bricks Manufacturing division prides itself on producing high-quality bricks tailored "
                      "to meet various construction needs. With a blend of innovative technology and traditional "
                      "craftsmanship, we strive to deliver durable and sustainable building materials, "
                      "contributing to the success of construction projects while prioritizing environmental "
                      "responsibility.",
            "icon": '<i class="bx bx-building-house"></i>'
        }
    ]


def get_check_input_values():
    check_inputs_1 = [
        {'id': 1, 'value': "IFO 380"},
        {'id': 2, 'value': "IFO 180"},
        {'id': 3, 'value': "MGO"},
    ]
    check_inputs_2 = [
        {'id': 1, 'value': "Cargo Discharge at Port", },
        {'id': 2, 'value': "Bunker Call only"}
    ]
    return check_inputs_1, check_inputs_2


def get_country_list():
    return {
        "AF": "Afghanistan",
        "AX": "Åland Islands",
        "AL": "Albania",
        "DZ": "Algeria",
        "AS": "American Samoa",
        "AD": "Andorra",
        "AO": "Angola",
        "AI": "Anguilla",
        "AQ": "Antarctica",
        "AG": "Antigua and Barbuda",
        "AR": "Argentina",
        "AM": "Armenia",
        "AW": "Aruba",
        "AU": "Australia",
        "AT": "Austria",
        "AZ": "Azerbaijan",
        "BS": "Bahamas",
        "BH": "Bahrain",
        "BD": "Bangladesh",
        "BB": "Barbados",
        "BY": "Belarus",
        "BE": "Belgium",
        "BZ": "Belize",
        "BJ": "Benin",
        "BM": "Bermuda",
        "BT": "Bhutan",
        "BO": "Bolivia, Plurinational State of",
        "BQ": "Bonaire, Sint Eustatius and Saba",
        "BA": "Bosnia and Herzegovina",
        "BW": "Botswana",
        "BV": "Bouvet Island",
        "BR": "Brazil",
        "IO": "British Indian Ocean Territory",
        "BN": "Brunei Darussalam",
        "BG": "Bulgaria",
        "BF": "Burkina Faso",
        "BI": "Burundi",
        "KH": "Cambodia",
        "CM": "Cameroon",
        "CA": "Canada",
        "CV": "Cape Verde",
        "KY": "Cayman Islands",
        "CF": "Central African Republic",
        "TD": "Chad",
        "CL": "Chile",
        "CN": "China",
        "CX": "Christmas Island",
        "CC": "Cocos (Keeling) Islands",
        "CO": "Colombia",
        "KM": "Comoros",
        "CG": "Congo",
        "CD": "Congo, the Democratic Republic of the",
        "CK": "Cook Islands",
        "CR": "Costa Rica",
        "CI": "Côte d'Ivoire",
        "HR": "Croatia",
        "CU": "Cuba",
        "CW": "Curaçao",
        "CY": "Cyprus",
        "CZ": "Czech Republic",
        "DK": "Denmark",
        "DJ": "Djibouti",
        "DM": "Dominica",
        "DO": "Dominican Republic",
        "EC": "Ecuador",
        "EG": "Egypt",
        "SV": "El Salvador",
        "GQ": "Equatorial Guinea",
        "ER": "Eritrea",
        "EE": "Estonia",
        "ET": "Ethiopia",
        "FK": "Falkland Islands (Malvinas)",
        "FO": "Faroe Islands",
        "FJ": "Fiji",
        "FI": "Finland",
        "FR": "France",
        "GF": "French Guiana",
        "PF": "French Polynesia",
        "TF": "French Southern Territories",
        "GA": "Gabon",
        "GM": "Gambia",
        "GE": "Georgia",
        "DE": "Germany",
        "GH": "Ghana",
        "GI": "Gibraltar",
        "GR": "Greece",
        "GL": "Greenland",
        "GD": "Grenada",
        "GP": "Guadeloupe",
        "GU": "Guam",
        "GT": "Guatemala",
        "GG": "Guernsey",
        "GN": "Guinea",
        "GW": "Guinea-Bissau",
        "GY": "Guyana",
        "HT": "Haiti",
        "HM": "Heard Island and McDonald Islands",
        "VA": "Holy See (Vatican City State)",
        "HN": "Honduras",
        "HK": "Hong Kong",
        "HU": "Hungary",
        "IS": "Iceland",
        "IN": "India",
        "ID": "Indonesia",
        "IR": "Iran, Islamic Republic of",
        "IQ": "Iraq",
        "IE": "Ireland",
        "IM": "Isle of Man",
        "IL": "Israel",
        "IT": "Italy",
        "JM": "Jamaica",
        "JP": "Japan",
        "JE": "Jersey",
        "JO": "Jordan",
        "KZ": "Kazakhstan",
        "KE": "Kenya",
        "KI": "Kiribati",
        "KP": "Korea, Democratic People's Republic of",
        "KR": "Korea, Republic of",
        "KW": "Kuwait",
        "KG": "Kyrgyzstan",
        "LA": "Lao People's Democratic Republic",
        "LV": "Latvia",
        "LB": "Lebanon",
        "LS": "Lesotho",
        "LR": "Liberia",
        "LY": "Libya",
        "LI": "Liechtenstein",
        "LT": "Lithuania",
        "LU": "Luxembourg",
        "MO": "Macao",
        "MK": "Macedonia, the Former Yugoslav Republic of",
        "MG": "Madagascar",
        "MW": "Malawi",
        "MY": "Malaysia",
        "MV": "Maldives",
        "ML": "Mali",
        "MT": "Malta",
        "MH": "Marshall Islands",
        "MQ": "Martinique",
        "MR": "Mauritania",
        "MU": "Mauritius",
        "YT": "Mayotte",
        "MX": "Mexico",
        "FM": "Micronesia, Federated States of",
        "MD": "Moldova, Republic of",
        "MC": "Monaco",
        "MN": "Mongolia",
        "ME": "Montenegro",
        "MS": "Montserrat",
        "MA": "Morocco",
        "MZ": "Mozambique",
        "MM": "Myanmar",
        "NA": "Namibia",
        "NR": "Nauru",
        "NP": "Nepal",
        "NL": "Netherlands",
        "NC": "New Caledonia",
        "NZ": "New Zealand",
        "NI": "Nicaragua",
        "NE": "Niger",
        "NG": "Nigeria",
        "NU": "Niue",
        "NF": "Norfolk Island",
        "MP": "Northern Mariana Islands",
        "NO": "Norway",
        "OM": "Oman",
        "PK": "Pakistan",
        "PW": "Palau",
        "PS": "Palestine, State of",
        "PA": "Panama",
        "PG": "Papua New Guinea",
        "PY": "Paraguay",
        "PE": "Peru",
        "PH": "Philippines",
        "PN": "Pitcairn",
        "PL": "Poland",
        "PT": "Portugal",
        "PR": "Puerto Rico",
        "QA": "Qatar",
        "RE": "Réunion",
        "RO": "Romania",
        "RU": "Russian Federation",
        "RW": "Rwanda",
        "BL": "Saint Barthélemy",
        "SH": "Saint Helena, Ascension and Tristan da Cunha",
        "KN": "Saint Kitts and Nevis",
        "LC": "Saint Lucia",
        "MF": "Saint Martin (French part)",
        "PM": "Saint Pierre and Miquelon",
        "VC": "Saint Vincent and the Grenadines",
        "WS": "Samoa",
        "SM": "San Marino",
        "ST": "Sao Tome and Principe",
        "SA": "Saudi Arabia",
        "SN": "Senegal",
        "RS": "Serbia",
        "SC": "Seychelles",
        "SL": "Sierra Leone",
        "SG": "Singapore",
        "SX": "Sint Maarten (Dutch part)",
        "SK": "Slovakia",
        "SI": "Slovenia",
        "SB": "Solomon Islands",
        "SO": "Somalia",
        "ZA": "South Africa",
        "GS": "South Georgia and the South Sandwich Islands",
        "SS": "South Sudan",
        "ES": "Spain",
        "LK": "Sri Lanka",
        "SD": "Sudan",
        "SR": "Suriname",
        "SJ": "Svalbard and Jan Mayen",
        "SZ": "Swaziland",
        "SE": "Sweden",
        "CH": "Switzerland",
        "SY": "Syrian Arab Republic",
        "TW": "Taiwan, Province of China",
        "TJ": "Tajikistan",
        "TZ": "Tanzania, United Republic of",
        "TH": "Thailand",
        "TL": "Timor-Leste",
        "TG": "Togo",
        "TK": "Tokelau",
        "TO": "Tonga",
        "TT": "Trinidad and Tobago",
        "TN": "Tunisia",
        "TR": "Turkey",
        "TM": "Turkmenistan",
        "TC": "Turks and Caicos Islands",
        "TV": "Tuvalu",
        "UG": "Uganda",
        "UA": "Ukraine",
        "AE": "United Arab Emirates",
        "GB": "United Kingdom",
        "US": "United States",
        "UM": "United States Minor Outlying Islands",
        "UY": "Uruguay",
        "UZ": "Uzbekistan",
        "VU": "Vanuatu",
        "VE": "Venezuela, Bolivarian Republic of",
        "VN": "Viet Nam",
        "VG": "Virgin Islands, British",
        "VI": "Virgin Islands, U.S.",
        "WF": "Wallis and Futuna",
        "EH": "Western Sahara",
        "YE": "Yemen",
        "ZM": "Zambia",
        "ZW": "Zimbabwe"
    }


def get_team_members():
    return [
        {'name': "Mohammed Rafiqul Islam", 'designation': mark_safe("<b>Chairman</b>"),
         'img': '/assets/img/team/boss.jpeg',
         'bio': mark_safe(
             "<b>Mohammed Rafiqul Islam</b> started his journey as a broker in Khatungonj, "
             "Chittagong. Later on he joined Abul Khair Group and gathered many knowledges about Industry "
             "handling, Import – Export, Trading and many more. He started his own Import – Export firm "
             "named"
             "as RR Trading Corporation in 1980. After that he saw many problems in the bunkering "
             "Industry of"
             "Bangladesh then he saw the opportunity to bring a better solution to the Industry then Sea "
             "marine fuel suppliers & Co was established in 1990. Later He established Bricks manufacturing "
             "company in 2008 and Real estate company named RR RAINBOW BD HOLDINGS LTD in 2021.")},
        {
            'name': "Mohammed Amanur Rashid", 'designation': mark_safe("<b>Managing partner</b>"),
            'img': "/assets/img/team/amanur.jpeg",
            'bio': mark_safe(
                "<b>Md. Amanur Rashid</b> is a Marine Engineer by profession, before joining with us "
                "he served in American Bureau of Shipping (ABS), Singapore as Marine Surveyor. He was assigned in "
                "new building construction and successfully delivered three container ships and two offshore supply"
                " vessels as new construction surveyor. His career at a glance: After passing out from Marine "
                "Academy, Chittagong, Bangladesh in 1991 he joined Neptune Ship management services, Singapore "
                "as Assistant Engineer. He joined Anglo Eastern Ship management UK as a Second Engineer in 1998 "
                "and was promoted to the rank of Chief Engineer in 2003. He has enormous experience in Chemical"
                " Tanker, Crude Oil Tanker, Product Tanker and Bulk Carrier.Joined in Ocean Tankers Pte Ltd, "
                "Singapore, as Technical Superintendent in 2004. He also served DNV Petroleum Services Singapore,"
                " as Technical Advisor\n")},
        {'name': "Mohammed Rezaul Islam ", 'designation': mark_safe("<b>Managing director</b>"),
         'img': "/assets/img/team/rezaul.jpeg",
         'bio': mark_safe(
             "<b>Mohammed Rezaul Islam</b> is a managing director of RR RAINBOW BD HOLDINGS LTD. He completed his "
             "High School from the BAF SHAHEEN COLLEGE CHATTOGRAM in 2018. He later went on to complete his "
             "undergraduate from the Independent University Bangladesh, in Bachelor of Business Administration ("
             "Hons) with a major in Accounting and Finance. He is a big believer in technological innovation-led "
             "development to increase efficiency within the work environment and the fostering of overall "
             "organizational growth.")},
    ]


def send_inquiry_email(data) -> dict:
    return {
        'company_name': data.get('company_name', ''),
        'contact_person': data.get('contact_person', ''),
        'telephone': data.get('telephone', ''),
        'email': data.get('email', ''),
        'select_value_1': data.get('select_value_1', ''),
        'select_value_2': data.get('select_value_2', ''),
        'quantity': data.get('quantity', ''),
        'vessel_name': data.get('vessel_name', ''),
        'port': data.get('port', ''),
        'birth_loc': data.get('birth_loc', ''),
        'eda': data.get('eda', ''),
        'eta': data.get('eta', ''),
        'etd': data.get('etd', ''),
        'agent': data.get('agent', ''),
        'message': data.get('message', '')
    }


def get_sister_concern():
    sister_concerns = [
        {
            "name": "RR RAINBOW BD",
            "detail": "Founded in 2022, RR RAINBOW BD has emerged as a trailblazer in the realms of residential, commercial, shopping mall development, and land subdivision projects. The company, now headquartered in Chittagong, has achieved rapid growth and recognition thanks to its pioneering spirit, innovative practices, and unwavering commitment to sustainable real estate development. RR RAINBOW BD is a world-class company, fully committed to making life better. Through strategic collaborations with renowned professionals spanning diverse fields of expertise and a dedicated and passionate team, RR RAINBOW BD consistently ensures the timely and successful completion of its projects.",
            "icon": '<i class="bx bx-building-house"></i>'
        },
        {
            "name": "RR TRADING CORPORATION",
            "detail": "RR TRADING CORPORATION is a sister concern of Sea Marine Fuel Supplier & Co and was established in 1992. Excellence is its motto. It has acquired wide experience in the Export-Import Business. Through this company, RR TRADING CORPORATION imports materials from various origins such as Stone Chips & Aggregates, Chemicals, Coal, Fruits, Paper, Food & Beverages, and other trading goods & commodities from sources outside of this country. RRTC is involved in business as an exporter, franchisee, clearing & forwarding agent, and supplier of various goods including finished and semi-finished goods of RRTC concerns to different parts of the world. RRTC is committed to providing quality products and services.",
            "icon": '<i class="bx bx-briefcase"></i>'
        },
        {
            "name": "BARODHONA BRICKS MANUFACTURING (BBM)",
            "detail": "BARODHONA BRICKS MANUFACTURING, based in Sathkania, is equipped with efficient semi-automatic machinery and strong manpower. The experienced team, with its professional production area, has the capacity to manufacture up to 10,000 bricks per day. The product portfolio includes bricks in standard sizes for successful construction projects.",
            "icon": '<i class="bx bx-building"></i>'
        },
        {
            "name": "SEA TRADE INTERNATIONAL",
            "detail": "SEA TRADE INTERNATIONAL shares the same business approach and commitment as Sea Marine Fuel Supplier & Co, being involved in similar maritime and fuel supply businesses.",
            "icon": '<i class="bx bx-anchor"></i>'
        }
    ]
    return sister_concerns

