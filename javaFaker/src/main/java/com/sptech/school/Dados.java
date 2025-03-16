package com.sptech.school;

import com.github.javafaker.Faker;

public class Dados {
    Faker faker = new Faker();

    private String ID;
    private String CPU_frequencia;
    private String RAM_utilizada;
    private String RAM_naoutilizada;
    private String RAM_total;
    private String RAM_disponivel;
    private String tempoAtivo;
    private String tempoInativo;
    private String tempoCPU;
    private String ArmazenamentoDisponivel;
    private String ArmazenamentoIndisponivel;
    private String ArmazenamentoTotal;
    private String Bateria;

    private String CPU_Porcentos;
    private String RAM_utilizadaPorcento;
    private String RAM_naoutilizadaPorcento;
    private String ArmazenamentoIndisponivelPorcento;

    public Dados() {
        gerarDados();
    }

    private void gerarDados() {
        this.ID = String.valueOf(faker.number().randomNumber(4, false));
        this.CPU_frequencia = String.valueOf(faker.number().randomDouble(2, 0, 5));
        this.RAM_utilizada = String.valueOf(faker.number().randomDouble(2, 0, 32));
        this.RAM_naoutilizada = String.valueOf(faker.number().randomDouble(2, 0, 32));
        this.RAM_total = "32";
        this.RAM_disponivel = String.valueOf(Double.parseDouble(this.RAM_total) - Double.parseDouble(this.RAM_utilizada));
        this.tempoAtivo = String.valueOf(faker.number().randomDouble(2, 1, 24));
        this.tempoInativo = String.valueOf(faker.number().randomDouble(2, 1, 24));
        this.tempoCPU = String.valueOf(faker.number().randomDouble(2, 0, 24));
        this.ArmazenamentoIndisponivel = String.valueOf(faker.number().randomDouble(2, 0, 1000));
        this.ArmazenamentoTotal = "1000";
        this.ArmazenamentoDisponivel = String.valueOf(Double.parseDouble(this.ArmazenamentoTotal) - Double.parseDouble(this.ArmazenamentoIndisponivel));
        this.Bateria = String.valueOf(faker.number().randomDouble(0, 0, 100));

        // Calculando percentuais e armazenando como String
        this.CPU_Porcentos = String.valueOf((int) ((Double.parseDouble(this.CPU_frequencia) * 100) / 5));
        this.RAM_utilizadaPorcento = String.valueOf((int) ((Double.parseDouble(this.RAM_utilizada) * 100) / Double.parseDouble(this.RAM_total)));
        this.RAM_naoutilizadaPorcento = String.valueOf((int) ((Double.parseDouble(this.RAM_naoutilizada) * 100) / Double.parseDouble(this.RAM_total)));
        this.ArmazenamentoIndisponivelPorcento = String.valueOf((int) ((Double.parseDouble(this.ArmazenamentoIndisponivel) * 100) / Double.parseDouble(this.ArmazenamentoTotal)));
    }

    public void repetir(int vezes) {
        for (int i = 0; i < vezes; i++) {
            gerarDados();
        }
    }

    // Getters
    public String getID() {
        return ID;
    }

    public String getCPU_frequencia() {
        return CPU_frequencia;
    }

    public String getRAM_utilizada() {
        return RAM_utilizada;
    }

    public String getRAM_naoutilizada() {
        return RAM_naoutilizada;
    }

    public String getRAM_total() {
        return RAM_total;
    }

    public String getRAM_disponivel() {
        return RAM_disponivel;
    }

    public String getTempoAtivo() {
        return tempoAtivo;
    }

    public String getTempoInativo() {
        return tempoInativo;
    }

    public String getTempoCPU() {
        return tempoCPU;
    }

    public String getArmazenamentoDisponivel() {
        return ArmazenamentoDisponivel;
    }

    public String getArmazenamentoIndisponivel() {
        return ArmazenamentoIndisponivel;
    }

    public String getArmazenamentoTotal() {
        return ArmazenamentoTotal;
    }

    public String getBateria() {
        return Bateria;
    }

    public String getCPU_Porcentos() {
        return CPU_Porcentos;
    }

    public String getRAM_utilizadaPorcento() {
        return RAM_utilizadaPorcento;
    }

    public String getRAM_naoutilizadaPorcento() {
        return RAM_naoutilizadaPorcento;
    }

    public String getArmazenamentoIndisponivelPorcento() {
        return ArmazenamentoIndisponivelPorcento;
    }
}
