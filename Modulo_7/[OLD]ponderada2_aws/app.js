const express = require("express");
const CORS = require("cors");
const auth = require("./middleware/auth");
const bp = require("body-parser");
const app = express();
const dotenv = require("dotenv");

const PrismaClient = require("@prisma/client").PrismaClient;
const prisma = new PrismaClient();
dotenv.config();

app.use(bp.json());
app.use(bp.urlencoded({ extended: true }));
app.use(CORS());

app.put("/create", auth, async (req, res) => {
  try {
    result = await prisma.cat.create({
      data: {
        name: req.body.name,
        age: req.body.age,
        kind: req.body.kind,
      },
    });
    res.status(200).send("ok");
  } catch (e) {
    res.status(500).send(e);
  }
});

app.get("/read", auth, async (req, res) => {
  const cats = await prisma.cat.findMany();
  res.send(cats);
});

app.post("/update", auth, async (req, res) => {
  try {
    const newData = {};
    if (req.body.name) {
      newData.name = req.body.name;
    }
    if (req.body.age) {
      newData.age = req.body.age;
    }
    if (req.body.kind) {
      newData.kind = req.body.kind;
    }

    const cat = await prisma.cat.update({
      where: {
        id: req.body.id,
      },
      data: newData,
    });

    res.status(200).send("ok");
  } catch (e) {
    res.status(500).send(e);
  }
});

app.delete("/delete", auth, (req, res) => {
  try {
    prisma.cat.delete({
      where: {
        id: req.body.id,
      },
    });
    res.status(200).send("ok");
  } catch (e) {
    res.status(500).send(e);
  }
});

app.listen(3000, () => {
  console.log("Server started on http://0.0.0.0:3000");
});
