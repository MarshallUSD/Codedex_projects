import { Pool } from "pg";

const pool = new Pool({
  host: "localhost",
  port: 5432,
  user: "postgres",
  password: "1974",
  database: "postgres",
});

pool
  .connect()
  .then(()=>{
    console.log("Connected to the database successfully.");
  })
  .catch((err)=>{
    console.error("Database connection error:", err);
  });
  

export default pool;