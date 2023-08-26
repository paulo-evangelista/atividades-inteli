"use client";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import Image from "next/image";
import edit from "../assets/edit.svg";
import axios from "axios";

const typeColors = {
  normal: "bg-gray-300   p px-2 mb-2 mt-2 mx-2 rounded-full",
  fighting: "bg-red-700  p px-2 mb-2 mt-2 mx-2 rounded-full text-white",
  flying: "bg-blue-500 p px-2 mb-2 mt-2 mx-2 rounded-full",
  poison: "bg-purple-500 p px-2 mb-2 mt-2 mx-2 rounded-full text-white",
  ground: "bg-yellow-500 p px-2 mb-2 mt-2 mx-2 rounded-full text-white",
  rock: "bg-yellow-800 p px-2 text-white mb-2 mt-2 mx-2 rounded-full",
  bug: "bg-green-500 p px-2 mb-2 mt-2 mx-2 rounded-full",
  ghost: "bg-purple-500 p px-2 mb-2 mt-2 mx-2 rounded-full",
  steel: "bg-slate-300 p px-2 mb-2 mt-2 mx-2 rounded-full",
  fire: "bg-red-500 p px-2 mb-2 mt-2 mx-2 rounded-full text-white",
  water: "bg-blue-500 p px-2 mb-2 mt-2 mx-2 rounded-full text-white",
  grass: "bg-green-500 p px-2 mb-2 mt-2 mx-2 rounded-full",
  electric: "bg-yellow-300 p px-2 mb-2 mt-2 mx-2 rounded-full",
  psychic: "bg-purple-500 p px-2 mb-2 mt-2 mx-2 rounded-full text-white",
  ice: "bg-blue-300 p px-2 mb-2 mt-2 mx-2 rounded-full",
  dragon: "bg-cyan-200 p px-2 mb-2 mt-2 mx-2 rounded-full text-black",
  dark: "bg-stone-700 p px-2 mb-2 mt-2 mx-2 rounded-full text-white",
  fairy: "bg-pink-200 p px-2 mb-2 mt-2 mx-2 rounded-full",
};

const Card = ({ url, name, number, types, nickname, id }) => {
  const [settings, setSettings] = useState(false);
  const [newNickname, setNewNickname] = useState("");
  const [newNick, setNewNick] = useState(nickname);
  const [isHidden, setIsHidden] = useState(false);

  const toggleSetings = () => {
    console.log("hello");
    setSettings(!settings);
  };

  const handleDeletion = () => {
    console.log(id)
    axios
    .post("http://localhost:4000/client/deletePokemon", {
      pokemonId: id,
    })
    .then((res) => {
      setIsHidden(true)
    })
  };

  const handleSetNickname = () => {
    axios
      .post("http://localhost:4000/client/editNickname", {
        nickname: newNickname,
        pokemonId: id,
      })
      .then((res) => {
        setSettings(false);
        setNewNick(newNickname);
      })
      .catch((err) => {
        console.log(err);
      })
  };

  if (isHidden) return null
  return (
    <>

      {!settings ? (
        <div className=" w-64 shadow-lg  rounded-xl border-green-500 border-2 text-center m-4">
          <Image
            className="ml-2 mt-2 absolute hover:cursor-pointer hover:scale-150 transition-all"
            onClick={toggleSetings}
            src={edit}
            width={22}
          ></Image>
          <div className="w-full">
            <Image
              className="object-cover mx-auto"
              src={url}
              width={250}
              height={250}
            ></Image>
          </div>
          <h1 className="font-semibold text-gray-500 text-xl">{`#${number}`}</h1>
          <h1 className="font-semibold text-2xl">{newNick || name}</h1>
          {!newNick ? (
            <div className="flex w-full text-center justify-center">
              {types.map((type, index) => (
                <p key={index} className={typeColors[type]}>
                  {type}
                </p>
              ))}
            </div>
          ) : (
            <div className="flex w-full">
              <p className="p-2 mx-2 font-semibold text-gray-600">{name}</p>
              <div className="flex justify-end">
                {types.map((type, index) => (
                  <p key={index} className={typeColors[type]}>
                    {type}
                  </p>
                ))}
              </div>
            </div>
          )}
        </div>
      ) : (
        <div className="w-64 shadow-lg rounded-xl border-green-500 border-2 text-center m-4">
          <div
            className="w-4 h-4 hover:cursor-pointer hover:scale-150 transition-all bg-red-500 rounded-full m-2 absolute"
            onClick={toggleSetings}
          />
          <p className="mt-12 mx-4">Give this pokemon a nickname?</p>
          <input
            type="text"
            name=""
            id=""
            value={newNickname}
            onChange={(e) => setNewNickname(e.target.value)}
            className="w-40 mb-1 p-2 px-4 border focus:outline-none focus:border-2 focus:ring-blue-600 border-blue-600 rounded mx-auto"
          />
          <br />
          <button
            className="bg-blue-500 font-bold p-4 hover:scale-105 transition-all  py-2 mt-1 rounded text-white"
            onClick={handleSetNickname}
          >
            Update
          </button>
          <p className="mt-8 text-xl">Remove this pokemon?</p>
          <button
            className="bg-red-500 font-bold hover:scale-105 transition-all p-4 mt-1 py-2 rounded text-white"
            onClick={handleDeletion}
          >
            Delete
          </button>
        </div>
        
      )}
    </>
  );
};

export default Card;
