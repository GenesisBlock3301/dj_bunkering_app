from typing import List


def footer_items_context(request):
    our_sectors_footer, menu_items = get_footer_items()
    return {'our_sectors_footer': our_sectors_footer, 'menu_items': menu_items}


def get_footer_items() -> tuple[List, List[dict]]:
    our_sectors = ["Physical Bunker Supply", "Lubricant Supply", "Exporter & Importer", "Ship Chandelling",
                   "Provision & Repair",
                   "Oil Carrying", "Real estate", "Bricks Manufacturing",
                   ]
    menu_items = [
        {"path": "/", "name": "Home"}, {"path": "/bunker", "name": "Bunkering"},
        {"path": "/team", "name": "Team"}, {"path": "/fleet", "name": "Fleet"},
        {"path": "/career", "name": "Career"}, {"path": "/quote", "name": "Request A Quote"},
        {"path": "/contact", "name": "Contact"}, {"path": "/terms", "name": "Terms & Conditions"}
    ]
    return our_sectors, menu_items
