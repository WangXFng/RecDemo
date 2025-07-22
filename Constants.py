DATASET = "Yelp2023"
ENCODER = 'hGCN'  # hGCN  Transformer  TransformerLS  gMLP
ABLATION = 'Full'  # Full  w/oImFe  w/oFeTra w/oGlobal w/oAtt w/oConv w/oGraIm

user_dict = {
    'Gowalla': 18737,
    'Yelp2023': 31668,
    'Foursquare': 7642,
}

poi_dict = {
    'Gowalla': 32510,
    'Yelp2023': 38048,
    'Foursquare': 28483
}

POI_NUMBER = poi_dict.get(DATASET)
USER_NUMBER = user_dict.get(DATASET)

print('Dataset:', DATASET, '#User:', USER_NUMBER, '#POI', POI_NUMBER)


PAD = 0

