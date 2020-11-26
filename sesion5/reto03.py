# 1. Usando la colección sample_airbnb.listingsAndReviews, 
# mediante el uso de agregaciones, encontrar el número de publicaciones 
# que tienen conexión a Internet, sea desde Wifi o desde cable (Ethernet).

client = MongoClient('mongodb+srv://BeduUser:12345@cluster1ds.sfgzw.mongodb.net/test?authSource=admin&replicaSet=atlas-e1gcf8-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
result = client['sample_airbnb']['listingsAndReviews'].aggregate([
    {
        '$match': {
            'amenities': {
                '$in': [
                    'Wifi', 'Ethernet', 'Internet'
                ]
            }
        }
    }, {
        '$count': 'Opciones con Internet'
    }
])
