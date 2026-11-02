from mcp.server import MCPServer
from cafe_data import MENU,COUPONS
from pydantic import BaseModel

mcp = MCPServer("Charminar Cafe",
                instructions = "Order food from Charminar Cafe in Hyderabad: read the menu, place orders, apply coupons, track delivery.")


ORDERS : dict[str,dict] = {}

@mcp.resource("cafe://menu")
def menu_card()->str:
    """
    The full charminar cafe menu card with prices, veg/non-veg and spice level
    """
    lines = ["CHARMINAR CAFE MENU:"]
    for name,item in MENU.items():
        tag = 'veg' if item["veg"] else 'non-veg'
        spice = f"spice {item['spicy']/4}" if item['spicy'] else "mild"
        