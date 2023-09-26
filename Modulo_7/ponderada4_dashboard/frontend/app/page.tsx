"use client";
import Dashboard from "@/components/Dashboard";
import Formulario from "@/components/Formulario";
import { useEffect } from "react";
import { useRouter } from "next/navigation";
import Historic from "@/components/Historic";

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    if (!localStorage.getItem("token")) {
      router.push("/login");
    }
  }, []);

  return (
    <>
      <div className="p-8">
        <h1 className="text-4xl font-semibold p-2">Nova previsão:</h1>
        <Formulario />
        <h2 className="text-4xl font-semibold p-2">Estatísticas:</h2>
        <Dashboard />
        <h2 className="text-4xl font-semibold p-2">Histórico:</h2>
        <Historic />
      </div>
    </>
  );
}
