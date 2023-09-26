import Image from "next/image";
import Dashboard from "@/components/Dashboard";
import Formulario from "@/components/Formulario";
export default function Home() {
  return (
    <>
    <div className="p-8">

      <h1 className="text-4xl font-semibold p-2">Nova previsão:</h1>
      <Formulario />
      <h2 className="text-4xl font-semibold p-2">Estatísticas:</h2>
      <Dashboard />
    </div>
    </>
  );
}
