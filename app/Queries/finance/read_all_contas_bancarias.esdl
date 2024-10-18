select People {
    conta: {
        bankName,
        agency,
        accountNumber,
        saldo,
        tipo_conta
    }
} filter .id = $id;