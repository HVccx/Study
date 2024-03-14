@echo off

echo Downloading...
go mod init network
go mod tidy

echo Build ing...
go build -ldflags="-s -w -H=windowsgui" -o GetInfo.exe -trimpath main.go