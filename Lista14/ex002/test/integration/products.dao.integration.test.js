const { beforeAll, afterAll, describe, it, expect} = require('@jest/globals');
const { createMongoContainer, closeConnection } = require('../environment/setup');
const { connect, saveProductToDb, getProductsFromDb } = require('../../src/modules/products/dao');
const { mockProductsArray, mockProductObject, mockProduct} = require('../mocks/products');

jest.setTimeout(1000000);

let container;

beforeAll(async () => {
  try {
    const env = await createMongoContainer();
    container = env.container;
    process.env.DB_URL = env.mongoUrl;
    await connect();
    for (const product of mockProductsArray) {
      await saveProductToDb(product);
    }
  } catch (err) {
    console.log('Error: ', err);
    throw err;
  }
});

describe('products dao integration tests', () => {
  it('should return products saved in DB', async () => {
    const result = await getProductsFromDb();
    expect(result).toBeDefined();
    expect(result.products.length).toEqual(mockProductsArray.length);
  });
  it('should save product to DB', async () => {
    const savedProduct = await saveProductToDb(mockProduct);
    const productsList = await getProductsFromDb();
    expect(savedProduct).toBeDefined();
    expect(savedProduct.data.name).toEqual(mockProduct.name);
    expect(savedProduct.result.acknowledged).toBeTruthy();
    expect(productsList).toBeDefined();
    expect(productsList.products.length).toEqual(mockProductsArray.length + 1);
  });
});

afterAll(async () => {
  await closeConnection(container);
});
