package routes

import "github.com/gin-gonic/gin"

func Router() *gin.Engine {
	// Migrate the schema
	router := gin.Default()

	v1 := router.Group("/todos")
	{
		v1.POST("/", CreateTodo)
		v1.GET("/", FetchAllTodo)
		v1.GET("/:id", FetchSingleTodo)
		v1.PUT("/:id", UpdateTodo)
		v1.DELETE("/:id", DeleteTodo)
	}

	return router
}
