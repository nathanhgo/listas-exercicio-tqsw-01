const { describe, it, expect, afterAll } = require('@jest/globals');
const { mockProductsArray, mockProductObject } = require("../../../mocks/products");

jest.mock('../../../../src/modules/products/dao');

const productDao = require('../../../../src/modules/products/dao');
const productService = require('../../../../src/modules/products/service');

const mockGetProductsFromDb = jest.spyOn(productDao, 'getProductsFromDb')
const mockCreateProductInDb = jest.spyOn(productDao, 'saveProductToDb')

describe('product service - unit tests', () => {
  it('should return products', async () => {
    const mockProductList = jest.fn(async () => {
      return { products: mockProductsArray };
    });
    mockGetProductsFromDb.mockImplementation(mockProductList);
    const response = await productService.getProductsList();
    expect(mockGetProductsFromDb).toHaveBeenCalledTimes(1);
    expect(response.products).toBeDefined();
    expect(response.products.length).toEqual(3);
  });
  it('should create a product', async () => {
    const mockProduct = jest.fn(async () => {
      return {
        data: {
          acknowledged: true,
          insertedId: '63de5b5604e5b6c3284ce52c'
        }
      };
    });
    mockCreateProductInDb.mockImplementation(mockProduct);
    const response = await productService.saveProduct(mockProductObject);
    expect(mockCreateProductInDb).toHaveBeenCalledTimes(1);
    expect(response.data).toBeDefined();
    expect(response.data.acknowledged).toBeTruthy();
  });
});

afterAll(() => {
  jest.clearAllMocks();
});
