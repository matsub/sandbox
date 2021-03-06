package database

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
)

func Connect() *gorm.DB {
	db, err := gorm.Open("postgres", "host=postgres user=sandbox dbname=sandbox sslmode=disable password=sandbox")
	if err != nil {
		panic("failed to connect database")
	}
	return db
}
