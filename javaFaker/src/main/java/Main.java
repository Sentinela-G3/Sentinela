import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws InterruptedException {

        System.out.println("\nQuantos dados deseja monitorar?");
        Scanner input = new Scanner(System.in);

        Integer repeticoes = input.nextInt();


            Dados dadosMaquina1 = new Dados();





            List<Double>ID = new ArrayList<>();
            List<Double> CPU_frequencia = new ArrayList<>();
            List<Double> RAM_utilizada = new ArrayList<>();
            List<Double> RAM_naoutilizada = new ArrayList<>();
            List<Double> RAM_total = new ArrayList<>();
            List<Double> RAM_disponivel = new ArrayList<>();
            List<Double> tempoAtivo = new ArrayList<>();
            List<Double> tempoInativo = new ArrayList<>();
            List<Double> tempoCPU = new ArrayList<>();
            List<Double> ArmazenamentoDisponivel = new ArrayList<>();
            List<Double> ArmazenamentoIndisponivel = new ArrayList<>();
            List<Double> ArmazenamentoTotal = new ArrayList<>();
            List<Double> Bateria = new ArrayList<>();
            List<Double> CPU_Porcentos = new ArrayList<>();
            List<Double> RAM_utilizadaPorcento = new ArrayList<>();
            List<Double> RAM_naoutilizadaPorcento = new ArrayList<>();
            List<Double> ArmazenamentoIndisponivelPorcento = new ArrayList<>();

            List<List> Componentes = new ArrayList<>();

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
                CPU_Porcentos.add((double)dadosMaquina1.getCPU_Porcentos());
                RAM_utilizadaPorcento.add((double)dadosMaquina1.getRAM_utilizadaPorcento());
                RAM_naoutilizadaPorcento.add((double)dadosMaquina1.getRAM_naoutilizadaPorcento());
                ArmazenamentoIndisponivelPorcento.add((double)dadosMaquina1.getArmazenamentoIndisponivelPorcento());
                dadosMaquina1.repetir(repeticoes);


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


        System.out.println("\nOh Não!! os dados estão tudo bagunçado!! quer que eu arrume?");
        System.out.println("1-Organizar por ID \n2-Organizar por maior número \n3- Organizar por menor número\n4-Não quero");
        Integer escolha = input.nextInt();
        // Thread.sleep(1000);

        if (escolha == 1) {
            for (int i = 0; i < ID.size(); i++) {
                List<Double> ComponenteAtual = Componentes.get(i);
                for (int j = i + 1; j < ComponenteAtual.size(); j++) {
                    if (ComponenteAtual.get(i) < ComponenteAtual.get(j)) {
                        // Swap elements
                        double aux = ComponenteAtual.get(i);
                        ComponenteAtual.set(i, ComponenteAtual.get(j));
                        ComponenteAtual.set(j, aux);
                    }
                }
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
        } else if (escolha.equals(2)) {

        } else if (escolha.equals(3)) {

        }else {

        }




//        System.out.println("CPU_porcento(%) : " + dadosMaquina1.getCPU_Porcentos() + "%");
//        System.out.println("CPU_frequencia(GHz) : " + dadosMaquina1.getCPU_frequencia() + " GHz");
//        System.out.println("RAM_utilizada(Gb) : " + dadosMaquina1.getRAM_utilizada()+ " Mb");
//        System.out.println("RAM_naoutilizada(Gb) : " + dadosMaquina1.getRAM_naoutilizada()+ " Mb");
//        System.out.println("RAM_total(Gb) : " + dadosMaquina1.getRAM_total()+ " Mb");
//        System.out.println("RAM_disponivel(Gb): " + dadosMaquina1.getRAM_disponivel()+ " Mb");
//        System.out.println("tempoAtivo(M) : " + dadosMaquina1.getTempoAtivo() + " Minutos");
//        System.out.println("tempoInativo(M) : " + dadosMaquina1.getTempoInativo() + " Minutos");
//        System.out.println("tempoCPU(M) : " + dadosMaquina1.getTempoCPU()+ " Minutos");
//        System.out.println("ArmazenamentoDisponivel(Gb) : " + dadosMaquina1.getArmazenamentoDisponivel() + " Mb");
//        System.out.println("ArmazenamentoIndisponivel(Gb) : " + dadosMaquina1.getArmazenamentoIndisponivel()+ " Mb");
//        System.out.println("ArmazenamentoTotal(Gb) : " + dadosMaquina1.getArmazenamentoTotal()+ " Mb");
//        System.out.println("Bateria: " + dadosMaquina1.getBateria() + "%");


        }

    }


