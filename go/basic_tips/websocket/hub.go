package main

// Hub maintains the set of active clients and broadcasts messages to the
// clients.
type Hub struct {
	clients map[*Client]bool
	broadcast chan []byte
	join chan *Client
	leave chan *Client
}

func newHub() *Hub {
	return &Hub{
		clients:   make(map[*Client]bool),
		broadcast: make(chan []byte),
		join:      make(chan *Client),
		leave:     make(chan *Client),
	}
}

func (h *Hub) run() {
	for {
		select {
		case client := <-h.join:
			h.clients[client] = true

		case client := <-h.leave:
			if _, exist := h.clients[client]; exist {
				delete(h.clients, client)
				close(client.send)
			}

		case message := <-h.broadcast:
			for client := range h.clients {
				select {
				case client.send <- message:
				default:
					close(client.send)
					delete(h.clients, client)
				}
			}
		}
	}
}
