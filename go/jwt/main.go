package main

import (
	"errors"
	"log"

	jwt "github.com/dgrijalva/jwt-go"
)

type User struct {
	ID    string `json:"id"`
	Email string `json:"email"`
	jwt.StandardClaims
}

func createTokenString(alg string) string {
	// Embed User information to `token`
	token := jwt.NewWithClaims(jwt.GetSigningMethod(alg), &User{
		ID:    "foobar",
		Email: "foo@example.com",
	})
	// token -> string. Only server knows this secret.
	tokenstring, err := token.SignedString([]byte("supersecret"))
	if err != nil {
		log.Fatalln(err)
	}
	return tokenstring
}

func main() {
	// for example, server receive token string in request header.
	tokenstring := createTokenString("HS256")
	// This is that token string.
	log.Println(tokenstring)

	// Let's parse this by the secrete, which only server knows.
	token, err := jwt.Parse(tokenstring, func(token *jwt.Token) (interface{}, error) {
		return []byte("supersecret"), nil
	})
	log.Println(token.Claims, err)

	// In another way, you can decode token to your struct, which needs to satisfy `jwt.StandardClaims`
	user := User{}
	token, err = jwt.ParseWithClaims(tokenstring, &user, func(token *jwt.Token) (interface{}, error) {
		return []byte("supersecret"), nil
	})
	log.Println(token.Valid, user.ID, err)

	// nonealg
	tokenstring = "eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0eyJJRCI6ImZvb2JhciIsIkVtYWlsIjoiZm9vQGV4YW1wbGUuY29tIn0."
	token, err = jwt.ParseWithClaims(tokenstring, &user, func(token *jwt.Token) (interface{}, error) {
		return []byte("supersecret"), nil
	})
	defer func() {
		if recover() != nil {
			err = errors.New("うおお")
		}
	}()
	if err != nil {
		log.Println("やべえ")
	}
	log.Println(token.Valid, user.ID, err)
}
