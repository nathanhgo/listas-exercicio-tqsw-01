const express = require('express');
const cors = require('cors');
const productRouter = require('./modules/products/routes');

const StatusCodes = {
  INTERNAL_SERVER_ERROR: 500
};

const app = express();
app.use(cors());
app.use(express.json());

// Routes
app.use('/', productRouter);

// Error handling middleware
const errorHandler = () => {
  return (err, req, res, next) => {
    return res
      .status(err.statusCode || StatusCodes.INTERNAL_SERVER_ERROR)
      .json({
        message: err.message,
        statusCode: err.statusCode || StatusCodes.INTERNAL_SERVER_ERROR
      });
  };
};

app.use(errorHandler());

module.exports = app;
