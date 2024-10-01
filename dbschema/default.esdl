module default {


    abstract type People {
        timestamp: datetime_of_statement();
        required email: str {
            delegated constraint exclusive;
        };
        nome: str;
        sexo: str;
        estado_civil: str;
        details: str
        tipo_pessoa: str
        multi evento: Scheduler
        multi telefone: Telefone;
        multi endereco: Endereco;
    }


    abstract type Service {
        status: bool
        valor: float32;
        descricao: str;
        multi evento: Scheduler
    }


    type Telefone {
        tipo: str
        ddd: str
        numero: str
        contato: str
        details: str
    }


    type Auditable {
        timestamp: datetime_of_statement();
        user: str;
        action: str;
        details: json;
    }


    type Scheduler {
        nome: str;
        status: bool;
        end_time: datetime
        start_time: datetime
        details: str;
        tipo_origem: str
    }


     type Conta {
        bankName: str;
        agency: str;
        accountNumber: str;
        saldo: float32;
        tipo_conta: str;
    }


    type Endereco {
        rua: str;
        numero: str;
        complemento: str;
        bairro: str;
        cep: str;
        cidade: str;
        estado: str
    } 


    type PessoaFisica extending People {
        cpf: str
        rg: str
        pis: str
        ctps: str
        serie: str
        nacionalidade: str
        profissao: str
        nome_mae: str
    }


    type PessoaJuridica extending People{
        cnpj: str
        responsavel: str
        tipo_empresa: str
        atividade_principal: str
        inscricao_municipal: str
        inscricao_estadual: str
    }


    type User extending People{
        required password: str {
            constraint min_lenght(6);
            constraint max_lenght(30);
        }
        tipo_user: str;
    }


    type Processo extending Service{
        classe: str
        tipo: str
        rito: str
        forum: str
        comarca: str
        vara: str
    }


    type Finance {
        nome: str;
        valor: float32;
        efetivado: bool;
        categoria: str;
        subcategoria: str;
        conta: Conta;
        multi evento: Scheduler;
    }
}