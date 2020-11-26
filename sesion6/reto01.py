# Con base en el ejemplo 1, modifica el agrupamiento para que muestre el costo promedio
# por habitación por país de las propiedades de tipo casa.


client = MongoClient('mongodb+srv://BeduUser:12345@cluster1ds.sfgzw.mongodb.net/test?authSource=admin&replicaSet=atlas-e1gcf8-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
result = client['sample_airbnb']['listingsAndReviews'].aggregate([
    {
        '$match': {
            'property_type': 'House', 
            'bedrooms': {
                '$gte': 1
            }
        }
    }, {
        '$addFields': {
            'costo_recamara': {
                '$divide': [
                    '$price', '$bedrooms'
                ]
            }
        }
    }, {
        '$group': {
            '_id': '$address.country', 
            'recamaras': {
                '$sum': 1
            }, 
            'total': {
                '$sum': '$costo_recamara'
            }
        }
    }, {
        '$addFields': {
            'pais': '$_id', 
            'costo_promedio': {
                '$divide': [
                    '$total', '$recamaras'
                ]
            }
        }
    }, {
        '$project': {
            '_id': 0, 
            'pais': 1, 
            'costo_promedio': 1
        }
    }
])
