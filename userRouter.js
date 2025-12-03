import express from "express";
import {
    getAllUsers,
    getSingleUser,
    createUser,
    updateUser,
    deleteUser
} from "../controllers/userController.js";
const userRouter = express.Router();

userRouter.get("/", getAllUsers);
userRouter.get("/:id", getSingleUser);
userRouter.post("/", createUser);
userRouter.put("/:id", updateUser);
userRouter.delete("/:id", deleteUser);

export default userRouter;