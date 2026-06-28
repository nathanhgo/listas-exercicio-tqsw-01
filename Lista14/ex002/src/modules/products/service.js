const Joi = require('joi');
const { getProductsFromDb, saveProductToDb } = require('./dao');

const productSchema = Joi.object({
  name: Joi.string().required(),
  price: Joi.number().required()
});

const validateSchema = async (params, schema) => {
  return schema.validateAsync(params);
};

const getProductsList = async () => {
  try {
    return await getProductsFromDb();
  } catch (e) {
    throw e;
  }
};

const saveProduct = async (params) => {
  try {
    await validateSchema(params, productSchema);
    return await saveProductToDb(params);
  } catch (e) {
    throw e;
  }
};

module.exports = {
  getProductsList,
  saveProduct,
  productSchema,
  validateSchema
};
