const { MongoClient } = require('mongodb');

let db;

const connect = async () => {
  const uri = process.env.DB_URL || `mongodb://localhost:27017`;
  const dbName = process.env.DB_NAME || `test`;
  const mongoClient = new MongoClient(uri);
  return new Promise((resolve) => {
    mongoClient.connect();
    db = mongoClient.db(dbName);
    resolve(db);
    console.info(`Successfully connected to the mongodb cluster: ${uri}/${dbName}`);
  });
};

const getDatabase = () => db;

const MongoCollections = {
  PRODUCTS: 'products'
};

const getProductsFromDb = async () => {
  const products = await db
    .collection(MongoCollections.PRODUCTS)
    .find({})
    .project({ _id: 0 })
    .toArray();
  return { products };
};

const saveProductToDb = async (data) => {
  const result = await db.collection(MongoCollections.PRODUCTS).insertOne(data);
  data.acknowledged = result.acknowledged;
  return { data, result };
};

module.exports = {
  connect,
  getDatabase,
  getProductsFromDb,
  saveProductToDb,
  MongoCollections
};
