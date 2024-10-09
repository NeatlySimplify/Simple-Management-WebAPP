CREATE MIGRATION m1yjptcpmco75nss34nyr2o4pvuy3i4hz2bdxa7m6yryhflpvri5na
    ONTO m1q7ny2tscprk7t5gcq3eo3g7c4x5mrqmlnjkub5r7z7g7sd5tr5ta
{
  ALTER TYPE default::Finance {
      DROP PROPERTY user_id;
  };
  ALTER TYPE default::Finance {
      CREATE LINK user_id: default::User;
  };
  ALTER TYPE default::Service {
      CREATE MULTI LINK finance: default::Finance;
      CREATE PROPERTY categoria: std::str;
  };
};
