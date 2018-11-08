package main

import (
	"github.com/matsub/sandbox/go/gin/database"
	"github.com/matsub/sandbox/go/gin/models"
	"github.com/matsub/sandbox/go/gin/routes"
)

func main() {
	// Migrate the schema
	db := database.Connect()
	db.AutoMigrate(&models.Todo{})

	router := routes.Router()
	router.Run()
}
