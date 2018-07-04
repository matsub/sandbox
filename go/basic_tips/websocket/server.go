package main

import (
	"io"
	"net/http"

	"golang.org/x/net/websocket"
)

func echo(ws *websocket.Conn) {
	io.Copy(ws, ws)
}

func main() {
	http.Handle("/echo", websocket.Handler(echo))
	http.Handle("/", http.FileServer(http.Dir("./statics")))
	err := http.ListenAndServe(":8001", nil)
	if err != nil {
		panic(err.Error())
	}
}
