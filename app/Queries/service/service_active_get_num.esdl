select <int16>(
    (
        select count(
            select Services filter status = "active"
        )
    )
);
