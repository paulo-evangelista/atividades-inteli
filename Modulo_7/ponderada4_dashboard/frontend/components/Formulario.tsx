'use client'
import React from 'react'
import { toast } from "react-toastify";
import { useState, useEffect } from 'react';
export default function Formulario() {
    const [lastResultStr, setLastResultStr] = useState('45 anos, sálario de 45k e mulher: 45% em 22/05/2004') 
    const handleSubmit = (e: any) => {
      e.preventDefault();
      const formData = new FormData(e.target);
      const data = Object.fromEntries(formData);
      const id = toast.loading("Your message is being sent...");
      fetch("/api/contact", {
        method: "POST",
        body: JSON.stringify(data),
      }).then((res) => {
        if (res.status === 200) {
          toast.update(id, {
            render: "Message sent! we'll be in touch soon!",
            type: "success",
            isLoading: false,
            autoClose: 4000,
            closeButton: true,
          });
        } else {
          toast.update(id, {
            render: "Oops, there was a problem sending your message :(",
            type: "error",
            isLoading: false,
            autoClose: 4000,
            closeButton: true,
          });
        }
      });
    };

  return (
    <div>
        <form onSubmit={handleSubmit}>
            <input type="number" name="age" placeholder="idade" className='bg-gray-300 rounded w-20'/>
            <input type="text" name="income" placeholder="Sálario (em kR$/mês)"  className='bg-gray-300 rounded mx-4'/>
            <select name="" id="" placeholder='Gênero'>
                <option value="0">Masculino</option>
                <option value="1">Feminino</option>
            </select>
            <button className='rounded p-2 bg-blue-500 mx-4 px-4 hover:scale-110 hover:bg-blue-400 transition' type={"submit"}>Enviar</button>
        </form>
        <div className='border-2 w-fit px-4 pb-2 border-blue-500 rounded-lg'>

        <p className='text-xl mb-4 font-semibold'>Resultado da última previsão:</p>
        <p>{lastResultStr}</p>
        </div>
    </div>
  )
}
