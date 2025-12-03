import pool from '../conection.js';


export const getAllProducts = async (req,res)=>{
    try{
        const result = await pool.query("SELECT * FROM products");
        res.status(200).json(result.rows);
    }catch(err){
        res.status(500).json({error}, err.message);
    }
};

export const getSingleProduct = async (req,res)=>{
    try{
    const {id} = req.params;
    const result = await pool.query("SELECT * FROM products WHERE id = $1",[id]);
    res.status(200).json(result.rows[0]);
    }catch(err){
        res.status(500).json({errror: err.message});

    }
};

export const createProduct = async (req,res)=>{
    try{
        const {name,price,category_id,image} = req.body;
        const result = await pool.query("INSERT INTO products (name,price,category_id,image) VALUES ($1,$2,$3,$4) RETURNING *",
            [name,price,category_id,image]);
        res.status(201).json({ message: "New product added",obj: result.rows[0]});

    }catch(err){
        res.status(500).json({error: err.message});
    }
};

export const updateProduct = async (req, res)=>{
    try{
    const {id} = req.params;
    const {name,price,category_id,image} = req.body;
    const result =
    await pool.query("UPDATE products SET name=$1, price=$2, category_id=$3, image=$4 WHERE id=$5 RETURNING *",
    [name,price,category_id,image,id]);
    res.status(201).json({message: "Product updated", data: result.rows[0]});
    }catch(err){
        res.status(500).json({error: err.message});
    }
  };

export const deleteProduct = async (req,res)=>{
    try{
    const {id} = req.params;
    const result = await pool.query("DELETE FROM products WHERE id=$1 RETURNING *",[id]);
    res.status(200).json({message: "Product deleted", data: result.rows[0]});
    }catch(err){
        res.status(500).json({error: err.message});
    }
};