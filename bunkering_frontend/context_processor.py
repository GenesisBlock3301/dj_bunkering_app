from typing import List
from django.conf import settings


def footer_items_context(request):
    our_sectors_footer, menu_items = get_footer_items()
    return {'our_sectors_footer': our_sectors_footer, 'menu_items': menu_items}


def get_footer_items() -> tuple[List, List[dict]]:
        ourSectors = ["Physical Bunker Supply", "Lubricant Supply", "Exporter & Importer", "Ship Chandelling",
                      "Provision & Repair",
                      "Oil Carrying", "Real estate", "Bricks Manufacturing",
                      ]
        menuItems = [
            {"path": "/", "name": "Home"}, {"path": "/bunker", "name": "Bunkering"},
            {"path": "/team", "name": "Team"}, {"path": "/fleet", "name": "Fleet"},
            {"path": "/career", "name": "Career"}, {"path": "/quote", "name": "Request A Quote"},
            {"path": "/contact", "name": "Contact"}, {"path": "/terms", "name": "Terms & Conditions"}
        ]
        return ourSectors, menuItems
