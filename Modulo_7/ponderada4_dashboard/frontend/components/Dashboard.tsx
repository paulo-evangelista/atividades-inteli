import React, { useEffect } from "react";
import { useState } from "react";
import axios from "axios";
import { Bar, BarChart, CartesianGrid, Cell, Legend, Line, LineChart, Pie, PieChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

const COLORS = ['#0099ff', '#ff00dd'];


export default function Dashboard() {
  const [ageVsIncome, setAgeVsIncome] = useState([]);
  const [maleVsFemale, setMaleVsFemale] = useState([{ name: 'male', value: 9 },{ name: 'female', value: 4 }]);
  const updateStatistics = () => {
    axios.get("http://44.201.102.34:4000/client/statistics").then((response) => {
      console.log(response.data);
      setAgeVsIncome(response.data.ageVsIncome);
      setMaleVsFemale(response.data.maleVsFemale);
      setTimeout(() => {
        console.log(maleVsFemale);
      }, 1000);
    });
  };
  useEffect(()=> {
    updateStatistics();
  }, [])
  return (
    <>
      <button className="text-xl px-4 py-2 bg-blue-500 rounded-lg transition hover:scale-110 text-white font-medium m-4" onClick={updateStatistics}>Atualizar Dashboard</button>
    <div className="w-full flex flex-wrap gap-6">
      
      {/* PRIMEIRO GRAPH */}
      <div className=" bg-blue-100 p-8 border-2 text-center border-blue-700 rounded-xl">
        <p className="text-2xl font-semibold text-black">Quantidade de registros masc. x fem.</p>
        <PieChart width={500} height={500}>
          <Pie
            cx="50%"
            cy="50%"
            labelLine={false}
            outerRadius={140}
            fill="#8884d8"
            data={maleVsFemale}
            label
            dataKey="value"
            >

        {maleVsFemale.map((entry, index) => (
          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
          ))}
          </Pie>
        </PieChart>
      </div>
          {/* SEGUNDO GRAPH */}
      <div className=" bg-blue-100 text-center p-8 border-2 border-blue-700 rounded-xl">
        <p className="text-2xl font-semibold text-black">Salário médio por idade</p>
      <LineChart
          width={900}
          height={500}
          data={ageVsIncome}
         
          >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="age" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="income" stroke="#8884d8" strokeWidth={2} />
        </LineChart>
      </div>
      <div className="bg-blue-100 p-8 border-2 text-center border-blue-700 rounded-xl">
        <p className="text-2xl font-semibold text-black">Quantidade de registros por idade</p>
          {/* TERCEIRO GRAPH */}
      <BarChart
          width={1000}
          height={500}
          data={ageVsIncome}
          
          >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="age" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="amountOfMeans" fill="#82ca9d" />
        </BarChart>
      </div>
    </div>
          </>
  );
}
