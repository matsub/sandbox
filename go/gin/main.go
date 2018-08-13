package main

import (
	"matsub/sandbox/go/gin/database"
	"matsub/sandbox/go/gin/models"
	"matsub/sandbox/go/gin/routes"
)

func main() {
	// Migrate the schema
	db := database.Connect()
	db.AutoMigrate(&models.Todo{})

	router := routes.Router()
	router.Run()
}
