'use client'
import React from 'react'
import axios from 'axios';
import { useState, useEffect } from 'react';
export default function Formulario() {
    const [lastResultStr, setLastResultStr] = useState('45 anos, sálario de 45k e mulher: 45% em 22/05/2004') 
    const [selectValue, setSelectValue] = useState(0)
    const handleSelectChange = (e: any) => {
      setSelectValue(e.target.value);
    };

    const handleSubmit = (e: any) => {
      e.preventDefault();
      const formData = new FormData(e.target);
      formData.append("gender", selectValue.toString())
      const data = Object.fromEntries(formData);
      console.log(data)
      axios.post("http://44.201.102.34:4000/client/run", data
      ).then((res) => {
        const {age: resAge, income: resIncome, gender: resGender, result: resResult} = res.data
        setLastResultStr(`${resAge} anos, sálario de ${resIncome}k e ${resGender} → ${resResult}%`)
      })
    };

  return (
    <div>
        <form onSubmit={handleSubmit}>
            <input type="number" name="age" placeholder="idade" className='bg-gray-300 rounded w-20'/>
            <input type="text" name="income" placeholder="Sálario (em kR$/mês)"  className='bg-gray-300 rounded mx-4'/>
            <select name="" id="" placeholder='Gênero' value={selectValue} onChange={handleSelectChange}>
                <option value={0}>Masculino</option>
                <option value={1}>Feminino</option>
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
