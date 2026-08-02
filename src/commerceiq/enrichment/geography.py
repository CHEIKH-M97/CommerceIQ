GOVERNORATE_MAP = {

    # North
    "tunis": {
        "zone": "North",
        "type": "Coastal",
    },
    "ariana": {
        "zone": "North",
        "type": "Coastal",
    },
    "ben arous": {
        "zone": "North",
        "type": "Coastal",
    },
    "manouba": {
        "zone": "North",
        "type": "Interior",
    },
    "bizerte": {
        "zone": "North",
        "type": "Coastal",
    },
    "beja": {
        "zone": "North",
        "type": "Interior",
    },
    "jendouba": {
        "zone": "North",
        "type": "Interior",
    },
    "le kef": {
        "zone": "North",
        "type": "Interior",
    },
    "siliana": {
        "zone": "North",
        "type": "Interior",
    },


    # Center
    "sousse": {
        "zone": "Center",
        "type": "Coastal",
    },
    "monastir": {
        "zone": "Center",
        "type": "Coastal",
    },
    "mahdia": {
        "zone": "Center",
        "type": "Coastal",
    },
    "sfax": {
        "zone": "Center",
        "type": "Coastal",
    },
    "kairouan": {
        "zone": "Center",
        "type": "Interior",
    },
    "kasserine": {
        "zone": "Center",
        "type": "Interior",
    },
    "zaghouan": {
        "zone": "Center",
        "type": "Interior",
    },


    # South
    "gabes": {
        "zone": "South",
        "type": "Coastal",
    },
    "medenine": {
        "zone": "South",
        "type": "Coastal",
    },
    "tataouine": {
        "zone": "South",
        "type": "Interior",
    },
    "gafsa": {
        "zone": "South",
        "type": "Interior",
    },
    "tozeur": {
        "zone": "South",
        "type": "Interior",
    },
    "kebili": {
        "zone": "South",
        "type": "Interior",
    },
}
def get_geography(governorate: str) -> dict:

    return GOVERNORATE_MAP.get(
        governorate,
        {
            "zone": "Unknown",
            "type": "Unknown",
        }
    )