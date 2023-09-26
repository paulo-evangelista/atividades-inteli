"use client";
import { useState } from "react";
export default function Login() {
  const [user, setUser] = useState("");
  const [password, setPassword] = useState("");
  return (
    <main>
      <div className="flex p-32 w-full h-screen">
        <div className="p-4 content-center mx-auto bg-blue-500 text-white w-96 h-96 rounded">
          <h1 className="font-semibold text-6xl">Bem vindo</h1>
          <br />
          <label htmlFor="user">username</label>
          <br />
          <input
          className="text-black px-2"
            type="text"
            name="user"
            id="user"
            onChange={(e) => {
              setUser(e.target.value);
            }}
            value={user}
          />
          <br />
          <label htmlFor="password">password</label>
          <br />
          <input
                    className="text-black px-2"

            type="password"
            name="password"
            id="password"
            onChange={(e) => {
              setPassword(e.target.value);
            }}
            value={password}
          />
          <br />
          <button className="bg-blue-700  rounded px-8 py-4 transition hover:scale-110 mt-12 font-semibold">
            Log In
          </button>
        </div>
      </div>
    </main>
  );
}
