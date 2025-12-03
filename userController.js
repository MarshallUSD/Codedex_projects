import pool from "../connection.js";


export const getAllUsers = async (req,res) =>{
    try{
        const result = await pool.query("SELECT * FROM users");
        res.status(200).json(result.rows);
    }catch(err){
        res.status(500).json({error: err.message});
    }
};

export const getSingleUser = async (req,res) => {
    try{
        const {id} = req.params;
        const result = await pool.query("SELECT * FROM users WHERE id = $1",[id]);
        res.status(200).json(result.rows[0]);
    }catch(err){
        res.status(500).json({error: err.message});
    }
};

export const createUser = async (req,res) =>{
    try{
        const {email,password,name,role,avatar} = req.body;
        const result = await pool.query("INSERT INTO Users (email,password,name,role,avatar) VALUES ($1,$2,$3,$4,$5) RETURNING *",
        [email,password,name,role,avatar]);
        res.status(201).json({message: "New user created", data: result.rows[0]});
    } catch(err){
        res.status(500).json({error: err.message});
    }
};

export const updateUser = async (req,res) =>{
    try{
        const {id} = req.params;
        const {email,password,name,role,avatar} = req.body;
        const result = await pool.query(
            "UPDATE users SET email=$1, password=$2, name=$3, role=$4, avatar=$5 WHERE id=$6 RETURNING *",
            [email,password,name,role,avatar,id]
        );
        res.status(201).json({message: "User updated", data: result.rows[0]});
    }catch(err){
        res.status(500).json({error: err.message});
    }
};

export const deleteUser = async (req,res) =>{
    try{
        const {id} = req.params;
        const result = await pool.query("DELETE FROM Users WHERE id=$1 RETURNING *",[id]);
        res.status(200).json({message: "User deleted", data: result.rows[0]});
    }catch(err){
        res.status(500).json({error: err.message});
    }
};

