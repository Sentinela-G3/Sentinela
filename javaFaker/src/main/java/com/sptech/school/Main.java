package com.sptech.school;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws InterruptedException {

        System.out.println("\nQuantos dados deseja monitorar?");
        Scanner input = new Scanner(System.in);

        Integer repeticoes = input.nextInt();

        Dados dadosMaquina1 = new Dados();

        List<String> ID = new ArrayList<>();
        List<String> CPU_frequencia = new ArrayList<>();
        List<String> RAM_utilizada = new ArrayList<>();
        List<String> RAM_naoutilizada = new ArrayList<>();
        List<String> RAM_total = new ArrayList<>();
        List<String> RAM_disponivel = new ArrayList<>();
        List<String> tempoAtivo = new ArrayList<>();
        List<String> tempoInativo = new ArrayList<>();
        List<String> tempoCPU = new ArrayList<>();
        List<String> ArmazenamentoDisponivel = new ArrayList<>();
        List<String> ArmazenamentoIndisponivel = new ArrayList<>();
        List<String> ArmazenamentoTotal = new ArrayList<>();
        List<String> Bateria = new ArrayList<>();
        List<String> CPU_Porcentos = new ArrayList<>();
        List<String> RAM_utilizadaPorcento = new ArrayList<>();
        List<String> RAM_naoutilizadaPorcento = new ArrayList<>();
        List<String> ArmazenamentoIndisponivelPorcento = new ArrayList<>();

        // lista de listas
        List<List<String>> Componentes = new ArrayList<>();
            // listas individuais
        Componentes.add(ID);
        Componentes.add(CPU_frequencia);
        Componentes.add(RAM_utilizada);
        Componentes.add(RAM_naoutilizada);
        Componentes.add(RAM_total);
        Componentes.add(RAM_disponivel);
        Componentes.add(tempoAtivo);
        Componentes.add(tempoInativo);
        Componentes.add(tempoCPU);
        Componentes.add(ArmazenamentoDisponivel);
        Componentes.add(ArmazenamentoIndisponivel);
        Componentes.add(ArmazenamentoTotal);
        Componentes.add(Bateria);
        Componentes.add(CPU_Porcentos);
        Componentes.add(RAM_utilizadaPorcento);
        Componentes.add(RAM_naoutilizadaPorcento);
        Componentes.add(ArmazenamentoIndisponivelPorcento);

        // adicionando dados em cada lista
        for (int i = 0; i < repeticoes; i++) {
            dadosMaquina1.repetir(repeticoes);
            ID.add(dadosMaquina1.getID());
            CPU_frequencia.add(dadosMaquina1.getCPU_frequencia());
            RAM_utilizada.add(dadosMaquina1.getRAM_utilizada());
            RAM_naoutilizada.add(dadosMaquina1.getRAM_naoutilizada());
            RAM_total.add(dadosMaquina1.getRAM_total());
            RAM_disponivel.add(dadosMaquina1.getRAM_disponivel());
            tempoAtivo.add(dadosMaquina1.getTempoAtivo());
            tempoInativo.add(dadosMaquina1.getTempoInativo());
            tempoCPU.add(dadosMaquina1.getTempoCPU());
            ArmazenamentoDisponivel.add(dadosMaquina1.getArmazenamentoDisponivel());
            ArmazenamentoIndisponivel.add(dadosMaquina1.getArmazenamentoIndisponivel());
            ArmazenamentoTotal.add(dadosMaquina1.getArmazenamentoTotal());
            Bateria.add(dadosMaquina1.getBateria());
            CPU_Porcentos.add(dadosMaquina1.getCPU_Porcentos());
            RAM_utilizadaPorcento.add(dadosMaquina1.getRAM_utilizadaPorcento());
            RAM_naoutilizadaPorcento.add(dadosMaquina1.getRAM_naoutilizadaPorcento());
            ArmazenamentoIndisponivelPorcento.add(dadosMaquina1.getArmazenamentoIndisponivelPorcento());
        }

        System.out.flush();

        System.out.println("\nID: " + ID);
        System.out.println("CPU_frequencia: " + CPU_frequencia);
        System.out.println("RAM_utilizada: " + RAM_utilizada);
        System.out.println("RAM_naoutilizada: " + RAM_naoutilizada);
        System.out.println("RAM_total: " + RAM_total);
        System.out.println("RAM_disponivel: " + RAM_disponivel);
        System.out.println("tempoAtivo: " + tempoAtivo);
        System.out.println("tempoInativo: " + tempoInativo);
        System.out.println("tempoCPU: " + tempoCPU);
        System.out.println("ArmazenamentoDisponivel: " + ArmazenamentoDisponivel);
        System.out.println("ArmazenamentoIndisponivel: " + ArmazenamentoIndisponivel);
        System.out.println("ArmazenamentoTotal: " + ArmazenamentoTotal);
        System.out.println("Bateria: " + Bateria);
        System.out.println("CPU_Porcentos: " + CPU_Porcentos);
        System.out.println("RAM_utilizadaPorcento: " + RAM_utilizadaPorcento);
        System.out.println("RAM_naoutilizadaPorcento: " + RAM_naoutilizadaPorcento);
        System.out.println("ArmazenamentoIndisponivelPorcento: " + ArmazenamentoIndisponivelPorcento);

        System.out.println("\nOh Não!! os dados estão bagunçados!! quer que eu arrume?");
        System.out.println("1-Organizar por ID");
        Integer escolha = input.nextInt();
    // SelectionSort para os dados
        for (int i = 0; i < ID.size() - 1; i++) {
            int indMenor = i;
            for (int j = i + 1; j < ID.size(); j++) {
                if (Integer.parseInt(ID.get(indMenor)) > Integer.parseInt(ID.get(j))) {
                    indMenor = j;
                }
            }

            if (indMenor != i) {
                String auxID = ID.get(i);
                ID.set(i, ID.get(indMenor));
                ID.set(indMenor, auxID);

                for (int k = 1; k < Componentes.size(); k++) {
                    List<String> componente = Componentes.get(k);
                    String auxComponente = componente.get(i);
                    componente.set(i, componente.get(indMenor));
                    componente.set(indMenor, auxComponente);
                }
            }
        }

        System.out.println("\nComponentes ordenados pelo ID:");

        System.out.println("ID: " + ID);
        System.out.println("CPU_frequencia: " + CPU_frequencia);
        System.out.println("RAM_utilizada: " + RAM_utilizada);
        System.out.println("RAM_naoutilizada: " + RAM_naoutilizada);
        System.out.println("RAM_total: " + RAM_total);
        System.out.println("RAM_disponivel: " + RAM_disponivel);
        System.out.println("tempoAtivo: " + tempoAtivo);
        System.out.println("tempoInativo: " + tempoInativo);
        System.out.println("tempoCPU: " + tempoCPU);
        System.out.println("ArmazenamentoDisponivel: " + ArmazenamentoDisponivel);
        System.out.println("ArmazenamentoIndisponivel: " + ArmazenamentoIndisponivel);
        System.out.println("ArmazenamentoTotal: " + ArmazenamentoTotal);
        System.out.println("Bateria: " + Bateria);
        System.out.println("CPU_Porcentos: " + CPU_Porcentos);
        System.out.println("RAM_utilizadaPorcento: " + RAM_utilizadaPorcento);
        System.out.println("RAM_naoutilizadaPorcento: " + RAM_naoutilizadaPorcento);
        System.out.println("ArmazenamentoIndisponivelPorcento: " + ArmazenamentoIndisponivelPorcento);
    }
}