# 1. ¿Qué comentarios ha hecho Greg Powell?

client = MongoClient('mongodb+srv://BeduUser:12345@cluster1ds.sfgzw.mongodb.net/test?authSource=admin&replicaSet=atlas-e1gcf8-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    'name': 'Greg Powell'
}

result = client['sample_mflix']['comments'].find(
  filter=filter
)

# 2. ¿Qué comentarios han hecho Greg Powell o Mercedes Tyler?

client = MongoClient('mongodb+srv://BeduUser:12345@cluster1ds.sfgzw.mongodb.net/test?authSource=admin&replicaSet=atlas-e1gcf8-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    '$or': [
        {
            'name': 'Greg Powell'
        }, {
            'name': 'Mercedes Tyler'
        }
    ]
}

result = client['sample_mflix']['comments'].find(
  filter=filter
)

# 3. ¿Cuál es el máximo número de comentarios en una película?
client = MongoClient('mongodb+srv://BeduUser:12345@cluster1ds.sfgzw.mongodb.net/test?authSource=admin&replicaSet=atlas-e1gcf8-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'num_mflix_comments': 1
}
sort=list({
    'num_mflix_comments': -1
}.items())
limit=1

result = client['sample_mflix']['movies'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)

# 4. ¿Cuál es título de las cinco películas más comentadas?
# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://BeduUser:12345@cluster1ds.sfgzw.mongodb.net/test?authSource=admin&replicaSet=atlas-e1gcf8-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'title': 1
}
sort=list({
    'num_mflix_comments': -1
}.items())
limit=5

result = client['sample_mflix']['movies'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)
