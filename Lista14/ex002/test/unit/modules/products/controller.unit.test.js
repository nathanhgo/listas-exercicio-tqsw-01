const httpMocks = require('node-mocks-http');
const { describe, it, expect, afterAll } = require('@jest/globals');
const { mockProductObject, mockProductsArray } = require("../../../mocks/products");

jest.mock('../../../../src/modules/products/service');

const productService = require('../../../../src/modules/products/service');
const productController = require('../../../../src/modules/products/controller');

const mockSaveProduct = jest.spyOn(productService, 'saveProduct')
const mockFetchProduct = jest.spyOn(productService, 'getProductsList')

describe('product controller - unit tests', () => {
  it('should get products list', async () => {
    // mock
    const response = httpMocks.createResponse();
    const request = httpMocks.createRequest();
    const mockProductList = jest.fn(async () => {
      return { products: mockProductsArray };
    });
    mockFetchProduct.mockImplementation(mockProductList);
    await productController.getProducts(request, response);
    expect(mockFetchProduct).toHaveBeenCalledTimes(1);
    expect(response.statusCode).toEqual(200);
    expect(response._isEndCalled()).toBeTruthy();
    expect(response._getJSONData().products.length).toEqual(3);
  });
  it('should create a product', async () => {
    const response = httpMocks.createResponse();
    const request = httpMocks.createRequest();
    request.body = {
      name: 'dummy 1',
      price: 10
    };
    const mockProduct = jest.fn(async () => {
      return { data: mockProductObject };
    });
    mockSaveProduct.mockImplementation(mockProduct);
    await productController.createProduct(request, response);
    expect(mockSaveProduct).toHaveBeenCalledTimes(1);
    expect(mockSaveProduct).toHaveBeenCalledWith(mockProductObject);
    expect(response.statusCode).toEqual(201);
    expect(response._isEndCalled()).toBeTruthy();
    expect(response._getJSONData().data.name).toEqual('dummy 1');
  });
});

afterAll(() => {
  jest.clearAllMocks();
});
