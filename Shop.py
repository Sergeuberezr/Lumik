class Shop:
    old = [
        {
            'Cost': 20,
            'Amount': 150
        },

        {
            'Cost': 50,
            'Amount': 400
        },

        {
            'Cost': 140,
            'Amount': 1200
        }

    ]

    boxes = [
        {
            'Name': 'Big Box',
            'Cost': 30,
            'Multiplier': 1
        },

        {
            'Name': 'Mega Box',
            'Cost': 80,
            'Multiplier': 1
        }

    ]


    token_doubler = {

        'Cost': 50,
        'Amount': 1000
    }
    """
    << Shop Offers IDs List >>

    0 = Free Brawl Box
    1 = Gold
    2 = Random Brawler
    3 = Brawler
    4 = Skin
    5 = StarPower/ Gadget
    6 = Brawl Box
    7 = Tickets
    8 = Power Points (for a specific brawler)
    9 = Token Doubler
    10 = Mega Box
    11 = Keys (???)
    12 = Power Points
    13 = EventSlot (???)
    14 = Big Box
    15 = AdBox (not working anymore)
    16 = Gems
    """
    offers = [
      {
         "OfferID": 4,
         "DataReference": [16,0],
         "SkinID": 123,
         "ShopType": 0,
         "ShopDisplay": 0,
         "Cost": 1,
         "Timer": 120,
         "Multiplier": 1,
         "OfferText": "Поел",
         "Claimed": False,
         "OfferBG": 'offer_lny'
      },
      {
         "OfferID": 10,
         "DataReference": [16,0],
         "SkinID": 0,
         "ShopType": 0,
         "ShopDisplay": 1,
         "Cost": 10,
         "Timer": 120,
         "Multiplier": 1,
         "OfferText": "Гром студио геи",
         "Claimed": False,
         "OfferBG": 'offer_lny'
      },
      {
         "OfferID": 16,
         "DataReference": [16,0],
         "SkinID": 0,
         "ShopType": 0,
         "ShopDisplay": 0,
         "Cost": 1,
         "Timer": 120,
         "Multiplier": 100,
         "OfferText": "чочочочочочочочочочочо",
         "Claimed": False,
         "OfferBG": 'offer_lny'
      },
      {
         "OfferID": 1,
         "DataReference": [16,0],
         "SkinID": 0,
         "ShopType": 0,
         "ShopDisplay": 0,
         "Cost": 1,
         "Timer": 120,
         "Multiplier": 999,
         "OfferText": "Ебал ого",
         "Claimed": False,
         "OfferBG": 'offer_lny'
      },      
      {
         "OfferID": 21,
         "DataReference": [16,0],
         "SkinID": 0,
         "ShopType": 0,
         "ShopDisplay": 0,
         "Cost": 1,
         "Timer": 120,
         "Multiplier": 1,
         "OfferText": "С днем святого гея",
         "Claimed": False,
         "OfferBG": 'offer_lny'
      },
      {
         "OfferID": 3,
         "DataReference": [16,44],
         "SkinID": 0,
         "ShopType": 0,
         "ShopDisplay": 0,
         "Cost": 1,
         "Timer": 120,
         "Multiplier": 1,
         "OfferText": "Я люблю когда волосатые хеоны оьмазываются своим дерьмом",
         "Claimed": False,
         "OfferBG": 'offer_lny'
      },
    ]