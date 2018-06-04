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

func standard() {
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

func main() {
	// standard()
	// Token from another example.  This token is expired
	var tokenString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIiLCJleHAiOjE1MDAwLCJpc3MiOiJ0ZXN0In0.HE7fK0xOQwFEr4WDgRWj4teRPZ6i3GLwD5YCm6Pwu_c"
	tokenString = "foo"

	if token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		return []byte("AllYourBase"), nil
	}); err != nil {
		log.Println(err)
	} else {
		if token.Valid {
			log.Println("You look nice today")
		} else if ve, ok := err.(*jwt.ValidationError); ok {
			if ve.Errors&jwt.ValidationErrorMalformed != 0 {
				log.Println("That's not even a token")
			} else if ve.Errors&(jwt.ValidationErrorExpired|jwt.ValidationErrorNotValidYet) != 0 {
				// Token is either expired or not
				// active yet
				log.Println("Timing is everything")
			} else {
				log.Println("Couldn't handle this token:", err)
			}
		} else {
			log.Println("Couldn't handle this token:", err)
		}
	}
}
