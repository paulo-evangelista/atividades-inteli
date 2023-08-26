"use client";

import axios from "axios";
import { useEffect, useState } from "react";
import Card from "@/components/Cards";
import Cookies from "js-cookie";
import { useRouter } from "next/navigation";
export default function Home() {
  const router = useRouter();
  const [data, setData] = useState([]);
  const [modalState, setModalState] = useState(false);
  const [addPokemonInput, setAddPokemonInput] = useState("");

  const handleAddPokemon = () => {
    const authCookie = Cookies.get("Auth");
    const userIdCookie = Cookies.get("userId");
    axios.defaults.headers.common["Authorization"] = `Bearer ${authCookie}`;
    axios.put("http://localhost:4000/client/addPokemon", {userId: userIdCookie, pokemon: addPokemonInput})
    .then(res => {
      return res.data
    })
    .then(res => {
      if (res.status) return
      const newData = [...data, res]
          newData.sort(function(a, b) {
      let aa = parseInt(a.number);
      let bb = parseInt(b.number);
      return aa-bb
      })
      setData(newData)
    })
    .catch(e => {
      console.log(e)
    })
  }

  const handleLogOut = () => {
    Cookies.remove("Auth")
    Cookies.remove("userId")
    router.replace("/login")
  }
  //FETCH ALL POKEMONS
  useEffect(() => {
    const authCookie = Cookies.get("Auth");
    const userIdCookie = Cookies.get("userId");
    axios.defaults.headers.common["Authorization"] = `Bearer ${authCookie}`;
    axios
      .post("http://localhost:4000/client/getPokemons", {
        userId: userIdCookie,
      })
      .then((res) => {
        return res.data;
      })
      .then((res) => {
        console.log(res)
        setData(res);
      })
      .catch((e) => {
        router.replace("/login");
      });
  }, []);

  return (
    <main>
      <>
        <div className="h-20 content-center grid grid-cols-2 text-center text-white shadow-xl bg-red-500 text-xl font-bold w-full">
          <h1 className="p-4">
            {" "}
            <span className="text-4xl"> POKEDEX </span> by PokeChain
          </h1>
          <div className="flex justify-between">
            <button
              onClick={() => {
                setModalState(!modalState);
                console.log(modalState);
              }}
              className="bg-blue-600 hover:bg-blue-700 hover:scale-110 rounded-xl p-4 my-1 transition-all px-6 ml-2 text-white font-medium "
            >
              Add new Pokemon
            </button>
              <button className="mr-4 hover:scale-110 transition-all" onClick={handleLogOut}>LOGOUT</button>
          </div>
        </div>
        <div className="flex flex-wrap justify-center">
          {data.map((pokemon, i) => (
            <Card
            key={i}
              name={pokemon.species}
              types={pokemon.type}
              number={pokemon.number}
              url={pokemon.imgURL}
              nickname={pokemon.nickname}
              id={pokemon.id}
            />
          ))}
        </div>
        {modalState && (
          <div className="absolute p-8 top-20 mt-2 content-center justify-center text-center right-[20vw] bg-white rounded-lg shadow-lg">
            <p className="text-xl font-semibold">Got a new Pokemon? Amazing!</p>
            <p className="text-gray-600 my-2">Insert it's name or dex number</p>
            <input
              className="w-40 p-2 px-4 border focus:outline-none focus:border-2 focus:ring-blue-600 border-blue-600 rounded mx-auto"
              value={addPokemonInput}
              onChange={(e) => setAddPokemonInput(e.target.value)}
            ></input>
            <button
              className="bg-blue-600 border z-10 border-blue-600 hover:bg-blue-700 hover:scale-110 rounded p-2 mt-1 transition-all px-3 ml-2 text-white font-medium mb-4"
              onClick={handleAddPokemon}
            >
              Add
            </button>
          </div>
        )}
      </>
    </main>
  );
}
