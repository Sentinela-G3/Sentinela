import com.github.javafaker.Faker;

public class Dados {
    Faker faker = new Faker();



    private Double ID;
    private Double CPU_frequencia;
    private Double RAM_utilizada;
    private Double RAM_naoutilizada;
    private Double RAM_total;
    private Double RAM_disponivel;
    private Double tempoAtivo;
    private Double tempoInativo;
    private Double tempoCPU;
    private Double ArmazenamentoDisponivel;
    private Double ArmazenamentoIndisponivel;
    private Double ArmazenamentoTotal;
    private Double Bateria;

    private Integer CPU_Porcentos;
    private Integer RAM_utilizadaPorcento;
    private Integer RAM_naoutilizadaPorcento;
    private Integer ArmazenamentoIndisponivelPorcento;

    public Dados() {

        this.ID = faker.number().randomDouble(0,0,100);
        this.CPU_frequencia = faker.number().randomDouble(2, 0, (int) 5.0);
        this.RAM_utilizada = faker.number().randomDouble(2, 0, 32);
        this.RAM_naoutilizada = faker.number().randomDouble(2, 0, 32);
        this.RAM_total = 32.0;
        this.RAM_disponivel = this.RAM_total - this.RAM_utilizada;
        this.tempoAtivo = faker.number().randomDouble(2, 1, 24);
        this.tempoInativo = faker.number().randomDouble(2, 1, 24);
        this.tempoCPU = faker.number().randomDouble(2, 0, 24);
        this.ArmazenamentoIndisponivel = faker.number().randomDouble(2, 0, 1000);
        this.ArmazenamentoTotal = 1000.0;
        this.ArmazenamentoDisponivel = this.ArmazenamentoTotal - this.ArmazenamentoIndisponivel;
        this.Bateria = faker.number().randomDouble(0, 0, 100);


        CPU_Porcentos = (int)((this.CPU_frequencia *100) / 5.0) ;

        RAM_utilizadaPorcento = (int) ((this.RAM_utilizada * 100) / this.RAM_total);

        RAM_naoutilizadaPorcento = (int)((this.RAM_naoutilizada *100) / this.RAM_total);

        ArmazenamentoIndisponivelPorcento = (int)((this.ArmazenamentoIndisponivel *100) / this.ArmazenamentoTotal);



    }

    public Integer repetir(Integer vezes){
        for (int i = 0; i < vezes; i++) {

            this.ID = faker.number().randomDouble(0,1,0);
            this.CPU_frequencia = faker.number().randomDouble(2, 0, (int) 5.0);
            this.RAM_utilizada = faker.number().randomDouble(2, 0, 32);
            this.RAM_naoutilizada = faker.number().randomDouble(2, 0, 32);
            this.RAM_total = 32.0;
            this.RAM_disponivel = this.RAM_total - this.RAM_utilizada;
            this.tempoAtivo = faker.number().randomDouble(2, 1, 24);
            this.tempoInativo = faker.number().randomDouble(2, 1, 24);
            this.tempoCPU = faker.number().randomDouble(2, 0, 24);
            this.ArmazenamentoIndisponivel = faker.number().randomDouble(2, 0, 1000);
            this.ArmazenamentoTotal = 1000.0;
            this.ArmazenamentoDisponivel = this.ArmazenamentoTotal - this.ArmazenamentoIndisponivel;
            this.Bateria = faker.number().randomDouble(0, 0, 100);


            CPU_Porcentos = (int)((this.CPU_frequencia *100) / 5.0) ;

            RAM_utilizadaPorcento = (int) ((this.RAM_utilizada * 100) / this.RAM_total);

            RAM_naoutilizadaPorcento = (int)((this.RAM_naoutilizada *100) / this.RAM_total);

            ArmazenamentoIndisponivelPorcento = (int)((this.ArmazenamentoIndisponivel *100) / this.ArmazenamentoTotal);

        }
        return 0;
    };

    public Double getID() {
        return ID;
    }

    public Double getCPU_frequencia() {
        return CPU_frequencia;
    }

    public Double getRAM_utilizada() {
        return RAM_utilizada;
    }

    public Double getRAM_naoutilizada() {
        return RAM_naoutilizada;
    }

    public Double getRAM_total() {
        return RAM_total;
    }

    public Double getRAM_disponivel() {
        return RAM_disponivel;
    }

    public Double getTempoAtivo() {
        return tempoAtivo;
    }

    public Double getTempoInativo() {
        return tempoInativo;
    }

    public Double getTempoCPU() {
        return tempoCPU;
    }

    public Double getArmazenamentoDisponivel() {
        return ArmazenamentoDisponivel;
    }

    public Double getArmazenamentoIndisponivel() {
        return ArmazenamentoIndisponivel;
    }

    public Double getArmazenamentoTotal() {
        return ArmazenamentoTotal;
    }

    public Double getBateria() {
        return Bateria;
    }

    public Integer getCPU_Porcentos() {
        return CPU_Porcentos;
    }

    public Integer getRAM_utilizadaPorcento() {
        return RAM_utilizadaPorcento;
    }

    public Integer getRAM_naoutilizadaPorcento() {
        return RAM_naoutilizadaPorcento;
    }

    public Integer getArmazenamentoIndisponivelPorcento() {
        return ArmazenamentoIndisponivelPorcento;
    }
}

