import express from "express";
const app = express();

import productRoute from "./routes/productRoute.js";
import categoryRoute from "./routes/categoryRoute.js";
import userRoute from "./routes/userRoute.js";

// Middleware
app.use(express.json());

// APIs
app.use("/products", productRoute);
app.use("/categories", categoryRoute);
app.use("/users", userRoute);

const PORT = 7777;
app.listen(PORT, () => {
  console.log(`Girgittonimiz ${PORT}-portida xizmatingizga muntazir (Server is running on port ${PORT})`);
});