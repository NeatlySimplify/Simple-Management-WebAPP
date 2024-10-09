CREATE MIGRATION m1kixgazrag7fazvdr277rzahpmo3pe77phtaxenmdozhdycslkn6q
    ONTO m1yjptcpmco75nss34nyr2o4pvuy3i4hz2bdxa7m6yryhflpvri5na
{
  ALTER TYPE default::Finance {
      CREATE PROPERTY details: std::str;
  };
  ALTER TYPE default::Service {
      ALTER PROPERTY descricao {
          RENAME TO details;
      };
  };
  ALTER TYPE default::Processo {
      CREATE PROPERTY fase: std::str;
  };
};
