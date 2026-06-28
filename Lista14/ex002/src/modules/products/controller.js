const _ = require('lodash');
const { getProductsList, saveProduct } = require('./service');

const StatusCodes = {
  BAD_REQUEST: 400,
  INTERNAL_SERVER_ERROR: 500
};

const getProducts = async (req, res) => {
  try {
    const result = await getProductsList();
    res.status(200).json(result);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

const createProduct = async (req, res, next) => {
  const params = req.body;
  if (_.isEmpty(params)) {
    const err = new Error('Request body is missing');
    err.statusCode = StatusCodes.BAD_REQUEST;
    res.status(400).json(err);
  } else {
    try {
      const result = await saveProduct(params);
      res.status(201).json(result);
    } catch (err) {
      next(err);
    }
  }
};

module.exports = {
  getProducts,
  createProduct
};
