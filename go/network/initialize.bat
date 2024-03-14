@echo off

echo Configure GOPROXY Environment Variable
set "GOPROXY=https://goproxy.io,direct"

echo Set private repositories or groups that do not go through the proxy
set "GOPRIVATE=git.mycompany.com,github.com/my/private"

echo Initialize Go Modules
go mod init network
go mod tidy

echo Installing dlv
go install -v github.com/go-delve/delve/cmd/dlv@latest

echo Installing gopls
go install -v golang.org/x/tools/gopls@latest

echo Initialization Completed

pause
