package main

import (
	"net/http"

	"golang.org/x/net/websocket"
)

type Pair struct {
	Sockets []*websocket.Conn
}

func (p Pair) Echo(ws *websocket.Conn) {
	p.Sockets = append(p.Sockets, ws)

	for _, conn := range p.Sockets {
		conn.Write([]byte("Hello"))
	}
}

func main() {
	var p Pair

	http.Handle("/echo", websocket.Handler(p.Echo))
	http.Handle("/", http.FileServer(http.Dir("./statics")))
	err := http.ListenAndServe(":8001", nil)
	if err != nil {
		panic(err.Error())
	}
}
