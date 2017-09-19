package main

import (
	"./database"
	"./models"
	"./routes"
)

func main() {
	// Migrate the schema
	db := database.Connect()
	db.AutoMigrate(&models.Todo{})

	router := routes.Router()
	router.Run()
}
