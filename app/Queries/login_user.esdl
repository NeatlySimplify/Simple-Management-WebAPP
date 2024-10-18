select User {
    password,
    salt,
} filter .email = $email;