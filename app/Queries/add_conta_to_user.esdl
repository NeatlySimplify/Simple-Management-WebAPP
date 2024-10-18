update User filter .id = <uuid>$user_id set{
    conta += (insert Conta {
            bankName := <str>$bankName,
            agency := <str>$agency,
            accountNumber := <str>$accountNumber,
            saldo := <float32>$saldo,
            tipo_conta:= <str>$tipo_conta
        }
    )
}

