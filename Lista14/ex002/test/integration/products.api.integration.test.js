const request = require('supertest');
const app = require('../../src/app');
const _ = require('lodash');
const { connect, saveProductToDb } = require('../../src/modules/products/dao');
const { createMongoContainer, closeConnection } = require('../environment/setup');
const { describe, it, expect, afterAll, beforeAll } = require('@jest/globals');
const { mockProductsArray, mockProductObject } = require("../mocks/products");

let container;

jest.setTimeout(1000000);

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

describe('product API integration tests', () => {
  it('GET /products - should fetch products',  async () => {
    return await request(app).get('/products')
      .then(res => {
        expect(res.body.products).toBeDefined();
        expect(_.isArray(res.body.products)).toBeTruthy();
        expect(res.body.products.length).toEqual(3);
        expect(res.statusCode).toEqual(200)
      });
  });
  it('POST /products - should create a product', async () => {
    const res = await request(app).post('/products').send(mockProductObject)
    expect(res.body.data).toBeDefined();
    expect(res.body.data.name).toEqual(mockProductObject.name);
    expect(res.statusCode).toEqual(201)
    expect(res.body.result).toBeDefined();
    expect(res.body.result.acknowledged).toBeTruthy();
  });
});

afterAll(async () => {
  await closeConnection(container);
});
