select count(
    select People filter .user_id = <uuid>$user_id and .tag_tipo = "Cliente"
);