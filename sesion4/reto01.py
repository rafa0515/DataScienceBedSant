# 1. Fecha, nombre y texto de cada comentario.

client = MongoClient('mongodb+srv://BeduUser:12345@cluster1ds.sfgzw.mongodb.net/test?authSource=admin&replicaSet=atlas-e1gcf8-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'date': 1, 
    'name': 1, 
    'text': 1
}

result = client['sample_mflix']['comments'].find(
  filter=filter,
  projection=project
)

# 2. Título, elenco y año de cada película.

client = MongoClient('mongodb+srv://BeduUser:12345@cluster1ds.sfgzw.mongodb.net/test?authSource=admin&replicaSet=atlas-e1gcf8-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'title': 1, 
    'cast': 1, 
    'year': 1
}

result = client['sample_mflix']['movies'].find(
  filter=filter,
  projection=project
)

# 3. Nombre y contraseña de cada usuario.

client = MongoClient('mongodb+srv://BeduUser:12345@cluster1ds.sfgzw.mongodb.net/test?authSource=admin&replicaSet=atlas-e1gcf8-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'name': 1, 
    'password': 1
}

result = client['sample_mflix']['users'].find(
  filter=filter,
  projection=project
)
