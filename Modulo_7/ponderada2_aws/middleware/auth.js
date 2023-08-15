const auth = function (req, res, next) {
  console.log("incoming header->" + req.headers.authorization);
  if (
    req.headers.authorization !==
    process.env.BEARER
  ) {
    console.log("wrong header");
    res.status(401).send("Unauthorized");
    res.end();
    return;
  } else {
    console.log("header accepted")
    next();
  }
};

module.exports = auth;
