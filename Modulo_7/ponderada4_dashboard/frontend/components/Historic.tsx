import React from 'react'
import { useState, useEffect } from 'react'
import axios from 'axios';
export default function Historic() {
    const [historicData, setHistoricData] = useState([])
    useEffect(()=>{
        axios.get("http://localhost:4000/client/historic").then((response) => {
      setHistoricData(response.data);
    });
    },[])
  return (
    historicData.map((item) => (
        <p className='w-full mr-16 border p-1'>{`${item.created_at} -> ${item.gender ? "Mulher" : "Homem"}, salário de ${item.income}kR$ e ${item.age} anos. Resultado: ${item.result}`}</p>
    )
  )
  )
}
