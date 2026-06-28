const { saveProductToDb, connect, getProductsFromDb } = require('../../../../src/modules/products/dao');
const { createMongoContainer, closeConnection } = require('../../../environment/setup');
const _ = require('lodash');
const { describe, it, expect, afterAll, beforeAll } = require('@jest/globals');

let container;

jest.setTimeout(1000000);

beforeAll(async () => {
  try {
    const env = await createMongoContainer();
    container = env.container;
    process.env.DB_URL = env.mongoUrl;
    await connect();
    await saveProductToDb({ name: 'dummy product 1' });
    await saveProductToDb({ name: 'dummy product 2' });
    await saveProductToDb({ name: 'dummy product 3' });
  } catch (err) {
    console.log('Error: ', err);
    throw err;
  }
});

describe('product dao - unit tests', () => {
  it('should fetch products', async () => {
    let productsFromDb = await getProductsFromDb();
    expect(productsFromDb).toBeDefined();
    expect(_.isArray(productsFromDb.products)).toBeTruthy();
    expect(productsFromDb.products.length).toEqual(3);
  });
  it('should save a product to db', async () => {
    let payload = {
      name: 'dummy product'
    }
    let savedProduct = await saveProductToDb(payload);
    expect(savedProduct.data).toBeDefined();
    expect(_.has(savedProduct.data, 'acknowledged')).toBeTruthy();
    let productsFromDb = await getProductsFromDb();
    expect(productsFromDb.products.length).toEqual(4);
  });
});

afterAll(async () => {
  await closeConnection(container);
});
