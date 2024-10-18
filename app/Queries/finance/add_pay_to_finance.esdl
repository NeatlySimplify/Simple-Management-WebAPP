update Finance filter .id = <uuid>$id set {
    pagamento += (insert Pagamento{
        user_id:= <uuid>$user_id,
        finance_id:= Finance.id,
        valor:= <float32>$valor,
        status:= <bool>$status,
        data_pagamento:= <datetime>$data_pagamento,
        parcela:= <int16>$parcela,
        evento:= (insert Scheduler {
            user_id:= <uuid>$user_id,
            nome:= Finance.nome,
            status:= <bool>$status,
            end_time:= <datetime>$data_pagamento,
            details:= Finance.details,
            tag_tipo:= Finance.tag_tipo
        }
        )
        }
    )
}


