const app = require('./app');
const { connect } = require('./modules/products/dao');

const PORT = process.env.PORT || 3000;

const startServer = async () => {
  try {
    await connect();
    app.listen(PORT, () => {
      console.log(`Server is running on port ${PORT}`);
    });
  } catch (err) {
    console.error('Failed to start server:', err);
    process.exit(1);
  }
};

startServer();
