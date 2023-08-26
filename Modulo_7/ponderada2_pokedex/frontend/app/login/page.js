"use client";
import axios from "axios";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Cookies from "js-cookie";

const Login = () => {
  const router = useRouter();
  const [loginUser, setLoginUser] = useState("");
  const [loginPass, setLoginPass] = useState("");
  const [SignupUser, setSignupUser] = useState("");
  const [SignupPass, setSignupPass] = useState("");

  const handleLogin = async () => {
    axios.defaults.withCredentials = true;
    axios.defaults.headers.post["Content-Type"] =
      "application/json;charset=utf-8";
    console.log(loginUser, loginPass);
    const res = await axios
      .post("http://localhost:4000/auth/login", {
        username: loginUser,
        password: loginPass,
      })
      .then((res) => {
        return res.data;
      })
      .then((data) => {
        Cookies.set("Auth", data.access_token);
        Cookies.set("userId", data.userId);
        router.push("/");
      })
      .catch((e) => {
       console.log("oops! user or password incorrect")
      });
  };
  const handleSignup = async () => {
    console.log(SignupUser, SignupPass)
    axios.defaults.withCredentials = true;
    axios.defaults.headers.post["Content-Type"] ="application/json;charset=utf-8";
    const res = await axios
      .post("http://localhost:4000/client/signin", {
        username: SignupUser,
        password: SignupPass,
      })
      .then((res) => {
        res.data;
      })
      .then(() => {
        alert("Account created. You can log in!");
      })
      .catch((e) => {
        alert("oops! are you sure this username is not taken?");
      });
  };
  return (
    <main className="ml-10">
      <h1 className="mt-8 text-4xl font-bold">Log In</h1>
      <p>username</p>
      <input
        className="w-56 mb-1 p-2 px-4 border focus:outline-none focus:border-2 focus:ring-blue-600 border-blue-600 rounded mx-auto"
        type="text"
        value={loginUser}
        onChange={(e) => setLoginUser(e.target.value)}
      ></input>
      <p>password</p>
      <input
        className="w-40 mb-1 p-2 px-4 border focus:outline-none focus:border-2 focus:ring-blue-600 border-blue-600 rounded mx-auto"
        type="password"
        value={loginPass}
        onChange={(e) => setLoginPass(e.target.value)}
      ></input>
      <button
        className="bg-blue-500 rounded-lg px-6 hover:scale-110 hover:bg-blue-600 transition-all p-2 text-white ml-4"
        onClick={handleLogin}
      >
        Go!
      </button>
      <h1 className="mt-16 font-bold text-4xl">Sign Up</h1>
      <p>username</p>
      <input
        className="w-56 mb-1 p-2 px-4 border focus:outline-none focus:border-2 focus:ring-blue-600 border-blue-600 rounded mx-auto"
        type="text"
        value={SignupUser}
        onChange={(e) => setSignupUser(e.target.value)}
      ></input>
      <p>password</p>
      <input
        className="w-40 mb-1 p-2 px-4 border focus:outline-none focus:border-2 focus:ring-blue-600 border-blue-600 rounded mx-auto"
        type="password"
        value={SignupPass}
        onChange={(e) => setSignupPass(e.target.value)}
      ></input>
      <button
        className="bg-blue-500 rounded-lg px-6 hover:scale-110 hover:bg-blue-600 transition-all p-2 text-white ml-4"
        onClick={handleSignup}
      >
        Go!
      </button>
    </main>
  );
};

export default Login;
