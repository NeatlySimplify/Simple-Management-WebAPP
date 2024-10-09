CREATE MIGRATION m1q7ny2tscprk7t5gcq3eo3g7c4x5mrqmlnjkub5r7z7g7sd5tr5ta
    ONTO m12qq4dwoj3f45anqnqjfcjmnhj5pf3h6fdvr7u33ufgubnroovqxa
{
  ALTER TYPE default::Auditable {
      DROP PROPERTY user_id;
  };
  ALTER TYPE default::Auditable {
      CREATE LINK user_id: default::User;
  };
  ALTER TYPE default::PessoaFisica {
      DROP PROPERTY user_id;
  };
  ALTER TYPE default::PessoaFisica {
      CREATE LINK user_id: default::User;
  };
  ALTER TYPE default::PessoaJuridica {
      DROP PROPERTY user_id;
  };
  ALTER TYPE default::PessoaJuridica {
      CREATE LINK user_id: default::User;
  };
  ALTER TYPE default::Service {
      DROP PROPERTY user_id;
  };
  ALTER TYPE default::Service {
      CREATE LINK user_id: default::User;
  };
  ALTER TYPE default::Scheduler {
      DROP PROPERTY user_id;
  };
  ALTER TYPE default::Scheduler {
      CREATE LINK user_id: default::User;
  };
};
