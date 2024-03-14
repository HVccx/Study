package main

import (
	"bytes"
	"fmt"
	"io"
	"os"
	"os/exec"

	"golang.org/x/text/encoding/simplifiedchinese"
	"golang.org/x/text/transform"
)

// Convert GBK to UTF-8
func convertGBKToUTF8(input []byte) ([]byte, error) {
	reader := transform.NewReader(bytes.NewReader(input), simplifiedchinese.GBK.NewDecoder())
	return io.ReadAll(reader)
}

func main() {
	// 指定输出文件路径
	outputFilePath := "network_info.txt"

	// 执行ipconfig /all 命令
	ipconfigCmd := exec.Command("cmd", "/c", "ipconfig", "/all")
	var ipconfigOut bytes.Buffer
	ipconfigCmd.Stdout = &ipconfigOut
	err := ipconfigCmd.Run()
	if err != nil {
		fmt.Println("Error executing ipconfig command:", err)
		return
	}
	ipconfigUTF8, err := convertGBKToUTF8(ipconfigOut.Bytes())
	if err != nil {
		fmt.Println("Error converting encoding:", err)
		return
	}

	// 执行route print 命令
	routeCmd := exec.Command("cmd", "/c", "route", "print")
	var routeOut bytes.Buffer
	routeCmd.Stdout = &routeOut
	err = routeCmd.Run()
	if err != nil {
		fmt.Println("Error executing route command:", err)
		return
	}
	routeUTF8, err := convertGBKToUTF8(routeOut.Bytes())
	if err != nil {
		fmt.Println("Error converting encoding:", err)
		return
	}

	// 执行arp -a 命令
	arpCmd := exec.Command("cmd", "/c", "arp", "-a")
	var arpOut bytes.Buffer
	arpCmd.Stdout = &arpOut
	err = arpCmd.Run()
	if err != nil {
		fmt.Println("Error executing arp command:", err)
		return
	}
	arpUTF8, err := convertGBKToUTF8(arpOut.Bytes())
	if err != nil {
		fmt.Println("Error converting encoding:", err)
		return
	}

	// 将输出写入文件
	outputFile, err := os.Create(outputFilePath)
	if err != nil {
		fmt.Println("Error creating output file:", err)
		return
	}
	defer outputFile.Close()

	outputFile.WriteString(string(ipconfigUTF8) + "\n" + string(routeUTF8) + "\n" + string(arpUTF8))
	fmt.Printf("Network information has been saved to %s\n", outputFilePath)
}
