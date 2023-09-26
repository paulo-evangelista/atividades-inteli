import React from 'react'

export default function Dashboard() {
  return (
    <div className='w-full flex flex-wrap gap-6'>
      <div className="h-72 w-96 bg-blue-500 "> gráfico de pizza que mostra se a maioria é mulher ou homem</div>
      <div className="h-72 w-96 bg-blue-500 "> gráfico de linha entre idade e income</div>
      <div className="h-72 w-96 bg-blue-500 "> gráfico de barra entre idade e quantidade de amostras</div>
    </div>
  )
}
