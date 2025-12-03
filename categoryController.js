import pool from "../conection.js";

export const getAllCategories = async (req,res)=>{
    try{
        const result = await pool.quesry("SELECT  FROM categories");
        res.status(200).json(result.rows);
    }catch(err){
        res.status(500).json({error}, err.message);

    }
};

export const getSingleCategory = async (req,res)=>{
    const {id} = req.params;
    try{
        const result = await pool.query("SELECT * FROM categories WHERE id = $1",[id]);
        res.status(200).json(result.rows[0]);

    }catch(err){
        res.status(500).json({error: err.message});
    }
};

export const createCategory = async (req,res)=>{
    try{
    const {name,image} = req.body;
    const result = await pool.query("INSERT INTO categories (name,image ) VALUES ($1,$2) RETURNING *",[name,image])
    res.status(201).json(result.rows[0]);

    }catch(err){
        res.status(500).json({error: err.message});
    }
};

export const updateCategory = async (req,res)=>{
    const {id}= req.params;
    const {name,image} = req.body;
    try{
        const result = await pool.query("UPDATE categories SET name=$1, image=$2 WHERE id =$3 RETURNING *",[name,image,id]);
        res
          .status(201)
          .json({message: "Updated successfully", data: result.rows[0] });
    }catch(err){
        res.status(500).json({error: err.message});
    }
};

export const deleteCategory = async (req,res)=>{
    try{
    const {id} = req.params;
    const result = await pool.query(
        "DELETE FROM categories WHERE id = $1 RETURNING *", [id]
    );
    res.status(200).json({message: "Deleted successfully", data: result.rows[0]});
    }
    catch(err){
        res.status(500).json({error: err.message});
    }
};
