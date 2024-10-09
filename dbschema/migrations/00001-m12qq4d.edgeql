CREATE MIGRATION m12qq4dwoj3f45anqnqjfcjmnhj5pf3h6fdvr7u33ufgubnroovqxa
    ONTO initial
{
  CREATE TYPE default::Auditable {
      CREATE PROPERTY action: std::str;
      CREATE PROPERTY details: std::json;
      CREATE REQUIRED PROPERTY timestamp: std::datetime {
          SET default := (std::datetime_of_statement());
      };
      CREATE PROPERTY user_id: std::uuid;
  };
  CREATE TYPE default::Conta {
      CREATE PROPERTY accountNumber: std::str;
      CREATE PROPERTY agency: std::str;
      CREATE PROPERTY bankName: std::str;
      CREATE PROPERTY saldo: std::float32;
      CREATE PROPERTY tipo_conta: std::str;
  };
  CREATE TYPE default::Scheduler {
      CREATE PROPERTY details: std::str;
      CREATE PROPERTY end_time: std::datetime;
      CREATE PROPERTY nome: std::str;
      CREATE PROPERTY start_time: std::datetime;
      CREATE PROPERTY status: std::bool;
      CREATE PROPERTY tag_tipo: std::str;
      CREATE PROPERTY user_id: std::uuid;
  };
  CREATE TYPE default::Finance {
      CREATE LINK conta: default::Conta;
      CREATE MULTI LINK evento: default::Scheduler;
      CREATE PROPERTY categoria: std::str;
      CREATE PROPERTY efetivado: std::bool;
      CREATE PROPERTY nome: std::str;
      CREATE PROPERTY subcategoria: std::str;
      CREATE PROPERTY tag_tipo: std::str;
      CREATE PROPERTY user_id: std::uuid;
      CREATE PROPERTY valor: std::float32;
  };
  CREATE TYPE default::Endereco {
      CREATE PROPERTY bairro: std::str;
      CREATE PROPERTY cep: std::str;
      CREATE PROPERTY cidade: std::str;
      CREATE PROPERTY complemento: std::str;
      CREATE PROPERTY estado: std::str;
      CREATE PROPERTY numero: std::str;
      CREATE PROPERTY rua: std::str;
  };
  CREATE TYPE default::Telefone {
      CREATE PROPERTY contato: std::str;
      CREATE PROPERTY ddd: std::str;
      CREATE PROPERTY details: std::str;
      CREATE PROPERTY numero: std::str;
      CREATE PROPERTY tipo: std::str;
  };
  CREATE ABSTRACT TYPE default::People {
      CREATE MULTI LINK endereco: default::Endereco;
      CREATE MULTI LINK evento: default::Scheduler;
      CREATE MULTI LINK telefone: default::Telefone;
      CREATE PROPERTY details: std::str;
      CREATE REQUIRED PROPERTY email: std::str {
          CREATE DELEGATED CONSTRAINT std::exclusive;
      };
      CREATE PROPERTY estado_civil: std::str;
      CREATE PROPERTY nome: std::str;
      CREATE PROPERTY sexo: std::str;
      CREATE PROPERTY tag_tipo: std::str;
      CREATE REQUIRED PROPERTY timestamp: std::datetime {
          SET default := (std::datetime_of_statement());
      };
  };
  CREATE TYPE default::PessoaFisica EXTENDING default::People {
      CREATE PROPERTY cpf: std::str;
      CREATE PROPERTY ctps: std::str;
      CREATE PROPERTY nacionalidade: std::str;
      CREATE PROPERTY nome_mae: std::str;
      CREATE PROPERTY pis: std::str;
      CREATE PROPERTY profissao: std::str;
      CREATE PROPERTY rg: std::str;
      CREATE PROPERTY serie: std::str;
      CREATE PROPERTY user_id: std::uuid;
  };
  CREATE TYPE default::User EXTENDING default::People {
      CREATE REQUIRED PROPERTY password: std::str;
  };
  CREATE TYPE default::PessoaJuridica EXTENDING default::People {
      CREATE PROPERTY atividade_principal: std::str;
      CREATE PROPERTY cnpj: std::str;
      CREATE PROPERTY inscricao_estadual: std::str;
      CREATE PROPERTY inscricao_municipal: std::str;
      CREATE PROPERTY responsavel: std::str;
      CREATE PROPERTY tipo_empresa: std::str;
      CREATE PROPERTY user_id: std::uuid;
  };
  CREATE ABSTRACT TYPE default::Service {
      CREATE MULTI LINK evento: default::Scheduler;
      CREATE PROPERTY descricao: std::str;
      CREATE PROPERTY status: std::bool;
      CREATE PROPERTY user_id: std::uuid;
      CREATE PROPERTY valor: std::float32;
  };
  CREATE TYPE default::Processo EXTENDING default::Service {
      CREATE PROPERTY classe: std::str;
      CREATE PROPERTY comarca: std::str;
      CREATE PROPERTY forum: std::str;
      CREATE PROPERTY rito: std::str;
      CREATE PROPERTY tipo: std::str;
      CREATE PROPERTY vara: std::str;
  };
};
